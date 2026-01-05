FROM nginx:alpine

RUN rm /usr/share/nginx/html/* \
    && mkdir -p /var/cache/nginx/app_cache /etc/nginx/certs /var/log/nginx \
    && touch /var/run/nginx.pid \
    && chown -R nginx:nginx /usr/share/nginx/html /var/cache/nginx /var/log/nginx /var/run/nginx.pid

COPY index.html /usr/share/nginx/html/

# Unprivileged run: listen on 8080 and drop root
EXPOSE 8080 8443

# Copy a default config (can be overridden by bind mount)
COPY nginx.conf /etc/nginx/nginx.conf

USER nginx

CMD ["nginx", "-g", "daemon off;"]
