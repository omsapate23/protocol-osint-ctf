FROM ctfd/ctfd:3.7.0
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "2", "-k", "gevent", "CTFd:create_app()"]