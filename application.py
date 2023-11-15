# app.py
import dash
from dash import html
from app import app

print(__name__)

if __name__ == '__main__':
    app.run_server(debug=True)
