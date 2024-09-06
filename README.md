# code-example

### Running the Flask application (Terminal)

1. Ensure you have Python installed on your system

   `python --version` e.g. Python 3.12.5

2. Change the working directory to api

   `cd api`

3. Create environment file

   `cp .env.example .env`

4. Update environment variables

   `nano .env`

5. Create a virtual environment

   `python -m venv venv`

6. Activate the virtual environment

   `source venv/bin/activate`

7. Install requirements within virtual environment

   `pip install -r requirements.txt`

8. Create database instance and run database migrations

   `flask db migrate`

   `flask db upgrade`

9. Start the Flask Application

   `python app.py`

10. Open Flask application within browser

    Visit [http://127.0.0.1:5000](http://127.0.0.1:5000/) within your browser

To stop the Flask application, press Ctrl + C in the terminal where it's running.

### Running the React application (Terminal)

1. Ensure you have Node.js installed on your system

   `node --version` e.g. v22.7.0

2. Ensure you have npm installed on your system

   `npm --version` e.g. 10.8.3

3. Change the working directory to app

   `cd app`

4. Create environment file

   `cp .env.example .env`

5. Update environment variables

   `nano .env`

6. Start the React Application

   `npm start`

7. Open React application within browser

   Visit [http://127.0.0.1:3000](http://127.0.0.1:3000/) within your browser

To stop the React application, press Ctrl + C in the terminal where it's running.

### Testing the Flask application

Follow steps 1 to 8 from within "Running the Flask application (Terminal)" section, then run `pytest`.
