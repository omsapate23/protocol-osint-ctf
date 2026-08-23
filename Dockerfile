FROM ctfd/ctfd:3.7.0

USER root

# Install PostgreSQL driver
RUN /opt/venv/bin/pip install --no-cache-dir psycopg2-binary

# Set permissions
RUN mkdir -p /var/log/CTFd /var/uploads && \
    chown -R 1001:1001 /var/log/CTFd /var/uploads /opt/CTFd

USER 1001

EXPOSE 8000

# Completely wipe the inherited entrypoint script so ping.py never runs
ENTRYPOINT []

# Direct command to run migrations and start Gunicorn on 0.0.0.0:8000
CMD ["sh", "-c", "python manage.py db upgrade && gunicorn --bind 0.0.0.0:8000 -w 2 -k gevent 'CTFd:create_app()'"]