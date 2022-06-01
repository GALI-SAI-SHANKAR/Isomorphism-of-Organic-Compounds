from rdkit import Chem
from rdkit.Chem import Draw
from urllib.request import urlopen
from urllib.parse import quote
from pysmiles import read_smiles
import networkx as nx


def CIR_convert(ids):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles'
        ans = urlopen(url).read().decode('utf8')
        return ans
    except:
        return 'Did not work'


def adj_matrix(c_name1, c_name2):
    s_formula1 = CIR_convert(c_name1)
    s_formula2 = CIR_convert(c_name2)

    Draw.MolToFile(Chem.MolFromSmiles(s_formula1), './static/mol_img_1.png')
    Draw.MolToFile(Chem.MolFromSmiles(s_formula2), './static/mol_img_2.png')

    mol_1 = read_smiles(s_formula1)
    mol_2 = read_smiles(s_formula2)

    # adjacency matrix
    adj_matrix_c1 = nx.to_numpy_matrix(mol_1)
    adj_matrix_c2 = nx.to_numpy_matrix(mol_2)

    return adj_matrix_c1, adj_matrix_c2
