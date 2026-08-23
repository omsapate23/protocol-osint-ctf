FROM ctfd/ctfd:3.7.0

USER root

# Install PostgreSQL driver into CTFd's python virtual environment
RUN /opt/venv/bin/pip install --no-cache-dir psycopg2-binary

# Ensure permissions are intact
RUN mkdir -p /var/log/CTFd /var/uploads && \
    chown -R 1001:1001 /var/log/CTFd /var/uploads /opt/CTFd

USER 1001

EXPOSE 8000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8000} -w 2 -k gevent 'CTFd:create_app()'"]