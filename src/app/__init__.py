from flask import Flask, jsonify
from .controller.index import index
from flask_swagger_ui import get_swaggerui_blueprint
import json


def init_app():
    """
    Application factory pattern
    """
    
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["TESTING"] = False

    # Configure Swagger UI
    SWAGGER_URL = "/swagger"
    API_URL = "http://localhost:3000/swagger.json"
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            "app_name": "Sample API"
        }
    )
    
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    @app.route("/swagger.json")
    def swagger():
        with open("swagger.json", "r") as f:
            return jsonify(json.load(f))
    
    app.register_blueprint(index)
    
    return app