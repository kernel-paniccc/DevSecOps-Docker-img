docker build -t my-ssh-server .

docker run -d -p 2222:22 --name ssh-container my-ssh-server
# ssh root@localhost -p 2222
