start:
	docker-compose up --build

stop:
	docker-compose down

rebuild:
	docker-compose down && docker-compose up --build

scan-security:
	bandit -r backend/
	trivy fs .
