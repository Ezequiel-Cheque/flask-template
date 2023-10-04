from flask import Flask
from src.app import init_app

app = init_app()

if __name__ == "__main__":
    
    app.run("0.0.0.0", port=3000)