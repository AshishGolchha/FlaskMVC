from flask import render_template
class FrontendController:
    def index():
        return render_template("index.html",message="This is index page")