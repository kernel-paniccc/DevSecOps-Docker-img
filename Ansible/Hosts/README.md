# Локальная демо-сеть

Данная сеть состоит из 3х ssh серверов, подключение к которым через ключи, сразу подгружается ключ рута и юзера.

##### Структура
- `entrypoint.sh` - скрипт, что бы протянуть ssh ключи в контейнер
- `Dockerfile` - стандартны докерфайл на основе убунту для одного сервера, ставит питон и нетворк тулзы
- `ssh_config` - конфиг для ключей, нужно добавить в `~/.ssh/config`
- `docker-compose.yml` - поднимает всю сеть


#### Быстрый старт

 Чистим known_host
``` Bash
ssh-keygen -f ~/.ssh/known_hosts -R '[127.0.0.1]:2222'                           
ssh-keygen -f ~/.ssh/known_hosts -R '[127.0.0.1]:2223'
ssh-keygen -f ~/.ssh/known_hosts -R '[127.0.0.1]:2224'
```

`sudo docker compose up -d --build --force-recreate` - поднимаеи сетку

   ``` sh
   ssh ssh1root
   ssh ssh2root
   ssh ssh3root
   ```