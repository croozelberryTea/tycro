from flask import Blueprint, redirect, url_for, abort, render_template
from repository.link_repository import LinkRepository

link_shortener = Blueprint("link_shortener", __name__, template_folder="templates")

db = LinkRepository()


@link_shortener.route("/l/", methods=["GET"])
def link_page():
    return render_template("linkshort.html")


@link_shortener.route("/l/", methods=["POST"])
def create_link():
    return abort(404)


@link_shortener.route("/l/<slug>")
def get_link(slug):
    link = fetch_link(slug)

    if link is not "":
        return redirect(link)
    return render_template("linknotfound.html")


def fetch_link(slug):
    return db.get_link(slug)
