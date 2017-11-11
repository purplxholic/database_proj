# database_proj

The database name is configured as `music_store` in the `/music_store/settings.py` file, so please set that as the name of your local database.

Before running the server (for ubuntu):
```
# install mysql
sudo apt-get update
sudo apt-get install mysql-server
mysql_secure_installation

# give priveledge to guest user on command line
mysql -u root -p
CREATE USER 'guest'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
FLUSH PRIVILEGES;

#create database
CREATE DATABASE music_store

#quit and run
python manage.py runserver

```
