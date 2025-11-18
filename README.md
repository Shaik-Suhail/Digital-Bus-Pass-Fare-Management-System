
## 📘 Digital Bus Pass & Fare Management System

🌐 Live Project Link

🚀 Hosted on Railway:
https://buspass-system-production.up.railway.app/

This is a web-based Django project designed to streamline the issuance, renewal, and management of bus passes for students and passengers, reducing long queues, paperwork, and manual processing.

---

### 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Django)
- **Database:** SQLite
- **Other Tools:** QR Code generation, PDFKit, ReportLab

---

### 📂 Project Modules

1. **User Registration & Login**
2. **Bus Pass Generation and Renewal**
3. **Admin Approval Panel**
4. **Online Payments (Mock)**
5. **QR Code & PDF Pass Generation**
6. **Search & Validation**
7. **Report Management**

---

### 📷 Screenshots

You can upload screenshots in your GitHub repo and reference them like this:

```md
![Home Page](screenshots/home.png)
![User Login](screenshots/login.png)
![Pass Generation](screenshots/pass_generation.png)
![Payment Gateway](screenshots/payment.png)
```

> 📌 Place your screenshot images inside a `/screenshots` folder in your repo.

---

### 🚀 Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shaik-Suhail/Digital-Bus-Pass-Fare-Management-System.git
   cd Digital-Bus-Pass-Fare-Management-System
   ```

2. **Create a virtual environment & activate it:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Visit `http://127.0.0.1:8000/` in your browser.

---

### 📄 Authors

- Shaik Suhail – 222G5A0515  
- Sunkara S R Harshini Devi – 212G1A05B4  
- Rajanna Gari Range Gowd – 222G5A0512  
- Talari Narendra – 212G1A05B5  
- Yatagiri Muni Anjaneyulu – 212G1A05C2  

Project under the guidance of **Mr. V. Naveen Kumar M.Tech**, Assistant Professor, ALTS.

---

### 📌 Note

- Admin must activate users after registration.
- Use test card details for mock payment flow.
- PDF generation uses `wkhtmltopdf` – install from [wkhtmltopdf.org](https://wkhtmltopdf.org/)

