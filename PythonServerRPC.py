from xmlrpc.server import SimpleXMLRPCServer
class RPC:
    #methods = ['get','set','delete','exists', 'keys', 'calc']
    methods = ['isValid', 'calc']
    operators = {
        '+':'+',
        '-':'-',
        '*':'*',
        '/':'/' 
    }
    def __init__(self, direccion, port):
        self.server = SimpleXMLRPCServer((direccion, port), allow_none=True)
        
        for method in self.methods:
            self.server.register_function(getattr(self, method))
    
    def isValid(self, oper):
        return oper in self.operators
    
    def calc(self, a, b, oper):
        c = 0
        if oper == self.operators['+']:
            c = a+b
        elif oper == self.operators['-']:
            c = a-b
        elif oper == self.operators['*']:
            c = a*b
        elif oper == self.operators['/']:
            c = a/b
        else:
            return 'Operación no válida'
        return c

    def run(self):
        self.server.serve_forever()
        print("Server iniciado")
    
if __name__ == '__main__':
    rpc = RPC('', 20064)
    print('Iniciando servidor...')
    rpc.run()
    