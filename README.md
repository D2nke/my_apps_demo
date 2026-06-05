# my_apps_demo

Demo project showing how to consume [my_workflows](https://github.com/D2nke/my_workflows) reusable GitHub Actions workflows across different application stacks.

---

## Why this repo exists

When I was at Bradesco, one of the main challenges during the Azure DevOps → GitHub Actions migration was consistency: each team implemented their pipeline differently, security gates were skipped or misconfigured, and every new project required manual setup from scratch.

The solution was to centralize pipeline logic into reusable workflows ([my_workflows](https://github.com/D2nke/my_workflows)) and create a reference implementation showing how to consume them — so teams had a concrete starting point, not just documentation.

This repo is that reference implementation, with one branch per stack.

---

## Branches

| Branch | Stack | Pipeline |
|--------|-------|---------|
| [java](https://github.com/D2nke/my_apps_demo/tree/java) | Java 17 · Spring Boot · Maven · JUnit · Jacoco | test → security → build → deploy |
| [python](https://github.com/D2nke/my_apps_demo/tree/python) | Python 3.11 · Flask · pytest · coverage | test → security → build → deploy |
| [node](https://github.com/D2nke/my_apps_demo/tree/node) | Node 20 · Express · Jest · supertest | test → security → build → deploy |

Each branch contains only the code and the `with:` parameters to call `my_workflows` — no pipeline logic is duplicated.

---

## How the pipeline works

```
Test → Security Scan (SonarQube + Mend) → Build Docker Image → Deploy to DEV
```

All steps are defined once in [my_workflows](https://github.com/D2nke/my_workflows). Updating a step there propagates to every branch automatically — no PRs needed across repos.

---

## Reproducing the setup

1. Fork this repo and [my_workflows](https://github.com/D2nke/my_workflows)
2. Configure secrets: `SONAR_TOKEN`, `MEND_API_KEY`, `SSH_PRIVATE_KEY`
3. Configure variables: `SONAR_HOST_URL`, `DEV_SERVER`
4. Push to any branch and watch the pipeline run
