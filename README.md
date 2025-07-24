# 🔐 DevSecOps Starter Kit – Secure CI/CD Template for Developers

DevSecOps Starter Kit is a **ready-to-use template** to set up a **secure development pipeline** with **FastAPI**, **React**, **Docker**, and **GitHub Actions**.  
It includes **security checks, vulnerability scans, and automated deployments**, helping developers implement **DevSecOps best practices** from day one.

---

## ✅ Features
- 🛡️ **Security First**: Integrated SAST (Static Analysis) and dependency scanning
- 🔄 **CI/CD Pipeline**: GitHub Actions for linting, testing, building, and deploying
- 🐳 **Dockerized**: Complete Docker + Docker Compose environment
- 🌐 **FastAPI Backend**: Lightweight, fast, and secure API server
- ⚛️ **Optional React Frontend**: Modern UI stack with Vite
- 🔍 **OWASP Checks**: Detect common vulnerabilities automatically
- 📦 **Dependency Scans**: Using `Trivy` and `Bandit`
- ☁️ **Deployment Ready**: Pre-configured for Render or VPS

---

## 🧰 Requirements
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)
- [GitHub Account](https://github.com/) for CI/CD
- (Optional) **Render / VPS** for deployment

---

## 🛠️ Quick Start (Local Development)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/devsecops-starter-kit.git
cd devsecops-starter-kit
```

### 2️⃣ Start the environment
- **Linux / Mac**
```bash
make start
```
- **Windows PowerShell**
```bash
docker-compose up --build
```

### 3️⃣ Stop the containers
```bash
docker-compose down
```

---

## 🌐 Available Services
| Service        | URL                                  |
|---------------|--------------------------------------|
| Frontend      | http://localhost:3000 (optional)    |
| Backend (API) | http://localhost:8000               |
| Swagger Docs  | http://localhost:8000/docs          |
| PostgreSQL    | localhost:5432 (user: `user`, password: `password`, db: `app`) |

---

## 🔐 Security Integrations
- ✅ **SAST**: Bandit (Python security analysis)
- ✅ **Dependency Scanning**: Trivy + OWASP Dependency Check
- ✅ **Docker Image Scans**: Trivy in CI
- ✅ **Secrets Detection**: Detect accidental credentials in repo

---

## 🔄 GitHub Actions Workflow
- **Stage 1**: Lint & Unit Tests
- **Stage 2**: Build Docker Images
- **Stage 3**: Security Scans (Bandit + Trivy)
- **Stage 4**: Deploy (optional: Render / VPS)

**Example workflow file:** `.github/workflows/ci-cd.yml`  
(Already included in the project)

---

## 📂 Project Structure
```
devsecops-starter-kit/
├── backend/                # FastAPI backend
│   ├── main.py             # API logic
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/ (optional)    # React + Vite
│   ├── src/
│   ├── package.json
│   └── Dockerfile
│
├── .github/
│   └── workflows/ci-cd.yml # GitHub Actions pipeline
│
├── docker-compose.yml
├── Makefile
└── README.md
```

---

## 🔄 Useful Commands
| Command                  | Description                      |
|-------------------------|----------------------------------|
| `make start`           | Start all containers            |
| `docker-compose down`  | Stop all containers             |
| `make rebuild`         | Rebuild Docker images          |
| `bandit -r backend/`   | Run Python security scan       |
| `trivy fs .`           | Scan for vulnerabilities       |

---

## 🧪 Testing Security Locally
Run **Bandit**:
```bash
bandit -r backend/
```

Run **Trivy**:
```bash
trivy fs .
```

---

## 🔮 Roadmap
- ✅ Add GitHub Actions pipeline for CI/CD
- ✅ Add Trivy scans for Docker images
- ✅ Add Render deployment support
- 🔜 Add Kubernetes deployment option
- 🔜 Add advanced DAST (Dynamic Application Security Testing)

---

## ❤️ Contribute
- Fork this repo
- Create a new branch: `feature-name`
- Submit a Pull Request

---

## 📜 License
MIT License – free to use and contribute.

