# my_apps_demo

Projeto de demonstração mostrando como usar os workflows de [my_workflows](https://github.com/D2nke/my_workflows) em diferentes stacks de aplicação.

---

## Branches

Cada branch contém uma stack diferente usando os mesmos workflows reutilizáveis:

| Branch | Stack | Descrição |
|--------|-------|-----------|
| `main` | Java (Maven) | App Spring Boot com testes JUnit |
| `python` | Python | App Flask com pytest e coverage |
| `node` | Node.js | App Express com Jest |

---

## Pipeline (todas as branches)

Todas as branches passam pelas mesmas etapas, definidas em `my_workflows`:

```
Test → Security Scan (SonarQube + Mend) → Build Docker Image → Deploy
```

A única diferença entre branches é o bloco `with:` na chamada do workflow — a estrutura do pipeline é idêntica.

---

## Rodando localmente

```bash
# Java (main branch)
mvn test
docker build -t my-app-demo .
docker run -p 8080:8080 my-app-demo

# Python (branch python)
pip install -r requirements.txt
pytest tests/ --cov=. --cov-report=term-missing

# Node (branch node)
npm install
npm test
```

---

## Reproduzindo o setup

1. Faça fork deste repo
2. Faça fork de [my_workflows](https://github.com/D2nke/my_workflows)
3. Configure os secrets: `SONAR_TOKEN`, `MEND_API_KEY`, `SSH_PRIVATE_KEY`
4. Configure as variables: `SONAR_HOST_URL`, `DEV_SERVER`
5. Faça um push em qualquer branch e veja o pipeline rodar

---

## Por que workflows reutilizáveis?

Copiar arquivos de pipeline por repositório significa:
- Gates de segurança podem ser removidos ou contornados
- Atualizações precisam ser aplicadas um repositório por vez
- Onboarding de novos times leva dias

Com workflows reutilizáveis, a atualização acontece uma vez no `my_workflows` e todos os projetos recebem automaticamente.
