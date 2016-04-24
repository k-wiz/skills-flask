from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    #return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def application_form():
    """Shows job application form page."""

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application_response():
    """Shows confirmation of submitted application."""

    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    salary = request.form["salary"]
    title = request.form["title"]


    return render_template("application-response.html",
                            firstname=firstname,
                            lastname=lastname,
                            salary=salary,
                            title=title)

    print firstname
    print lastname


if __name__ == "__main__":
    app.run(debug=True)
