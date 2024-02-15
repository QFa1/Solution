from flask import Flask, render_template, url_for
from data import db_session
from data.jobs import Jobs
from data.users import User
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    a = db_sess.query(Jobs)
    return render_template("index.html", news=a, style=url_for('static', filename='css/style.css'))


if __name__ == '__main__':
    main()
