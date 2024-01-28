from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

html_template = "..."  # Your updated HTML template as a string


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file.save(os.path.join(".", file.filename))
    data = {
        "Title": "Sales Analysis Report",
        "Number of rows": 200,
        "Number of columns": 10,
        "Sales Over time": "./static/sales_over_time.png",
        "Sales Stats": "Mean: 50, Variance: 10, STD: 25",
        "Sales by Country": "./static/sales_by_country.png",
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
