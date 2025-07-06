from flask import Flask
myapp = Flask(__name__)
@myapp.route("/info")
def lwinfo():
    return "This is lw"
@myapp.route("/mail")
def lwmail():
    return "this is mail"
@myapp.route("/me")
def name():
    x = request.args.get("x")
    return f"I am {x}"
myapp.run()
