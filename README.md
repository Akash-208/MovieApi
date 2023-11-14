TITLE : MovieApi (RESTFULL)

##OVERVIEW:
MovieApi is a RESTful web API built using Django and Django Rest Framework, with PostgreSQL as the
database. This API allows users to perform various operations related to movies, such as creating,
updating, deleting, and retrieving movie information. 

## Features
- **CRUD Operations:** Perform Create, Read, Update, and Delete operations on movie data.
- **Used django's default router for managin the routes.
- **Search and Ordering:** Easily search and filter movies based on different criteria.
- **Pagination:** Manage large datasets efficiently with built-in pagination.

## Technologies Used
- **Django:** A high-level web framework for building web applications in Python.
- **Django Rest Framework (DRF):** A powerful and flexible toolkit for building Web APIs on top
  of Django.
- **PostgreSQL:** An open-source relational database management system.

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/MovieApi.git
    ```

2. Navigate to the project directory:

    ```bash
    cd MovieApi
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Configure the database settings in `MovieApi/settings.py`. Update the `DATABASES` section with
    your PostgreSQL configuration.

8. Make migrations and then Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

9. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Usage
-  **After starting the development server click on the development server link and then a
   browsable api interface will open and the click on:
   GET : ``` http://127.0.0.1:8000/api/ ``` 
   
-  **After this a list of movie with details will appear with page number and also a have a
   section for making the POST request.

-  **For retrieving,updating and destroying the data according to their id.
      ``` http://127.0.0.1:8000/api/<id>/ ```

-  **For searching the movie according to actor, geners, and name.
      ``` http://127.0.0.1:8000/api/?search=<actor_name> ```
      ``` http://127.0.0.1:8000/api/?search=<geners> ```
      ``` http://127.0.0.1:8000/api/?search=<movie_name> ```
