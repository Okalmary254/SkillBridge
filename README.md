# 🧠 SkillBridge — MVP

### 📘 Bridging the Gap Between Graduate Skills and Industry Demand

**SkillBridge** is a web platform that analyzes a user’s current skillset (via manual input or resume upload), compares it with real-time job market requirements, and generates a personalized **Skill Gap Report** with recommended learning resources.

---

## 🚀 MVP Features

* 🔍 **Skill Input**: manual entry or CV upload
* 🧠 **NLP Skill Extraction** from uploaded CVs
* 🌐 **Job Data Loading**: mock job postings with in-demand skills
* 📊 **Skill Gap Analysis**: compare user skills with market needs
* 🎯 **Recommendations**: tutorials/courses for missing skills
* 📈 **Dashboard**: visualize owned vs missing skills

---

## 🧱 Project Structure (MVP)

```
skillbridge/
│
├── frontend/                     # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard/
│   │   │   ├── UploadForm.jsx
│   │   │   └── SkillChart.jsx
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   └── UploadResume.jsx
│   │   ├── services/
│   │   │   └── api.js            # fetch/axios wrapper
│   │   └── App.jsx
│   ├── package.json
│   └── .env
│
├── backend/                      # Flask backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── profile.py
│   │   │   ├── jobdata.py
│   │   │   ├── gap.py
│   │   │   └── recommend.py
│   │   ├── services/
│   │   │   ├── nlp.py
│   │   │   └── scraper.py (mock)
│   │   ├── models.py
│   │   └── utils.py
│   ├── requirements.txt
│   └── run.py
│
├── database/
│   └── schema.sql                # optional or migrations folder
│
├── docs/
│   └── api_endpoints.md
│
├── README.md
└── .gitignore
```

---

## ⚙️ Tech Stack

| Layer      | Tool / Library                      |
| ---------- | ----------------------------------- |
| Frontend   | React (Vite or CRA), TailwindCSS    |
| Backend    | Flask (Python) + Flask-RESTful      |
| NLP Engine | spaCy or NLTK                       |
| Database   | SQLite (MVP) / PostgreSQL           |
| Hosting    | Render (backend), Vercel (frontend) |

---

## 🤞 API Overview (MVP)

| Endpoint               | Method | Description                        |
| ---------------------- | ------ | ---------------------------------- |
| `/api/profile/upload`  | POST   | Upload resume (multipart)          |
| `/api/profile/skills`  | POST   | Add manual skills                  |
| `/api/gap/analyze`     | GET    | Compare skills vs market           |
| `/api/recommendations` | GET    | Get recommended learning resources |

---

## 🧰 Setup Instructions

### 💻 Backend (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
pip install -r requirements.txt
flask run
```

**.env Example**

```
FLASK_ENV=development
DATABASE_URL=sqlite:///skillbridge.db
```

---

### 🖥️ Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

**.env Example**

```
VITE_API_URL=http://127.0.0.1:5000/api
```

---

## 🧠 How It Works (MVP Flow)

1. User **uploads a resume** or enters skills manually.
2. Backend extracts skills (via NLP) and stores them.
3. Backend loads **mock job data** (JSON).
4. Comparison engine finds **missing skills**.
5. User gets a **Skill Gap Report** and **learning recommendations**.
6. Dashboard displays charts and progress.

---

## 🧪 Example Response (Skill Gap Analysis)

```json
{
  "user_skills": ["Python", "SQL"],
  "market_skills": ["Python", "SQL", "Flask", "React"],
  "missing_skills": ["Flask", "React"],
  "recommendations": [
    {"skill": "Flask", "resource": "Flask Mega Tutorial"},
    {"skill": "React", "resource": "React Docs Tutorial"}
  ]
}
```

---

## 🧭 Roadmap

* ✅ MVP (Resume upload, skill extraction, gap detection)
* 📊 Add job scraping
* 🧑‍💼 Integrate live APIs (LinkedIn / Indeed)
* 🎓 Personalized learning paths
* 🧰 Mentor matching & gamification

---

## 👥 Contributors

* **Team SkillBridge** – Hackathon MVP
* Tech Stack: React + Flask + spaCy + SQLite