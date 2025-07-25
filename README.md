# DevSecOps Starter Kit

## 📌 Overview
A complete **DevSecOps Starter Kit** to build secure, modern web applications with:
- **Backend:** FastAPI + PostgreSQL
- **Frontend:** React + Vite
- **Security Tools:** Bandit (Python Security Scan), Trivy (Docker Image Scan)
- **CI/CD:** GitHub Actions pipeline
- **Deployment:** Docker Compose for development and production

---

## ✅ Features
- Secure API with FastAPI
- React-based frontend using Vite for fast builds
- PostgreSQL database integration
- `.env` file for secrets management
- Health checks for backend and database
- CI/CD pipeline with security scans and image checks

---

## ⚙️ Requirements
- **Docker** & **Docker Compose**
- **Node.js & npm** (if running frontend locally)
- **Python 3.11+** (if running backend locally)

---

## 🚀 Quick Start (Windows, Mac, Linux)

### 1. Clone the repository
```bash
git clone <repo-url>
cd DevSecOps-Starter-Kit
```

### 2. Create the environment file
```bash
cp .env.example .env
```
On Windows PowerShell:
```powershell
Copy-Item .env.example .env
```
Edit `.env` to set database credentials:
```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=app
```

### 3. Start services in DEV mode
```bash
docker-compose up -d
```

### 4. Access services
- **Frontend (Dev):** [http://localhost:5173](http://localhost:5173)
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
For a specific service:
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
Access at: [http://localhost:5173](http://localhost:5173)

---

## 🏗 Production Build

### 1. Build frontend for production
```bash
cd frontend
npm install
npm run build
```
The production build will be in the `dist/` folder.

### 2. Serve the build locally (optional)
```bash
npm install -g serve
serve -s dist -l 3000
```
Access at: [http://localhost:3000](http://localhost:3000)

### 3. Run in Docker (Production mode)
Use the production Compose file:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

---

## 🔐 Security Tools
- **Bandit:** Scans Python backend for security issues
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

## 🖼 Architecture
```
[ React Frontend ] <---> [ FastAPI Backend ] <---> [ PostgreSQL DB ]
    (Vite Build)          (API + Auth)             (Persistent Data)
Docker Compose orchestrates all services.
```

---

## 🔮 Future Enhancements
- JWT authentication & OAuth integration
- Logging & Monitoring (ELK Stack)
- Advanced DevSecOps tools (SAST, DAST)

---

## 📜 License
MIT
