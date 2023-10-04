from flask import Blueprint

index = Blueprint("index", __name__, url_prefix="/index")

@index.route("/", methods=["GET"])
def home():
    return "Hello world"