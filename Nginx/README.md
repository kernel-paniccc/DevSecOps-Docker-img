# Nginx конфиги

Набор готовых конфигов и Dockerfile для типовых сценариев Nginx.

#### Содержимое
- `nginx.conf` — базовый статический сервер на 8080 с простыми заголовками безопасности.
- `nginx.reverse-proxy.conf` — реверс‑прокси до сервиса `app:3000` (WebSocket, `/healthz`).
- `nginx.rate-limit.conf` — лимиты запросов для `/api`, статика отдаётся без ограничений.
- `nginx.ssl.conf` — HTTPS на 8443 + редирект с 8080, ищет сертификаты в `/etc/nginx/certs/`.
- `Dockerfile` — образ `nginx:alpine` с каталогами для cache/certs; остаётся запуск от пользователя `nginx`.
- `start.sh` — сборка и запуск контейнера с выбранным конфигом.
- `index.html` — демо‑страница.

#### Быстрый старт
```bash

./start.sh                        
curl -i http://localhost:8080
```

#### Выбор других конфигов
```bash
./start.sh nginx.reverse-proxy.conf
./start.sh nginx.rate-limit.conf
./start.sh nginx.ssl.conf
```

---

- **Upstream**: во всех proxy-конфигах ожидается сервис `app:3000` в Docker-сети; поменяйте host/port в `server app:3000`.
- **TLS**: положите `certs/server.crt` и `certs/server.key` рядом с конфигами или смонтируйте каталог сертификатов (`-v $(pwd)/certs:/etc/nginx/certs:ro`); пробрасывайте порт 8443.
- **Rate limit**: лимиты заданы для `/api/` (5 rps, burst 10, до 20 соединений/IP), статика отдаётся из `index.html`.
