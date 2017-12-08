# database_proj 

The database name is configured as `music_store` in the `/music_store/settings.py` file, so please set that as the name of your local database.

Before running the server (for ubuntu):
```
# install mysql
sudo apt-get update
sudo apt-get install mysql-server
mysql_secure_installation

# give PRIVILEGES to guest user on command line
mysql -u root -p
CREATE USER 'guest'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'guest'@'localhost';
FLUSH PRIVILEGES;

#create database
CREATE DATABASE music_store

#install python and django
sudo apt-get install python
pip install Django

#quit and run
python manage.py runserver

```

# Paths

browse/ - Browser
music/<music sid> - Info of the music, with the feedback and ratings for the music 