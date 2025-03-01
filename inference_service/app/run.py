""""
Flask Application Entry Point

This module serves as the main entry point for the Flask application. 

Usage:
    The flask application is created and initialized here.
    The prediciton blueprint('api.prediction.bp') is registered with the application. 
"""

from flask import Flask
from api.prediction import bp

app=Flask(__name__)
app.register_blueprint(bp)

if __name__=='__main__':
    app.run(debug=True)