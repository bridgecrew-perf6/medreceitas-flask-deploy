from pony.orm import *
from dataclasses import dataclass
from dataclasses_json import dataclass_json


db = Database()


class Medicamento(db.Entity):
    nome = Required(str)
    posologia = Required(str)
    qtde = Required(str)
    comentarios = Optional(str)

    def __repr__(self):
        return f'[Medicamento] [Nome: {self.nome}, Posologia: {self.posologia}]'


class Protocolo(db.Entity):
    nome = Required(str)
    meds = Optional(Json)

@dataclass_json
@dataclass
class MedSelected:
    nome: str
    posologia: str
    quantidade: str
    comentarios: str

