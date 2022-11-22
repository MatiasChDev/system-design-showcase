FROM openstax/python3-poetry AS builder

WORKDIR /app
COPY . .
RUN poetry export -o requirements.txt

FROM python:3.9.15 AS installer

WORKDIR /app
COPY --from=builder /app /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "entrypoint.sh"]