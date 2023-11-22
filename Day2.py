 from flask import Flask
app = Flask(__name__) # Create an instance of a Flask Application
@app.route("/") # Application Routing
def hello_world():
return "<p>Hello, World!</p>"