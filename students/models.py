from django.db import models
from admins.models import Route
from datetime import date

import uuid
from io import BytesIO
import qrcode
from django.core.files.base import ContentFile


# ================================
# Student Registration Model
# ================================
class studentregistermodel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    mobile = models.CharField(unique=True, max_length=20)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ================================
# Applicant Personal Details
# ================================
class ApplicantDetails(models.Model):
    name = models.CharField(max_length=20)
    father_guardian_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    age_as_on = models.DateField(default=date.today)
    gender = models.CharField(max_length=6)
    aadhaar_no = models.CharField(max_length=12, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name


# ================================
# Residential Address Model
# ================================
class ResidentialAddress(models.Model):
    applicant = models.OneToOneField(
        ApplicantDetails, on_delete=models.CASCADE, related_name="residential_address"
    )
    address = models.TextField(max_length=20)
    district = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.address}, {self.district}, {self.pincode}"


# ================================
# Route Selection + QR Code
# ================================
class RouteSelection(models.Model):
    MONTHLY = 'Monthly'
    QUARTERLY = 'Quarterly'
    ANNUAL = 'Annual'

    PASS_TYPES = [
        (MONTHLY, 'Monthly'),
        (QUARTERLY, 'Quarterly'),
        (ANNUAL, 'Annual'),
    ]

    applicant = models.ForeignKey(ApplicantDetails, on_delete=models.CASCADE, related_name='route_selections')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='route_selections')
    application_status = models.CharField(max_length=20, default='Pending')
    payment_status = models.CharField(max_length=20, default='Unpaid')
    application_number = models.CharField(max_length=20, unique=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    pass_applied_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    pass_valid_upto = models.DateField()

    # Pass type & fare
    pass_type = models.CharField(max_length=10, choices=PASS_TYPES, default=MONTHLY)
    fare_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate unique application number
        if not self.application_number:
            self.application_number = f"APP-{uuid.uuid4().hex[:8].upper()}"

        # Generate QR code once
        if not self.qr_code:
            qr_data = (
                f"Application Number: {self.application_number}\n"
                f"Name: {self.applicant.name}\n"
                f"Expires: {self.pass_valid_upto}\n"
                f"Route: {self.route.start_point} to {self.route.end_point}"
            )
            qr_image = qrcode.make(qr_data)
            buffer = BytesIO()
            qr_image.save(buffer, format='PNG')
            self.qr_code.save(f"{self.application_number}.png", ContentFile(buffer.getvalue()), save=False)

        # Fare calculation
        if self.pass_type == self.MONTHLY:
            self.fare_amount = self.route.fare
        elif self.pass_type == self.QUARTERLY:
            self.fare_amount = self.route.fare * 3
        elif self.pass_type == self.ANNUAL:
            self.fare_amount = self.route.fare * 12

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Application {self.application_number} - {self.applicant.name}"
