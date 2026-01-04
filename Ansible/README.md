# Ansible плейбуки

Сборник плейбуков для демо‑инфры из каталога `Hosts`.

#### Содержимое
- `inventory` — инвентори с хостами.
- `metrics_playbook.yaml` — снимает метрики с хостов и пишет снапшоты на контроллер в `logs/<inventory_hostname>/`.
- `directory_playbook.yaml` — создаёт демо‑каталоги на хостах.
- `Jinga2-demo/demo.j2` — пример Jinja2 шаблона.
- `ansible.ctg` - пайплайны.
- `Docker_role` - пример роли Ansible для раскатки Docker

#### Быстрый старт
```bash
# В каталоге DevSecOps-Docker-img/Ansible
ansible-inventory -i inventory --list          # проверить инвентори
ansible-playbook -i inventory metrics_playbook.yaml
```

Логи метрик сохраняются в `Ansible/logs/<host>/metrics_<timestamp>.txt` на контроллере.


