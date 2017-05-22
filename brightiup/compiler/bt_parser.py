import sys
import ply.yacc as yacc
from bt_lexer import BTLexer
import bt_ast as ast

sys.path.append('../../common')
from log import ConsoleLogger

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
        self.parser = yacc.yacc(module=self, start='decoder', **kwargs)

    @staticmethod
    def p_error(p):
        if p:
            raise BTParserException("Syntax error at line %s near %s."%(p.lineno, p.value))
        else:
            raise BTParserException("Reached unexpected end of file.")

    @staticmethod
    def p_decoder(p):
        """decoder : states"""
        p[0] = ast.BTASTDecoder('test', p[1])

    @staticmethod
    def p_states(p):
        """states : states state"""
        p[0] = p[1]
        p[0].append(p[2])

    @staticmethod
    def p_states_single(p):
        """states : state"""
        p[0] = [p[1]]

    @staticmethod
    def p_state(p):
        """
        state : STATE ID '{' expressions '}'
        """
        p[0] = ast.BTASTState(p[1], p[4])


    @staticmethod
    def p_expressions(p):
        """
        expressions : expressions expression
        """
        p[0] = p[1]
        p[0].append(p[2])

    @staticmethod
    def p_expressions_empty(p):
        """
        expressions : empty
        """
        # p[0] = p[1]
        # p[0].append(p[2])
        p[0] = []

    @staticmethod
    def p_expressions_single(p):
        """
        expressions : expression 
        """
        p[0] = [p[1]]


    @staticmethod
    def p_expression(p):
        """
        expression : assign
        """
        p[0] = p[1]
    
    @staticmethod 
    def p_assign(p):
        """assign : VARIABLE '=' ID ';'"""
        p[0] = ast.BTASTAssign(p[1], p[3])

    @staticmethod
    def p_empty(p):
        """empty : """
        p[0] = None

    precedence = (
        # ('left', 'empty'),
        # ('left', 'expressions'),
    )

    def parse(self, file_name):
        decoder = self.parser.parse(open(file_name).read())
        states = decoder.states
        for state in states:
            expressions = state.expressions
            for expression in expressions:
                print expression



if __name__ == '__main__':
    parser = BTParser()
    parser.parse('../script/http.bt')
