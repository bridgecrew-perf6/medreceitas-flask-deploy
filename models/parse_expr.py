import re


class ParseExpr():

    def __init__(self, txt):
        self.txt = txt
        self.var_map = {}

    def get_vars(self) -> dict:
        """
        Retorna dicionário com as váriaveis presentes na expressão
        sem seus valores 
        Ex: {'peso': '', 'altura': ''}
        """
        
        self.var_map = dict.fromkeys(
            expr.group(1) for expr in re.finditer('\[(\w+)\]', self.txt)
        )

        return self.var_map

    def eval_expr(self, var_map) -> str:
        """
        retorna string com expressões calculadas
        """

        expr_replaced = ''
        str_expr = ''
        txt = self.txt
        self.var_map = var_map
        for expr in re.finditer('\{\{(.*?)\}\}', txt):
            # substitui todas as variaveis pelos seus valores
            str_expr = expr.group(0)
            if self.var_map:
                expr_replaced = str_expr
                for key, value in self.var_map.items():
                    expr_replaced = expr_replaced.replace(f'[{key}]', str(value))
            
            expr_replaced = expr_replaced.replace('{{', '').replace('}}', '')
            # substitui no texto original o valor da expressão
            txt = txt.replace(str_expr, str(round(eval(expr_replaced))))

        return txt
