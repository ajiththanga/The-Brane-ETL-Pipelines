# set base image (host OS)
FROM python:3.7.6

WORKDIR /app
RUN  pip install requests==2.22.0
COPY graph.py .

ENTRYPOINT ["python", "graph.py"]
