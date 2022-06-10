from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from models.models import *
from models.parse_expr import ParseExpr

app = Flask(__name__, static_url_path="")
Bootstrap(app)

db.bind(provider='sqlite', filename='meds.db', create_db=True)
db.generate_mapping(create_tables=True)


lista_meds_sel = []

def get_meds_names():
    with db_session:
        lst_names = select(med.nome for med in Medicamento)
        return lst_names.fetch()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', lista_meds=get_meds_names())

@app.route('/add_med', methods=['POST'])
def add_med():
    cur_med = None
    med_name = request.form['med_name']
    if med_name:
        with db_session:
            cur_med = Medicamento.get(nome=med_name)
    return cur_med.to_dict()



if __name__ == '__main__':
    app.run(debug=True)
