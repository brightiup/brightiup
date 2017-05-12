import ply.lex as lex
import ply.yacc as yacc
import sys

sys.path.append('../../common')
from log import ConsoleLogger

logger = ConsoleLogger()

tokens = (
        'STATE',
        'STATENAME',
        'OBRACE',
        'EBRACE',
        'SEMICOLON',
    )

def t_STATE(t):
    r'state'
    logger.info('Parsing token "%s".'%t.value)
    return t

def t_STATENAME(t):
    r'[a-zA-Z][a_zA-Z0-9_]*'
    logger.info('Parsing token state "%s".'%t.value)
    return t

def t_OBRACE(t):
    r'{'
    logger.info('Parsing token obrace "%s".'%t.value)
    return t

def t_EBRACE(t):
    r'}'
    logger.info('Parsing token ebrace "%s".'%t.value)
    return t

def t_SEMICOLON(t):
    r';'
    logger.info('Parsing token SEMICOLON "%s".'%t.value)
    return t

t_ignore = "\t "

def t_error(t):
    logger.warn("Illegal character '%s'."%t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    new_line_count = len(t.value)
    logger.info('Parsing %s new lines.'%new_line_count)
    t.lexer.lineno += new_line_count

lexer = lex.lex()
lexer.input(open('../script/http.bt').read())
while True:
    tok = lexer.token()
    if not tok: break
    print tok
