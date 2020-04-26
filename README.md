# Inventory Managament System
This is an inventory Managment system which can be used by small retail shops or supermarkets to manage their products and have an upto date feedback of the stock and sales made
## Functionalities
#### User should be able to:
1. See a list of all the products, their prices and stock
2. Create a new product Inventory which is added to the database
3. Edit the Product Inventory in the database
4. Delete the inventory from the database
5. Generate the profits made for each product
6. Generate pie-chart according to the stock of products
## Fuctionalities still in working progress:
1. Working on an admin authentication sysytem
2. Training the system using Machine Learning to be able to forecast future sales and appropriate stock needed
---using Jupyter Notebook  and pandas library
## Technologies Used
Python 3
Bootstrap 4
Flask 1.1.1
Flask-SQLAlchemy 2.4.1
Jinja2 2.11.1
psycopg2 2.8.4
pygal 2.4.0
SQLAlchemy 1.3.15
Postgresql database managed using pgAdmin 4
### Project Structure
The main python file is the 'main.py' file commonly reffered to as app.py by some developers.
All our pages rendered in the browser are in the 'templates' folder and styles in the 'static' folder
The 'models' folder contains the three tables run by the sqlalchemy each in a separate python file.
'requirements.txt' file which shows all the dependancies used in the project   


### Project setup
```
pip install Flask
```
### Other dependancies
These distributions will be installed automatically when installing Flask.

    Werkzeug --- implements WSGI, the standard Python interface between applications and servers.

    Jinja--- is a template language that renders the pages your application serves.

    MarkupSafe--- comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.

    ItsDangerous--- securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.

    Click--- is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.
These depencies will therefore also appear in our requirements.txt file 
You can learn more about them [here](https://flask.palletsprojects.com/en/1.1.x/installation/)




### Additional guides
Use a virtual environment to manage the dependencies for your project, both in development and in production.
Python 3 comes bundled with the venv module to create virtual environments.
Just run,
```
py -3 -m venv venv
```

