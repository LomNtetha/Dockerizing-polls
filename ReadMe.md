# Dockerizing-polls
Dockerizing Django Polls  with PostgreSQL,  Gunicorn  and nginx.  nginx is also used to serve media and staticfiles. Entrypoint.sh verify that PostgreSQL is healthy before applying the migrations and running the Django development server

# System prerequisite
- To Run this project you need to have some basics of Django, Ubuntu and git
- Ensure that ubuntu, python, git, editor (such as VS code), docker and docker composer are installed in your system

## How to run The project Local for Development

To get started please ensure that python 3.8 or above is installed in your system


- To run the project locally first of all clone the repository 
  ```
  git clone https://github.com/LomNtetha/Dockerizing-polls.git
  ```
- go to project directory
  ```
  cd Dockerizing-polls
  ```
- Remove exisitng volumes
 ```
 docker-compose down -v
 ```
- All0w entrypoint permissions to verify that PostgreSQL is healthy before applying the migrations for Development
  ```
  chmod +x myviews/entrypoint.sh
  ```
- Build the images and run the containers
  ```
  docker-compose up -d --build
  ```
- Run the migrations
  ```
  docker-compose exec web python manage.py migrate --noinput
  ```
- Ensure the default Django tables were created
 ```
 docker-compose exec db psql --username=lumkile --dbname=myviews_dev
 ```
 List databases
  ```
  \l
  ```
  connected to database "myviews_dev" 
  ```
   \c myviews_dev
   ```
 List relations
 ```
 \dt
 ```
 then exit
 ```
 \q
 ```

-  check that the volume was created as well by running
  ```
   docker volume inspect Dockerizing-polls_postgres_data
   ```
- Create superuser
  ```
  docker-compose exec web python manage.py createsuperuser
  ```
- collect static files
 ```
  docker-compose  exec web python manage.py collectstatic --no-input --clear
  ```
- You should be able to view the page at http://localhost:8080/

- Check for errors in the logs if this doesn't work via 
  ```
  docker-compose logs -f.
  ```
## How to run The project Local for Production with nginx and gunicorn
- Bring the container down
 ```
  docker-compose -f docker-compose.prod.yml down -v
  ```
 
- Allow entrypoint permissions to verify that PostgreSQL is healthy before applying the migrations for production
 ```
 chmod +x myviews/entrypoint.prod.sh
 ```
- Build the images and run the containers
 ```
  docker-compose -f docker-compose.prod.yml up -d --build
  ```
- Run migrations
 ```
 docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
 ```
- Create superuser
 ```
 docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
 ```
- organize static and media files to be serve by nginx
 ```
 docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
 ```
- then visit: http://localhost:3000/

- if the container fails to start, check for errors in the logs via 
 ```
 docker-compose -f docker-compose.prod.yml logs -f
 ```
## Technology tools and python packages used to develop this system
- Ubuntu 22.04.1 LTS
- Docker version 20.10.18, build b40c2f6
- docker-compose version 1.29.2, build unknown
- git version 2.34.1
- python 3
- Django 4.1.1
- postgresql
- nginx web server
- gunicorn 20.1.0 for http/https server request and WSGI server
- flake8
- Entrypoint shell

 
