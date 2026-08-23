FROM ctfd/ctfd:3.7.0

USER root

# Expose Hugging Face default port
EXPOSE 7860

# Ensure data directory permissions
RUN mkdir -p /var/log/CTFd /var/uploads && \
    chown -R 1001:1001 /var/log/CTFd /var/uploads /opt/CTFd

USER 1001

# Run Gunicorn binding explicitly to 0.0.0.0:7860
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "-w", "4", "-k", "gevent", "CTFd:create_app()"]