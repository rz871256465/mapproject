## Map Task Application

A template repository for student software development teams to use in for coursework

## How to run?

This program is developed based on the MYSQL database, not sqlite3. Users need to download mysql before cloning the application.

mysql download link:https://dev.mysql.com/downloads/

Recommended username: **_root_** Password: **_123456_**

If you do not have this username and password, you need to modify the configuration file. Modify the **_'database'_** of **_'setting.py'_** in **_'map_app_project'_** to your own account

Before running this program, you need to open cmd in administrator to start database

```
net start mysql80
```

Then open your own database (mysql or any software that supports mysql) and enter the sql statement to create the corresponding table

```
CREATE DATABASE userinfor;
```

After the database is created, you have completed the first part of running the program.

The first time you clone the program, you need to enter the program.

```
cd map_app_project
```

After that, depending on the software you are using, decide whether you need to enter the environment

```
python -m venv .venv
```

Next, data migration needs to be performed. If you encounter an error after entering the instructions. T
he corresponding module is missing and you need to download the module in the error message.

```
pip install -r requirements.txt
```

migration:

```
python manage.py migrate
```

```
python manage.py makemigrations
```

Since we use the asgi protocol to develop the chat function, we do not need to use the **_python manage.py runserver_** command to open the program.
After the data migration is completed, enter this line of code to open the program

```
daphne -p 8001  map_app_project.asgi:application
```

Again, if you encounter an error message, it is because you lack the corresponding module and you need to enter the command 'pip install \*\*'

## Your next steps

- Change the .gitignore file to suite your needs - it's currently set to ignore python related temp files, etc. Google 'gitignore <your language>' to find examples.
- Edit this file to fill in relevant empty sections below
- Change the licence as required to a more suitable one.

## Vision

The participant interface should match two participants in a room where there is a chat paneland a task panel. Each participant will be assigned a role within this room, either instructiongiver, or instruction follower. This role will determine what view of the task they have: giverwill have the solution, follower will have to try and follow giver’s instructions (and ask theirown questions) via the chat to try to achieve the solution. The task will involve a novel,instant-message version of the original MapTask dialogue corpus designed with the optionfor multiple versions of the map, which will be set according to certain conditions input bythe researcher. Participant pairs should complete three tasks within their interaction.The task panel itself should be designed to be modular, such that alternative tasks (such as thetangram task) could be substituted out in future iterations of the project if the researcherwants to design another experiment.The researcher interface will allow the researcher to inspect the map conditions which dictatethe room settings that users will be assigned to. They can also inspect the users, and viewtheir task history.The map task can either consist of a maze or a map with landmarks marked on the map. Thefollower has to draw the route on the giver’s map and the giver has to describe their route tomake this happen. Landmarks will be shapes that either have a name (circle triangle etc) orare abstract (e.g. see eth tangram corpus materials), the landmarks will vary in size colour,quantity, and overlap between giver and follower’s maps (e.g. follower may not have alllandmarks that giver has and vice versa). The researcher can set these conditions, and theinterface should allow them to generate a set of rooms with all possible combinations ofconditions. New users should then be assigned tasks with different conditions.

## Requirements

List the libraries needed to build your application

## Building the application

What steps are there to build this application?

## Testing the build

How do I test the code to ensure the build is correct?

## Running the application

What do I do to deploy and/or run this?

## Team Members

Kofi Agyenim Boateng

Tamunoibi Miebaka-Ogan

Ciwie Lin

Rui Zhu

Darryl Arun

Anbazhagan Murgasen

Liu Yang
