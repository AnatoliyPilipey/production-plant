        Production-plant 
    In a factory it is necessary to keep a record of the products made during a Shift.
There is a Foreman (user) at the head of the Shift.
There are several Workmen on the Shift.
Each Workman has WorkCommitments.
With this information we will know:
            how much production there is,
            we can also compare shifts,
            see what we need to produce more,
            analyze the cost of production.

        Manual Build
1 In Pycharm, open the folder where the project will be stored.
2 Cloning the project.
    git clone https://github.com/AnatoliyPilipey/production-plant.git
3 Go to the folder with the project.
    cd production-plant
4 Creating a virtual environment.
    python -m venv venv
5 Activating the virtual environment.
    For Apple source env/bin/activate
    For Windows venv\Scripts\activate
6 Install the required modules from the specified list.
    pip install -r requirements.txt
7 Create an .env file and put the secret key in it.
    password = "django-insecure-jgd9@7+bs^s%cq-!zypmq7a@r0y6v3ckwk0#(+b3s3(3m*8qmw"
8 Perform database creation migrations.
    python manage.py migrate
8 Using the fixture with test data, we fill the database.
    python manage.py loaddata db.json
10 Running the server
    python manage.py runserver
11 At this point, the app runs at
    http://127.0.0.1:8000/
12 Use login and password to log in to the database.
    admin
    zaq12wsx

            Thank you for familiarizing yourself with my work.
