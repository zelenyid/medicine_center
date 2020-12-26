# Pull base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

# Install dependencies
RUN pip install pipenv
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
EXPOSE 8000 80

ADD mongo-init.js /docker-entrypoint-initdb.d/

RUN cd /usr/src/app/
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "80"]
