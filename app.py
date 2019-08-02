from flask import Flask, render_template, request

app = Flask(__name__)

"""
書くこと
    /index で GETリクエストが来たら
    index.html というテンプレートをレンダリングする
"""


@app.route("/index")
def index():
    if request.method == "GET":
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
