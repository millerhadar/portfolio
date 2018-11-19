from django.db import models

# Create Database in Postgresql
# Open the postgresql
# Doublclick on database ( like postres, opens a terminal )
# /du  shows the users on the server for this database
# To set a password for a db user
# /password [username]   like /password postgres
# CREATE DATABASE [dbname];
# python manage.py createsuperuser
# now we can connect our application to the database


# Crete New class
# add AppName app to the settings , if it is new app
# add new model to admin.py
# create a migration
# migrate
# add to admin

class Blog(models.Model):
    title = models.CharField(max_length=50)
    publ_date = models.DateField()
    body = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    def summary(self):
        return self.body[:50]
    def my_pub_date(self):
        return self.publ_date.strftime("%b %e %Y")

