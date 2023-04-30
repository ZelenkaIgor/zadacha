from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<list_t>')
def list_proffe(list_t):
    paramets = dict()
    paramets['professions'] = ['Инженер', 'Строитель', 'Экономист']
    paramets['list_t'] = list_t
    return render_template('odd_even.html', **paramets)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)