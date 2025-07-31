# 🚀 GDG Django Event Management System

A robust event management platform built using Django for managing GDG (Google Developer Group) events. It features a fully role-based system with user-specific dashboards, attendance tracking, task assignments, and AI assistant integration.

---

## 📌 Overview

This platform is designed to streamline the process of organizing and managing GDG-related events and activities. With support for multiple user roles like Admin, HOD, Students, and Demo Users, it offers features like:

- Role-based dashboards
- Event creation and approval
- Attendance tracking
- Task management
- Media uploads
- AI assistant integration
- Performance tracking

---

## 🛠️ Core Technologies

- **Backend**: Django 5.2.4
- **Database**: PostgreSQL (via psycopg3)
- **Frontend**: Django templates
- **AI Integration**: Google Generative AI
- **Deployment**: Gunicorn, Whitenoise
- **API Clients**: Supabase, Google API Client

---

## 🧩 Django Apps

- `sers`: Handles user management and roles
- `ai_assistant`: Integrates with AI for assistance and Q&A
- `dashboard`: Central dashboard view for all roles
- `events`: Event creation, approval, and participation
- `gdg_tasks`: Task assignment and status tracking
- `infraises`: Infrastructure-related resource management
- `media`: File uploads and media tracking
- `performance`: Attendance and user performance stats

---

## 👥 Roles & Permissions

- **Admin**: Full access to everything
- **HOD**: Department-specific approvals and oversight
- **Students**: Event registration, attendance, tasks
- **Demo User**: Limited view for testing or trials

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/gdg_django_project.git
cd gdg_django_project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver


---

##📦 Dependencies
Key dependencies from requirements.txt include:

Django==5.2.4

psycopg3 + psycopg2-binary

google-generativeai

supabase

gunicorn

whitenoise

python-dotenv

requests, httpx, grpcio

Pillow (for image handling)
View full list in requirements.txt

##📂 Project Structure
gdg_django_project/
├── ai_assistant/
├── dashboard/
├── events/
├── gdg_tasks/
├── infraises/
├── media/
├── performance/
├── sers/
├── gdg_django_project/    # Settings and root urls
├── manage.py
└── requirements.txt


##🙌 Contributing
Pull requests and improvements are welcome! Please open an issue first to discuss what you’d like to change

##📄 License
This project is licensed under the MIT License.


##🔗 GitHub Repository
git clone https://github.com/gunn2522/GDG_DJANGO.git


##📧 Contact

Author: GUNN Malhotra 

Email: gunnmlhtr@gmail.com


---

### ✅ Next Steps:
- Replace `yourusername` and `your.email@example.com` with your actual GitHub username and email.
- Save this as `README.md` in your root project directory.
- Commit and push it to GitHub:
  ```bash
  git add README.md
  git commit -m "Add project README"
  git push origin main




