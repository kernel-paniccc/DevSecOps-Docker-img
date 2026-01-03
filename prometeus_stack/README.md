# Prometheus + Grafana

Локальная система мониторинга для сбора метрик (Prometheus + Grafana) и node_exporter.

## Что внутри
- `prometeus-grafana/docker-compose.yaml` — Prometheus (9090) + Grafana (3000), общий external-сетевой сегмент `monitoring`.
- `prometeus-grafana/prometheus.yml` — базовая конфигурация, Prometheus и `node-exporter:9100`.
- `node_exporter/docker-compose.yaml` — node_exporter (9100) на той же сети `monitoring`.

## Подготовка
Создайте общую сеть:
```bash
docker network create monitoring
```

## Запуск
node_exporter:
```bash
cd node_exporter
docker compose up -d
```
поднять Prometheus + Grafana:
```bash
cd prometeus-grafana
docker compose up -d
```

## Доступ
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (дефолт admin/admin)
- node_exporter: http://localhost:9100/metrics (скрейпается как `node-exporter:9100` внутри сети `monitoring`)


---

- Данные Prometheus хранятся во volume `prometheus_data`.
- `1860` - Id Full Node_exporter dashboard
