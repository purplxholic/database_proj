# 50.008 Database Project Y2017 Fall

The database name is configured as `music_store` in the `/music_store/settings.py` file, so please set that as the name of your local database.

Done by [Aishwarya](https://github.com/aishwaryaprabhat) , [Vanessa](https://github.com/vanJargon), [Steven](https://github.com/kong-artist) and [Zanette](https://github.com/purplxholic)

# Instructions
Before running the server (for linux/ubuntu):
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

#you would need to be in the same directory as the repo to run the .sql files
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

# Mapping to Original Project

Point 1: found at the root page and signup/ - New user signup <br>

Point 2: found at order/ - Order information

Point 3: myrecord/\<user uid\> - User record

Point 4: inventory/ - Music inventory <br>

Point 5: inventory/ - Music inventory <br>

Point 6: music/- Info of the music, with the feedback and ratings for the music

Point 7: music/- Info of the music, with the feedback and ratings for the music

Point 8:  browse/ - Music browser

Point 9: music/- Info of the music, with the feedback and ratings for the music

Point 10: Recommender/\<user id\>/\<song id\> - Recommendations

Point 11: statistics/ - Music store statistics
--add on: will inform user if cannot return all results

# What We learnt
1. Always update your branches
The master branch is constantly being updated. To prevent overwrites, always ```git pull``` before ```git merge```. If you are not confident, do a pull request and have someone merging.

2. Django runs on apps concept
Whenever we created a new app folder, we must remember to install it to settings.py. It's like a phone with different applications. For external libraries used, they had to be "installed" into the settings.py to import it, such as ```django-widget-tweaks```

3. Be consistent on MySql syntax
Ran into trouble when some of us did SELECT * FROM **artist** instead of SELECT * FROM **Artist**. It worked on one laptop but did not for the other. Might as well use the actual name

4. Pycharm is amazing for generating values
> Fast game

5. When you update the schema, always inform group mates
So that we would know to update our local schemas

6. Django's tutorials does not cover everything
It is better to look around their documentation. For example, their form views are not explicitly covered in their tutorials.

7. Different ways to render
```HttpResponse``` : most basic, renders input as paragraph
```HttpResponseRedirect``` : redirects to targetted url
```redner()``` : takes in an input for the Django template in {} form and redirects to specified .html file 
