import json

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/member')
def member():
    with open("templates/members.json", "rt", encoding="utf8") as f:
        members_list = json.loads(f.read())
    return render_template('member.html', members_list=members_list)


@app.route('/')
def index():
    return redirect('/member')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
