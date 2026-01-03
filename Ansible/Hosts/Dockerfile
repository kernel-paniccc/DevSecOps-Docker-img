FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       openssh-server sudo ca-certificates \
       iproute2 net-tools iputils-ping traceroute curl \
       python3 python3-venv python3-pip \
    && rm -rf /var/lib/apt/lists/*


RUN useradd -m -s /bin/bash ansible \
    && usermod -aG sudo ansible \
    && mkdir -p /var/run/sshd


COPY keys/id_ed25519_ansible.pub /tmp/ansible_key.pub


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh \
    && ssh-keygen -A

EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/sbin/sshd","-D","-e"]
