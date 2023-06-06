FROM python:3.11-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FIRST_RUN=True
ENTRYPOINT ["python"]
CMD ["app.py"]