import ply.yacc as yacc
from bt_lexer import BTLexer

class BTParserException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class BTParser(object):
    """BT parser"""

    def __init__(self, **kwargs):
        self.lexer = BTLexer(**kwargs)
        self.tokens = self.lexer.tokens
        kwargs['debug'] = True
        kwargs['write_tables'] = True
        self.parser = yacc.yacc(module=self, **kwargs)

    @staticmethod
    def p_error(p):
        if p:
            raise BTParserException("Syntax error at line %s near %s."%(p.lineno, p.value))
        else:
            raise BTParserException("Reached unexpected end of file.")

    @staticmethod
    def p_state(p):
        """
        state : STATE ID '{' expressions '}'
        """
        print p[1], p[2], p[3]


    @staticmethod
    def p_expressions(p):
        """
        expressions : expression
                    | empty
        """
        print p[1]

    @staticmethod
    def p_expression(p):
        """expression : assign"""
        print p[1]

    @staticmethod 
    def p_assign(p):
        """assign : VARIABLE ID '=' ID ';'"""
        print p[1], p[2], p[3], p[4]


    @staticmethod
    def p_empty(p):
        """empty : """
        pass

    def parse(self, file_name):
        self.parser.parse(open(file_name).read())


if __name__ == '__main__':
    parser = BTParser()
    parser.parse('./test.bt')
