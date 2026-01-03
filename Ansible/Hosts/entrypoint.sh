#!/bin/bash
set -e

PUBKEY=/tmp/ansible_key.pub

configure_user() {
  local user=$1
  local home_dir=$2
  mkdir -p "${home_dir}/.ssh"
  if [ -f "${PUBKEY}" ]; then
    cat "${PUBKEY}" > "${home_dir}/.ssh/authorized_keys"
  fi
  chmod 700 "${home_dir}/.ssh"
  chmod 600 "${home_dir}/.ssh/authorized_keys"
  chown -R "${user}:${user}" "${home_dir}/.ssh" 2>/dev/null || true
}


configure_user ansible /home/ansible
configure_user root /root


SSHD_CFG="/etc/ssh/sshd_config"
sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' "${SSHD_CFG}"
sed -i 's/^#\?ChallengeResponseAuthentication.*/ChallengeResponseAuthentication no/' "${SSHD_CFG}"
sed -i 's/^#\?UsePAM.*/UsePAM yes/' "${SSHD_CFG}"
if grep -q '^PermitRootLogin' "${SSHD_CFG}"; then
  sed -i 's/^PermitRootLogin.*/PermitRootLogin yes/' "${SSHD_CFG}"
else
  echo "PermitRootLogin yes" >> "${SSHD_CFG}"
fi
if ! grep -q '^PubkeyAuthentication' "${SSHD_CFG}"; then
  echo "PubkeyAuthentication yes" >> "${SSHD_CFG}"
fi

exec "$@"
