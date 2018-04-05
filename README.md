
## Flask Scaffolding

This is the very basic flask boilerplate, which can be used to create microservices. This does not have any functionality apart from code organization and any of your code can be used to build over this basic skeleton. This scaffolding is mostly up to date uses python 3.6 and runs inside a docker container.

***Code Navigation***

This project consists of a main folder `src` which contains all the project files. The files outside the source folder consists of `docker-compose.yml`, `Dockerfile` and a `local.env` file which are used for running the docker containers. The `src` folder contains the entrypoint of the Flask project `app.py`, `settings` folder which contains your application settings and an `apis` folder that stores all your urls and views.

Specify the urls in `urls.py` file in the api folder as list of tuples with following format:

    (endpoint, view_func, methods, description)
example:

    ("/", views.index, ["GET"], "index page")

***Installation***

Running the scaffolding app is very easy. First [install](https://docs.docker.com/install/) docker for your operating system from the docs provided in the docker website. Also [install](https://docs.docker.com/compose/install/) docker-compose

Then run

    sudo docker-compose build
and then

    sudo docker-compose up
This will run the server at port http://localhost:8400/

The index view will be displayed in your browser.

***Tasks***

Celery (4.1.0) is being used for asynchronous services. Using Redis as a broker as well as results backend. The celery application runs by default with one single worker ready to accept tasks listed in tasks.py. If you don't want to run a task service make according changes in the docker-compose.

***Logs***

A `logs` folder is created in the root of the project i.e outside the `src` folder, which is mounted using the docker-compose volume mount. It will contain a file `flask-scaffolding.log` and will contain the project logs.

***Queries***

For any queries:
Contact: arpitgoyal.iitkgp@gmail.com

Feel free to incorporate more basic features as you will and submit pull requests. I will be more than happy to incorporate those features. It would be best to support a very basic skeleton for flask which is are not available otherwise. This project mainly helps who are looking for creating `microservices` for their application using `python`.
