FROM python:3.8.0rc1-alpine

LABEL MAINTAINER="bala@nus.edu.sg"

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "-f", "http://localhost/time", "||" ,"exit", "1" ]

WORKDIR /app

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD . .

ENV PORT=5000

ENTRYPOINT [ "python", "app.py" ]