import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)

# Configure the secret key
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Configure the database URI based on environment
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes
from taskmanager import routes  # noqa
