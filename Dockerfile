FROM python:3.9-alpine3.13
LABEL mainteiner="https://github.com/pinballtec"

ENV PYTHONUNBUFFERED 1

COPY . .

WORKDIR /api-recipe

EXPOSE 8000

RUN pip install --upgrade pip && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-

ENV PATH="/py/bin:$PATH"