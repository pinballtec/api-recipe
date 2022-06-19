FROM python:3.9-alpine3.13
LABEL mainteiner="https://github.com/pinballtec"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt
COPY requirements.dev.txt /tmp/requirements.dev.txt

WORKDIR /app

EXPOSE 8000

ARG DEV=false

RUN pip install -r requirements.txt && \
     if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

COPY . /app/

RUN adduser -D django-user
RUN chown django-user:django-user -R /app/
RUN chmod +x /app/
USER django-user

ENV PATH="/py/bin:$PATH"

CMD ["run.sh"]