# Copyright (c) 2019, Art Compiler LLC

from sympy.physics import units as u
from sympy.physics.units import convert_to
from sympy.functions.elementary.hyperbolic import HyperbolicFunction
from sympy.simplify.fu import TR1, TR2, TR6, TR11, TR22
from sympy import *


FUNC_WHITELIST = [
    'eval',
    'latex',
    'literal',
]

def eval_math(obj):
    if 'func' not in obj:
        raise ValueError('must provide func')
    func = obj['func']
    if func not in FUNC_WHITELIST:
        raise ValueError('func must be eval, latex, or literal')

    if 'expr' not in obj:
        raise ValueError('must provide expr')
    expr = obj['expr']

    if func == 'eval':
        kwargs = {'ln_notation': 'True', 'inv_trig_style': 'power'}
        return latex(eval(expr), **kwargs)
    elif func == 'latex':
        return latex(sympify(expr, evaluate=False))
    elif func == 'literal':
        return expr
    return 'error'
