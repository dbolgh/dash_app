# application.py
from app import app

print(app)

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050)
