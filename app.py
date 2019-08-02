from flask import Flask, render_template, request, redirect, url_for

import db

app = Flask(__name__)

"""
書くこと
    /index で GETリクエストが来たら
    index.html というテンプレートをレンダリングする
"""


@app.route("/index")
def index():
    customers = db.find_all_customers()

    return render_template("index.html", customers=customers)


@app.route("/add", methods=["POST"])
def add_customer():
    """新規の顧客を追加する"""
    # フォームに入力されたデータを取得する
    name = request.form["name"]
    age = request.form["age"]

    # データをデータベースに保存する
    db.add_customer(name, age)

    # index() にリダイレクトする
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
