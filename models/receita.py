from models.models import Medicamento, db
from dominate.tags import *


class Receita:

    def __init__(self, nome, data, meds: list, template_file):
        # lista de mapas
        self.nome = nome
        self.data = data
        self.meds = meds
        self.template_file = template_file

    def get_html(self):
        f = open(self.template_file, 'r', encoding='utf-8')
        txt = f.read()

        txt = txt.replace('{{NOME_PACIENTE}}', self.nome)
        txt = txt.replace('{{DATA}}', self.data)

        lista_med = ol()

        # Lista de medicamento
        with lista_med:
            for m in self.meds:
                lista = li(style='font-size: 0.8em')
                lista.add(span(m['nome'], style='font-weight: bold'))
                lista.add(span(m['qtde'], style='float: right'))
                lista.add(p(m['posologia']))

        txt = txt.replace('{{MEDICAMENTOS}}', lista_med.render())

        return txt
