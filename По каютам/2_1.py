from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    astronauts = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
                  'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', astronauts=astronauts)


@app.route('/')
def index():
    return redirect('/distribution')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
