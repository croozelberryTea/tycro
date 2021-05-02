FROM python:3.9-slim-buster

ENV FLASK_APP=tycro FLASK_ENV=development

COPY . .

RUN pip3 install -e .

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]