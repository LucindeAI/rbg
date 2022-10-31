import os
import secrets
import string
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from werkzeug.utils import secure_filename
from rembg import remove

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

special_chars = "_!/?"
length = 10

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            folder = "uploads/"

            input_image = filename

            # generate a random name for result image
            chars = string.ascii_letters + string.digits
            while True:
                output_image = ''.join(secrets.choice(chars)
                                       for i in range(10)) + '.png'
                if (any(c.islower() for c in output_image)
                        and any(c.isupper() for c in output_image)
                        and sum(c.isdigit() for c in output_image) >= 3):
                    break

            input_path = folder + input_image
            output_path = folder + output_image

            with open(input_path, "rb") as i:
                with open(output_path, "wb") as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)
                    o.close()
            return redirect(
                url_for("uploaded_file", filename=secure_filename(output_image))
            )

    return render_template("index.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
