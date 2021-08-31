# **in local**

> mkdir flaskapp && cd flaskapp

> python -m venv venv

> git clone https://github.com/rasimogluali/flask-todo-app.git

To activate virtual environment 
> **in linux:** source venv/bin/activate
> **in windows:** venv\Scripts\activate

> pip install -r requirements.txt 

> python main.py 

> to see swagger api documentation send request to **/swagger/**
> to run unit tests locate to the project root directory and just type **pytest**

# **with docker**

after doing steps above 
> docker-compose build && docker-compose up


**NOTE:** 
>Actually, I have finished task 2 days ago. Everything is ok but I have been dealing with Docker for the last 2 days. I've been trying to solve problems in Docker for the last 2 days. Project and Database containers stand up and run separately well. However, it seems that the project and the database cannot see each other. There is no solution I haven't tried in the last 2 days. If I had a little more time I would have figured it out this issue. Frankly, I had to send it so that the project would not be too late. You can query the /todos/dockertest endpoint to check that the project is up and running in Docker.


# YOU CAN SEE DEMO EXAMPLE PHOTOS BELOW


## SWAGGER API DOCUMENTATION



## UNIT TESTS RESULT


## ENDPOINT TESTS