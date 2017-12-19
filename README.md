# 50.008 Database Project Y2017 Fall

The database name is configured as `music_store` in the `/music_store/settings.py` file, so please set that as the name of your local database.

Done by [Aishwarya 1001848](https://github.com/aishwaryaprabhat) , [Vanessa 1001827](https://github.com/vanJargon), [Steven 1003223](https://github.com/kong-artist) and [Zanette 1001845](https://github.com/purplxholic)

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

* add on: will inform user if cannot return all results

## Extras that we wanted to do but couldn't
1. Create a playlist (although this is possible to built from ```Purchases``` Table)
2. Loading real songs (copyright issues of course!)

# GUI

GUI is simple, clear and self-explanatory. Used Bootstrap with django-widget-tweaks for forms

# Git

We all use Git-tracking system - either through Git on Terminal or Github Desktop. Each of us have our own branches where we commited to first before merging.

# What We learnt
1. Always update your branches

The master branch is constantly being updated. To prevent overwrites, always ```git pull``` before ```git merge```. If you are not confident, do a pull request and have someone merging.

Branch everthing because you would not want to accidentally overwrite your teammate's code halfway! Esp during early stages to get a controlled environemnt as you code.

We also learnt to always git push. 2 of us are using VM to do Djano and this project and both of our VMs crashed and got into trouble. Our pushed codes became our latest version of the code when we got back our VMs.

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

```HttpResponse(stuff)``` : most basic, renders input as paragraph

```HttpResponseRedirect(url)``` : redirects to targetted url

```renders(request,html file,input)``` : input used in the Django template inside ```{}``` and redirects to specified .html file

8. Template syntax

```{% %}``` -> you are doing some function or importing something to the template

* it is worth noting that Django's template is limited in ways of access lists

You can't access using index
```
#not allowed
{% for r in list[1] %}

#allowed
{% for r in list.1 %}
```
Indexes **must be** hardcoded. Hence, you would need to find ways to go around it, like restructuring your lists or writing customer filters. [An example filter](https://djangosnippets.org/snippets/2740/)

```{{ }}``` -> you are putting stuff from input from views.py

Funfact (well to me) : Django's template syntax reminds me of VBA x Python
