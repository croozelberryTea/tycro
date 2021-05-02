from flask import Flask, render_template
#from link_shortener import link_shortener

app = Flask(__name__)
#app.register_blueprint(link_shortener)


@app.route("/")
def homepage():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
