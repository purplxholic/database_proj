# database_proj 

The database name is configured as `music_store` in the `/music_store/settings.py` file, so please set that as the name of your local database.

Before running the server (for ubuntu):
```
# install mysql
sudo apt-get update
sudo apt-get install mysql-server
mysql_secure_installation

# cd into directory
cd database_proj

# give PRIVILEGES to guest user on command line
mysql -u root -p
CREATE USER 'guest'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'guest'@'localhost';
FLUSH PRIVILEGES;

#create database
CREATE DATABASE music_store

#create tables
source schema.sql

#populate with dummy data
source insert_into_schema.sql
source Recommender_cases.sql

#quit mysql shell
exit

#install python and django
sudo apt-get install python
pip install Django
pip install django-widget-tweaks

#run
python manage.py runserver

```

# Paths 

browse/ - Music browser <br>
inventory/ - Music inventory <br>
music/\<music sid\> - Info of the music, with the feedback and ratings for the music <br>
myrecord/\<user uid\> - User record <br>
order/ - Order information <br>
signup/ - New user signup <br>
statistics/ - Music store statistics <br>
Recommender/\<user id\>/\<song id\> - Recommendations 
