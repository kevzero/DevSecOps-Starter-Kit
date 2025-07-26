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
- **Docker & Docker Compose**
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

---

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
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### ✅ Post-Deployment Verification
- **Frontend (Prod):** [http://localhost:3000](http://localhost:3000)
- **Backend API:** [http://localhost:8000](http://localhost:8000)
- **Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

Check container status:
```bash
docker ps
```
Logs:
```bash
docker-compose -f docker-compose.prod.yml logs -f
```

---

## 🔍 Troubleshooting

### 1. `.env` File Missing
Create `.env` with:
```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=app
```

### 2. Port Conflicts
Stop other services or edit `docker-compose.prod.yml` to use different ports.

### 3. Healthcheck Failures
Restart services:
```bash
docker-compose up -d --force-recreate
```

### 4. Blank Frontend Page
Rebuild the frontend:
```bash
cd frontend
npm install && npm run build
```

---

## 🔐 Security Tools
- **Bandit:** `bandit -r backend`
- **Trivy:** `trivy image devsecops-backend`

---

## ⚡ CI/CD Pipeline
On every **push**, GitHub Actions will:
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

![Architecture Diagram](https://dummyimage.com/600x400/cccccc/000000&text=DevSecOps+Architecture)

---

## 📸 Screenshots
- **Frontend UI:** ![Frontend Screenshot](https://dummyimage.com/600x400/cccccc/000000&text=Frontend)
- **Swagger Docs:** ![Swagger Screenshot](https://dummyimage.com/600x400/cccccc/000000&text=Swagger+Docs)

---

## 🔮 Future Enhancements
- JWT authentication & OAuth integration
- Logging & Monitoring (ELK Stack)
- Advanced DevSecOps tools (SAST, DAST)

---

## 📜 License
MIT

---

### **About**
DevSecOps Starter Kit is a ready-to-use template to set up a secure development pipeline with FastAPI, React, Docker, and GitHub Actions. It includes security checks, vulnerability scans, and automated deployments, helping developers implement DevSecOps best practices from day one.

**Topics:**
react, docker, template, security, deployment, starter-kit, automated, vulnerability-scanners, security-tools, devsecops, ready-to-use, fastapi, ci-cd

**Resources:**
- License: MIT
- GitHub Actions Workflow: Included
