from flask import render_template

import config


connex_app = config.connex_app

# Feed the endpoints from the swagger.yml file
connex_app.add_api("swagger.yml")


@connex_app.route("/")
def home():
    """
    This function just responds to the root URL

    :return:        the rendered template "root.html"
    """
    return render_template("root.html")


if __name__ == "__main__":
    connex_app.run(debug=True)
