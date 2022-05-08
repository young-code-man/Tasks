from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/table/<sex>/<int:age>')
def table_param(sex, age):
    return render_template('table.html', sex=sex, age=age)


@app.route('/')
def index():
    return redirect('/table/female/12')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
