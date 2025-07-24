from flask import Flask, send_from_directory, render_template
from pathlib import Path

app = Flask(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
# # point to the folder that holds index.html
FRONT_FILES = REPO_ROOT


@app.route("/<path:path>")
def static_proxy(path):
    """
    Anything that’s not /api/* is treated as a static asset request
    (style.css, images/xxx.png, script.js, …)
    """
    return send_from_directory(FRONT_FILES, path)


app = Flask(__name__,
            # let Flask find *.css / images automatically
            static_folder=str(FRONT_FILES),
            static_url_path="")


@app.route("/")
def index():
    # Your HTML with the button
    return send_from_directory(FRONT_FILES, "index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
