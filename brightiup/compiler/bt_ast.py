
class BTASTException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class BTNamespace(object):
    def __init__(self):
        pass


class BTASTNode(object):
    def __init__(self):
        self.parrent = None
        self.childs = []

    def gen_code(self):
        pass


class BTASTDecoder(BTASTNode):
    def __init__(self, name, states):
        super(BTASTDecoder, self).__init__()
        self.name = name
        self.states = states


class BTASTState(BTASTNode):
    def __init__(self, name, expressions):
        super(BTASTState, self).__init__()
        self.expressions = expressions

class BTASTVariable(BTASTNode):
    def __init__(self, name):
        super(BTASTVariable, self).__init__()


class BTASTBinaryOperator(BTASTNode):
    def __init__(self, operator):
        super(BTASTBinaryOperator, self).__init__()
        self.operator = operator


class BTASTAssign(BTASTNode):
    def __init__(self, variable, value):
        super(BTASTAssign, self).__init__()
        self.variable = variable
        self.value = value

    def __str__(self):
        return "BTAssign: %s = %s"%(self.variable, self.value)


class BTASTInteger(BTASTNode):
    def __init__(self, value):
        super(BTASTInteger, self).__init__()
        self.value = value
