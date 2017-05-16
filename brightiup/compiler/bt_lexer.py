import ply.lex as lex

class BTLexerException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class BTLexer(object):
    """BT lexer"""
    keywords = [
        # "import",
        "state",
    ]

    tokens = [keyword.upper() for keyword in keywords] + [
                            'ID',
                            'VARIABLE',
                        ]
    t_ignore = " \t"
    t_VARIABLE = r'''\$[A-Za-z][A-Za-z0-9_]*'''

    literals = ".{};="
    
    _keyword_map = {}
    for keyword in keywords:
        _keyword_map[keyword] = keyword.upper()


    @staticmethod
    def t_NEWLINE(t):
        r'''\n+'''
        t.lexer.lineno += t.value.count('\n')

    @staticmethod
    def t_error(t):
        raise BTLexerException('Illegal character %s at line %s'%(t.value[0], t.lineno))

    @staticmethod
    def t_ID(t):
        r'''[A-Za-z][A-Za-z0-9_]*'''
        t.type = BTLexer._keyword_map.get(t.value, 'ID')
        return t

    
    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print tok


if __name__ == '__main__':
    lexer = BTLexer()
    lexer.test(open('../script/http.bt').read())
