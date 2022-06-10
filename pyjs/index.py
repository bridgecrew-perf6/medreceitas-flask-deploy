from org.transcrypt.stubs.browser import __pragma__
from datetime import date
import re

__pragma__ ('skip')
document = window = jq = Math = Date = console = 0 # Prevent complaints by optional static checker
__pragma__ ('noskip')

__pragma__ ('alias', 'jq', '$')

btn_imprimir = document.getElementById('btnImprimir')
btn_adicionar = document.getElementById('btnAdicionar')
btn_remover = document.getElementById('btnRemover')
btn_limpar = document.getElementById('btnLimpar')
txt_nome_paciente = document.getElementById('txtNomePaciente')
txt_data = document.getElementById('txtData')
txt_nome_med = document.getElementById('txtNomeMed')
txt_quantidade = document.getElementById('txtQuantidade')
txt_posologia = document.getElementById('txtPosologia')
lista_meds_receita = document.getElementById('lista-meds-receita')
lbl_nome_paciente_receita = document.getElementById('lbl-nome-paciente-receita')
lbl_data_receita = document.getElementById('lbl-data-receita')
txt_meds_list_filter_input = document.getElementById('meds-list-filter-input')

lista_med_receita = []

window.onload = lambda: jq('#txtData').val(date.today().strftime('%d/%m/%Y'))

def print_receita():
    print_contents = document.getElementById('divReceitaHtml').innerHTML
    original_contents = document.body.innerHTML
    document.body.innerHTML = print_contents
    window.print()
    document.body.innerHTML = original_contents
    window.location.reload()

def postMed(event):
    event.preventDefault()
    med_name = event.target.innerHTML
    console.log(med_name)

    def add_med_selected(data):
        jq('#txtNomeMed').val(data.nome)
        jq('#txtPosologia').val(data.posologia)
        jq('#txtQuantidade').val(data.qtde)
        jq('#txtComentarios').val(data.comentarios)
        txt_meds_list_filter_input.value = ''
    
    jq.ajax(
        {
            'type': 'post',
            'url': '/add_med',
            'data': 'med_name=' + med_name,
            'success': lambda response: add_med_selected(response),
        }
    )

    return False

# def evaluate(expr):
#     return __pragma__('js', '{}', 'console.log(eval(expr))')

def eval_expr(txt, var_map) -> str:
    """
    retorna string com expressões calculadas
    """
    expr_replaced = ''
    str_expr = ''
    for expr in re.finditer('\{\{(.*?)\}\}', txt):
        # substitui todas as variaveis pelos seus valores
        str_expr = expr.group(0)
        if var_map:
            expr_replaced = str_expr
            for key, value in var_map.items():
                expr_replaced = expr_replaced.replace(f'[{key}]', str(value))
        
        expr_replaced = expr_replaced.replace('{{', '').replace('}}', '')
        # substitui no texto original o valor da expressão
        txt = txt.replace(str_expr, str(round(eval(expr_replaced))))

    return txt

def get_vars(txt) -> dict:
    """
    Retorna dicionário com as váriaveis presentes na expressão
    sem seus valores 
    Ex: {'peso': '', 'altura': ''}
    """
    vars = {}
    for expr in re.finditer('\[(\w+)\]', txt):
        vars[expr.group(1)] = ''
    return vars

def get_vars_values(txt) -> dict:
    var_map = {}
    for expr in re.finditer('\[(\w+)\]', txt):
        var_name = expr.group(1)
        var_map[var_name] = window.prompt(f'Digite o valor da variável [{var_name}]:')
    return var_map


def remove_ultimo_med_receita():
    lista_meds_receita.removeChild(lista_meds_receita.lastChild)

def remove_med_receita(med_name):
    jq("#lista-meds-receita li").filter(lambda x: x.text() == med_name).remove()

def add_med_receita():
    lbl_nome_paciente_receita.innerHTML = txt_nome_paciente.value
    lbl_data_receita.innerHTML = txt_data.value

    var_map = get_vars_values(txt_posologia.value)
    result_posologia = eval_expr(txt_posologia.value, var_map)

    list_item  = f'<li class="nome-med">'
    list_item += f'    <span class="nome-med" onclick="main.remove_item(parentNode)">{txt_nome_med.value}</span>'
    list_item += f'    <span class="quantidade">{txt_quantidade.value}</span>'
    list_item += f'    <p class="posologia">{result_posologia}</p>'
    list_item += f'</li>'

    lista_meds_receita.innerHTML += list_item

    txt_meds_list_filter_input.focus()

    # med = {
    #     'nome': txt_nome_med.value,
    #     'quantidade': txt_quantidade.value,
    #     'posologia': eval_expr(result_posologia),
    # }
    # lista_med_receita.append(med)

def remove_item(item):
    lista_meds_receita.removeChild(item)


btn_adicionar.addEventListener('click', add_med_receita)
btn_imprimir.addEventListener('click', print_receita)
btn_remover.addEventListener('click', lambda: remove_med_receita('Dipirona 500mg'))

