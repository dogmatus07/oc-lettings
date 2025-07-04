Installation & Deployment
=========================
Local Installation
------------------
1. Clone the repository:
   .. code-block:: bash

    git clone https://github.com/dogmatus07/oc-lettings.git

    cd oc-lettings
2. Create a virtual environment:
    .. code-block:: bash

     python3 -m venv env
     source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install the required packages:
    .. code-block:: bash

     pip install -r requirements.txt
4. Apply migrations and load the fixtures:
    .. code-block:: bash

     python3 manage.py migrate
     python3 load_fixtures.py
5. Run the development server:
    .. code-block:: bash

     python3 manage.py runserver

Via Docker
----------
1. Build the Docker image:
   .. code-block:: bash

    docker build -t oc-lettings-app .
2. Run the Docker container:
    .. code-block:: bash

     docker run -it -p 8000:8000 oc-lettings-app

CI/CD with GitHub Actions
-------------------------
The GitHub Actions pipeline :
* **Tests and Coverage**: pytest --cov=. --cov-report=term-missing
* **Lint**: flake8
* **Build Docker** with Dockerfile and push to Docker Hub
* **Deploy** to Render

Environment Variables
---------------------
+----------------------+--------------------------------------------+
| Variable             |    Description                             |
+======================+============================================+
|'SECRET_KEY'          |    Django secret key                       |
+----------------------+--------------------------------------------+
|'DEBUG'               | false for production, true for development |
+----------------------+--------------------------------------------+
|'ALLOWED_HOSTS'       | 'oc-lettings-xxx.onrender.com, localhost'  |
+----------------------+--------------------------------------------+
|'SENTRY_DSN'          | Sentry Data Source Name for error tracking |
+----------------------+--------------------------------------------+
