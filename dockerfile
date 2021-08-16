FROM python:latest
RUN pip install flask psycopg2 yaml2
COPY . .
RUN cat db_credentials.yaml
ENTRYPOINT [ "python", "show_result.py"]