import os
import json

from flask import Flask, render_template, request, Response

# from link_shortener import link_shortener

app = Flask(__name__)
# app.register_blueprint(link_shortener)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("home.html")


@app.route("/", methods=["POST"])
def handle_contact():
    email = request.form["email"]
    subject = request.form["subject"]
    body = request.form["body"]
    print(email)
    print(subject)
    print(body)
    return render_template('home.html', form=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
