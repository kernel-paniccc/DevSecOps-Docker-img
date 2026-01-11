🧪 Демо для CI

прогон pytest/flake8 и сборка Docker-образа

#### Содержимое
- `testApp/app.py` — три эндпойнта: `/` (приветствие), `/health` (статус), `/echo?msg=` (эхо).
- `testApp/test_app.py` — pytest-покрытие всех эндпойнтов.
- `testApp/requirements.txt` — зависимости (Flask, pytest, flake8, gunicorn).
- `testApp/Dockerfile` — образ на `python:3.12-slim`, запуск через gunicorn на 8080.

#### Тесты и линт
```bash
cd DevSecOps-Docker-img/CI/testApp
pytest
flake8 app.py test_app.py
```

#### Docker
```bash
cd DevSecOps-Docker-img/CI/testApp
docker build -t ci-test-app .
docker run --rm -p 8080:8080 ci-test-app
curl 'http://localhost:8080/echo?msg=hi'
```

#### CI воркфлоу
- `.github/workflows/Lint-Test-SAST.yml` — три джоба: flake8, pytest на Python 3.10/3.12/3.13, Semgrep с `--config auto`
- `.github/workflows/docker.yml` — сборка Docker-образа из `CI/testApp/Dockerfile` через `docker/build-push-action`
