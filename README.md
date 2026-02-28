# DevSecOps sandbox

Репозиторий для практики и отработки и практики на реальных DevOps && DevSecOps сценариях

## Структура
- `Ansible/` — Ansible плейбуки.
- `CI/` — пайплайны и утилиты для CI.
- `ELK/` — примеры и шаблоны для ELK стека.
- `kubernetes-advanced/` — эксперименты и шаблоны для Kubernetes.
- `Nginx/` — шаблоны для Nginx proxy.
- `prometeus_stack/` — шаблоны для monitoring стека (Grafana + Prometheus + Node-exporter).
- `Simple-Docker/` — простые Docker шаблоны.
- `Terraform/` — инфраструктурные шаблоны для Terraform.
- More in future.

## Дерево (L=2)
```
├── Ansible
│   ├── ansible.cfg
│   ├── directory_playbook.yaml
│   ├── docker_role_playbook.yaml
│   ├── Hosts
│   ├── inventory
│   ├── Jinja2-demo
│   ├── logs
│   ├── metrics_playbook.yaml
│   ├── README.md
│   └── roles
├── CI
│   ├── README.md
│   └── testApp
├── ELK
├── kubernetes-advanced
│   ├── k3s-vagrant-cluster
│   └── minikube
├── Nginx
│   ├── Dockerfile
│   ├── index.html
│   ├── nginx.conf
│   ├── nginx.rate-limit.conf
│   ├── nginx.reverse-proxy.conf
│   ├── nginx.ssl.conf
│   ├── README.md
│   └── start.sh
├── prometeus_stack
│   ├── node_exporter
│   ├── prometeus-grafana
│   └── README.md
├── README.md
├── Simple-Docker
│   ├── 1-Simple-SSH-client
│   ├── 2-Simple-Flask-API
│   └── 3-Compose Demo
└── Terraform
    ├── 1_AWS_resurses
    └── 2_lesson
```
