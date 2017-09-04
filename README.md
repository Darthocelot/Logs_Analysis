## INTRODUCTION

This program (log_analysis.py) is designed to query within the 'news' database in order to find out important information about their visitor traffic. The program will return the 3 most popular articles of all time based on the number of views, the order of author popularity based on their views, and the dates where more than 1% of server requests returned error.

## HOW TO

In order to run this program, make sure you have downloaded the log_analysis.py file into your vagrant directory from the command line containing your VM, as well as the newsdata.sql file. In order to run this program, you must have the psycopg2 module installed and functioning from your VM.

## STEP ONE

From the command line of your bash terminal, cd to your vagrant directory (wherever that is stored on the computer). Once here, call the VM by entering the command vagrant Up. Once the VM is done updating and has loaded, enter the command vagrant ssh. Once open, navigate to your shared file directory (cd /vagrant)

## STEP TWO

Once here, run the python program. Depending on which installation of python you have available, this could be done by either command python3 log_analysis.py or python log_analysis.py

## STEP THREE (FINAL)

The resulting output is the data discussed in the introduction.

## NOTE:

This program is designed to create the views required to successfully run the queries on its own. If you desire to run the progrma more than once, you will have to remove the c.execute for creating the new view, or drop the view in psql -d news.