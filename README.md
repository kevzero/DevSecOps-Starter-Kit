# DevSecOps Starter Kit

## 📌 Overview
This is a **DevSecOps Starter Kit** providing a secure foundation for web applications with:
- **Backend:** FastAPI + PostgreSQL
- **Frontend:** React + Vite
- **Security:** Bandit (Python Security Scan), Trivy (Docker Image Scan)
- **CI/CD:** GitHub Actions pipeline
- **Deployment:** Docker Compose for Dev & Prod

---

## ✅ Features
- Secure API with FastAPI
- React-based frontend (Vite for fast builds)
- PostgreSQL database
- `.env` file for secrets
- Health checks for backend and DB
- CI/CD pipeline with security scans

---

## ⚙️ Requirements
- **Docker** & **Docker Compose**
- **Node.js & npm** (if running frontend locally)
- **Python 3.11+** (if running backend locally)

---

## 🚀 Quick Start (Windows, Mac, Linux)

### 1. Clone repository
```bash
git clone <repo-url>
cd DevSecOps-Starter-Kit
```

### 2. Create environment file
```bash
cp .env.example .env
```
Edit `.env` to set your DB credentials.

### 3. Start services (DEV mode)
```bash
docker-compose up -d
```

### 4. Access services
- **Frontend:** [http://localhost:3000](http://localhost:3000)
- **Backend API:** [http://localhost:8000](http://localhost:8000)
- **Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

### Stop services
```bash
docker-compose down
```

### View logs
```bash
docker-compose logs -f
```
Logs for a specific service:
```bash
docker-compose logs backend
docker-compose logs frontend
```

### Rebuild containers
```bash
docker-compose build --no-cache
```

---

## 🛠 Local Development Without Docker

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Access at: [http://localhost:3000](http://localhost:3000)

---

## 🔐 Security Tools
- **Bandit:** Scans Python code for security issues
- **Trivy:** Scans Docker images for vulnerabilities

Run manually:
```bash
bandit -r backend
./trivy image devsecops-backend
```

---

## ⚡ CI/CD Pipeline
- On every **push**, GitHub Actions will:
  - Run **Bandit** security scan on Python code
  - Build Docker image and scan with **Trivy**

Workflow file: `.github/workflows/devsecops.yml`

---

## 📜 Deployment for Production
Use the production Compose file:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

---

## 🖼 Architecture
```
[ React Frontend ] <---> [ FastAPI Backend ] <---> [ PostgreSQL DB ]
    (Vite Build)          (API + Auth)             (Persistent Data)
Docker Compose orchestrates all services.
```

---

## 🔮 Future Enhancements
- JWT authentication & OAuth
- Logging & Monitoring (ELK Stack)
- Advanced DevSecOps with SAST & DAST tools

---

## 📜 License
MIT
