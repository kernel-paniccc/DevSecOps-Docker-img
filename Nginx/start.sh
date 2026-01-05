#!/bin/bash
set -euo pipefail

image_name="my-nginx"
config_file="${1:-nginx.conf}"
script_dir="$(cd "$(dirname "$0")" && pwd)"
config_path="${script_dir}/${config_file}"
cert_dir="${script_dir}/certs"
cert_mount=()

if [[ ! -f "${config_path}" ]]; then
  echo "Config ${config_file} not found in $(dirname "${config_path}")" >&2
  exit 1
fi

if [[ -d "${cert_dir}" ]]; then
  cert_mount=(-v "${cert_dir}:/etc/nginx/certs:ro")
fi

docker build -t "${image_name}" .
docker rm -f "${image_name}" 2>/dev/null || true
docker run -d --name "${image_name}" -p 8080:8080 -p 8443:8443 \
  -v "${config_path}:/etc/nginx/nginx.conf:ro" \
  "${cert_mount[@]}" \
  "${image_name}"
