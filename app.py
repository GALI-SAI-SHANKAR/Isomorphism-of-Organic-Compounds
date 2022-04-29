from flask import *
from Isomorphism import *
from ChemSmiles import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def isomorphic():
    if request.method == "POST":
        mol1 = request.form["cname1"]
        mol2 = request.form["cname2"]

        adj_matrix_c1, adj_matrix_c2 = adj_matrix(mol1, mol2)
        if GraphMatcher(adj_matrix_c1, adj_matrix_c2):
            res = 'Isomorphic'
            return render_template("result.html", result=res)
        else:
            res = 'Not Isomorphic'
            return render_template("result.html", result=res)


@app.route('/result')
def output():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
