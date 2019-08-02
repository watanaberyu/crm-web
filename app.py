from flask import Flask, render_template

app = Flask(__name__)

"""
書くこと
    /index で GETリクエストが来たら
    index.html というテンプレートをレンダリングする
"""


@app.route("/index")
def index():
    customers = [["Bob", 15],
                 ["Tom", 57],
                 ["Ken", 73]]

    return render_template("index.html", customers=customers)


if __name__ == "__main__":
    app.run(debug=True)
