# Python branch

Demo app showing how to use [my_workflows](https://github.com/D2nke/my_workflows) reusable workflows in a Python (Flask) stack.

---

## Pipeline

```
Test (pytest + coverage) → Security Scan (SonarQube + Mend) → Build Docker Image → Deploy to DEV
```

All steps are defined in `my_workflows` — this repo only provides the `with:` parameters.

---

## Running locally

```bash
pip install -r requirements.txt
pytest tests/ --cov=. --cov-report=term-missing
python app.py
```

App runs at `http://localhost:8080`.

---

## Branches

| Branch | Stack |
|--------|-------|
| [master](https://github.com/D2nke/my_apps_demo/tree/master) | Java (Spring Boot + Maven) |
| [python](https://github.com/D2nke/my_apps_demo/tree/python) | Python (Flask + pytest) |
| [node](https://github.com/D2nke/my_apps_demo/tree/node) | Node.js (Express + Jest) |
