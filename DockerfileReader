FROM ubuntu:20.04
RUN apt-get upgrade -y
RUN apt-get update && apt-get -y install --no-install-recommends \ 
    gnupg2 \
    curl \
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

RUN curl https://packages.microsoft.com/config/ubuntu/19.10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB3E94ADBE1229CF
RUN apt-get update && ACCEPT_EULA=Y apt-get -y install --no-install-recommends \  
    msodbcsql17 \
    mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile

COPY /accounts/requirements.txt ./app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /app/application/read
EXPOSE 6000
CMD python3 server.py
