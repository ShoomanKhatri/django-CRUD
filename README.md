# 🚀 **Full CRUD App with React (Vite), Bootstrap, Django & PostgreSQL** ✨

### **Project Stack:**

- **Frontend:** React (Vite) + Bootstrap
- **Backend:** Django + Django REST Framework + PostgreSQL
- **Database:** PostgreSQL

---

### **1️⃣ Backend Setup (Django + PostgreSQL)**

1. **Install dependencies**:

   ```bash
   pip install django djangorestframework psycopg2-binary django-cors-headers
   ```

2. **Create Django project & app**:

   ```bash
   django-admin startproject myproject
   cd myproject
   python manage.py startapp myapp
   ```

3. **Configure PostgreSQL database** in `settings.py`:

   ```bash
   CREATE DATABASE mydatabase;
   CREATE USER myuser WITH PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```

4. **Create API views, serializers & models** for CRUD operations.

5. **Run Django server**:
   ```bash
   python manage.py runserver
   ```

---

### **2️⃣ Frontend Setup (React + Vite + Bootstrap)**

1. **Set up Vite + React**:

   ```bash
   npm create vite@latest myreactapp --template react
   cd myreactapp
   npm install axios bootstrap
   ```

2. **Add Bootstrap in `app.jsx`**:

   ```javascript
   import "bootstrap/dist/css/bootstrap.min.css";
   ```

3. **Create `StudentList` component** to handle CRUD operations via API.

4. **Run React app**:
   ```bash
   npm run dev
   ```

---

### **3️⃣ Final Step**

- Your **Full CRUD app** is now live with **React (Vite)** + **Bootstrap** on the frontend and **Django + PostgreSQL** on the backend. 🎉

---

🎨 **Enjoy Building!** Feel free to customize it and make it your own. 🚀

---
