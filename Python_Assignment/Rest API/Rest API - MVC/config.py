from app import database_app

DEBUG = True


database_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
database_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False