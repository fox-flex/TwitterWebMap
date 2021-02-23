"""
main module, run the webpage
"""
from flask import Flask, render_template, request
# from flask import redirect
from modules.crate_map import create_map, crate_list_of_points

app = Flask(__name__)

students = {"students": []}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("screen_name")
    bearer_token = request.form.get("bearer_token")
    # from modules.hidden import bearer_token
    if not name or not bearer_token:
        return render_template("failure.html")
    create_map(name, crate_list_of_points(name, bearer_token))
    return render_template("map.html")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
