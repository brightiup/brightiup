


class BTASTException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class BTASTNode(object):
    pass

class BTASTDecoder(BTASTNode):
    def __init__(self):
        super(BTASTDecoder, self).__init__()

class BTASTState(BTASTNode):
    def __init__(self):
        super(BTASTState, self).__init__()

class BTASTVariable(BTASTNode):
    def __init__(self):
        super(BTASTVariable, self).__init__()
        
