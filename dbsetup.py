# -*- coding: utf-8 -*-
# swtstore->dbsetup.py

# Create and setup databases for the first time run of the application

import sys, os

# Get the path to the base directory of the app
BASE_DIR = os.path.join(os.path.dirname(__file__))

# append the path to the WSGI env path
sys.path.insert(0, BASE_DIR)

# Import and create the app; also get the db instance from the current app
from swtstore import create_app, getDBInstance

app = create_app()

db = getDBInstance()

# Import all modules which represents a SQLAlchemy model;
# they have corresponding tables that are needed to be created
from swtstore.classes.models import Sweet, Context, Client, AuthorizedClients
from swtstore.classes.models.um import User, Group, Membership

# Create them!
db.create_all()


