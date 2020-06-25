FROM ubuntu:20.04
RUN apt-get update && apt-get -y install --no-install-recommends \ 
    python3.8 \
    python3-pip \
    python3-venv \
    python3-dev \
    libpq-dev \
    unixodbc-dev \
    g++
RUN python3 -m pip install \ 
    pyodbc \
    flask \ 
    flask_restful \
    flask_jwt_extended
COPY /accounts/requirements.txt ./app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /app/application/writer
EXPOSE 5000
CMD python3 server.py
