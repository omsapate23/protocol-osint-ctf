FROM ctfd/ctfd:3.7.0

USER root

# Install psycopg2 binary
RUN /opt/venv/bin/pip install --no-cache-dir psycopg2-binary

# Ensure permissions
RUN mkdir -p /var/log/CTFd /var/uploads && \
    chown -R 1001:1001 /var/log/CTFd /var/uploads /opt/CTFd

USER 1001

EXPOSE 8000

ENTRYPOINT ["/opt/CTFd/docker-entrypoint.sh"]