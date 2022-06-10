// Transcrypt'ed from Python, 2022-06-07 17:34:53
var re = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_re__ from './re.js';
__nest__ (re, '', __module_re__);
import {date} from './datetime.js';
var __name__ = '__main__';
export var btn_imprimir = document.getElementById ('btnImprimir');
export var btn_adicionar = document.getElementById ('btnAdicionar');
export var btn_remover = document.getElementById ('btnRemover');
export var btn_limpar = document.getElementById ('btnLimpar');
export var txt_nome_paciente = document.getElementById ('txtNomePaciente');
export var txt_data = document.getElementById ('txtData');
export var txt_nome_med = document.getElementById ('txtNomeMed');
export var txt_quantidade = document.getElementById ('txtQuantidade');
export var txt_posologia = document.getElementById ('txtPosologia');
export var lista_meds_receita = document.getElementById ('lista-meds-receita');
export var lbl_nome_paciente_receita = document.getElementById ('lbl-nome-paciente-receita');
export var lbl_data_receita = document.getElementById ('lbl-data-receita');
export var txt_meds_list_filter_input = document.getElementById ('meds-list-filter-input');
export var lista_med_receita = [];
window.onload = (function __lambda__ () {
	return $ ('#txtData').val (date.today ().strftime ('%d/%m/%Y'));
});
export var print_receita = function () {
	var print_contents = document.getElementById ('divReceitaHtml').innerHTML;
	var original_contents = document.body.innerHTML;
	document.body.innerHTML = print_contents;
	window.print ();
	document.body.innerHTML = original_contents;
	window.location.reload ();
};
export var postMed = function (event) {
	event.preventDefault ();
	var med_name = event.target.innerHTML;
	console.log (med_name);
	var add_med_selected = function (data) {
		$ ('#txtNomeMed').val (data.nome);
		$ ('#txtPosologia').val (data.posologia);
		$ ('#txtQuantidade').val (data.qtde);
		$ ('#txtComentarios').val (data.comentarios);
		txt_meds_list_filter_input.value = '';
	};
	$.ajax (dict ({'type': 'post', 'url': '/add_med', 'data': 'med_name=' + med_name, 'success': (function __lambda__ (response) {
		return add_med_selected (response);
	})}));
	return false;
};
export var eval_expr = function (txt, var_map) {
	var expr_replaced = '';
	var str_expr = '';
	for (var expr of re.finditer ('\\{\\{(.*?)\\}\\}', txt)) {
		var str_expr = expr.group (0);
		if (var_map) {
			var expr_replaced = str_expr;
			for (var [key, value] of var_map.py_items ()) {
				var expr_replaced = expr_replaced.py_replace ('[{}]'.format (key), str (value));
			}
		}
		var expr_replaced = expr_replaced.py_replace ('{{', '').py_replace ('}}', '');
		var txt = txt.py_replace (str_expr, str (round (eval (expr_replaced))));
	}
	return txt;
};
export var get_vars = function (txt) {
	var vars = dict ({});
	for (var expr of re.finditer ('\\[(\\w+)\\]', txt)) {
		vars [expr.group (1)] = '';
	}
	return vars;
};
export var get_vars_values = function (txt) {
	var var_map = dict ({});
	for (var expr of re.finditer ('\\[(\\w+)\\]', txt)) {
		var var_name = expr.group (1);
		var_map [var_name] = window.prompt ('Digite o valor da variável [{}]:'.format (var_name));
	}
	return var_map;
};
export var remove_ultimo_med_receita = function () {
	lista_meds_receita.removeChild (lista_meds_receita.lastChild);
};
export var remove_med_receita = function (med_name) {
	$ ('#lista-meds-receita li').filter ((function __lambda__ (x) {
		return x.text () == med_name;
	})).remove ();
};
export var add_med_receita = function () {
	lbl_nome_paciente_receita.innerHTML = txt_nome_paciente.value;
	lbl_data_receita.innerHTML = txt_data.value;
	var var_map = get_vars_values (txt_posologia.value);
	var result_posologia = eval_expr (txt_posologia.value, var_map);
	var list_item = '<li class="nome-med">'.format ();
	list_item += '    <span class="nome-med" onclick="main.remove_item(parentNode)">{}</span>'.format (txt_nome_med.value);
	list_item += '    <span class="quantidade">{}</span>'.format (txt_quantidade.value);
	list_item += '    <p class="posologia">{}</p>'.format (result_posologia);
	list_item += '</li>'.format ();
	lista_meds_receita.innerHTML += list_item;
	txt_meds_list_filter_input.focus ();
};
export var remove_item = function (item) {
	lista_meds_receita.removeChild (item);
};
btn_adicionar.addEventListener ('click', add_med_receita);
btn_imprimir.addEventListener ('click', print_receita);
btn_remover.addEventListener ('click', (function __lambda__ () {
	return remove_med_receita ('Dipirona 500mg');
}));

//# sourceMappingURL=index.map