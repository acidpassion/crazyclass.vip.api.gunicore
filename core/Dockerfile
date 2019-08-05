FROM python:3.7.2-alpine3.9

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV PORT=5000

EXPOSE 5000

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "server.py --threaded" ]
