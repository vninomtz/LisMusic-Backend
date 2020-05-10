
# Update system packages and install basic utilities
update_box() {
  echo "Updating box software"
  sudo apt update && sudo apt upgrade -y > /dev/null 2>&1
  sudo apt install -y tree git curl wget > /dev/null 2>&1
}
# Set missing language configuration
set_language() {
  echo "Setting ´vagrant´ user language configuration"
  echo -e "\n# Set locale configuration" >> ~/.profile
  echo 'export LC_ALL=en_US.UTF-8' >> ~/.profile
  echo 'export LANG=en_US.UTF-8' >> ~/.profile
  echo "export LANGUAGE=en_US.UTF-8\n" >> ~/.profile
}
# Install Python 3
install_python() {
  echo 'Installing Python 3'
  sudo apt-get install -y python3-all \
    python3-all-dbg \
    python3-all-dev \
    python3-setuptools \
    python3-pip > /dev/null 2>&1
}
#Install PostgreSQL
install_postgresql(){
    #PostgreSQL version
    PG_VERSION=11.1
    echo 'Installing PostgreSQL'
    sudo apt-get -y install "postgresql-$PG_VERSION" "postgresql-contrib-$PG_VERSION"
    PG_CONF="/etc/postgresql/$PG_VERSION/main/postgresql.conf"
    PG_HBA="/etc/postgresql/$PG_VERSION/main/pg_hba.conf"
    PG_DIR="/var/lib/postgresql/$PG_VERSION/main"
    # Edit postgresql.conf to change listen address to '*':
    sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" "$PG_CONF"
    # Append to pg_hba.conf to add password auth:
    echo "host    all             all             all                     md5" >> "$PG_HBA"

    # Explicitly set default client_encoding
    echo "client_encoding = utf8" >> "$PG_CONF"
    # Restart so that all new config is loaded:
    service postgresql restart

    echo "Successfully created PostgreSQL dev virtual machine."
}
#Install Django
install_django(){
    python3 -m pip install -y Django==3.0.6
}
# Remove unused software
clean_up() {
  sudo apt -y autoremove && sudo apt autoclean > /dev/null 2>&1
}

setup() {
    echo "Initialize the provision"
    update_box
    set_language
    install_python
    clean_up 
}

setup "$@"