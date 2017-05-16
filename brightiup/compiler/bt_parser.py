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
        print 'p_state', p[1], p[2], p[3], p[4], p[5]
        p[0] = 'hhhh'


    # @staticmethod
    # def p_expressions(p):
        # """
        # expressions : expressions expression
        # """
        # print 'p_expressions', p[1]

    @staticmethod
    def p_expressions_single(p):
        """
        expressions : expression
        """
        print 'p_expressions_single', p[1]
        p[0] = 'hhhhh'


    @staticmethod
    def p_expression(p):
        """
        expression : assign
                   | empty
        """
        print 'p_expression', p[1]
        p[0] = 'hhhhh'

    
    @staticmethod 
    def p_assign(p):
        """assign : VARIABLE '=' ID ';'"""
        print 'p_assign', p[1], p[2], p[3], p[4]
        p[0] = 'hhhhh'


    @staticmethod
    def p_empty(p):
        """empty : """
        print 'empty'

    def parse(self, file_name):
        self.parser.parse(open(file_name).read())


if __name__ == '__main__':
    parser = BTParser()
    parser.parse('./test.bt')
