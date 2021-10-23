# Dockerfile, DockerImage, Container
FROM python:3.8

ADD app.py .
ADD getcryptoprices.py .
ADD creds.py .

RUN python -m pip install requests
RUN python -m pip install Flask

EXPOSE 8000/tcp
EXPOSE 8000/udp

CMD ["python", "app.py"]

