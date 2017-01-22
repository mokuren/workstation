class Responder:

    def  __init__(self, name):
        self.name = name

    def response(self, input):
        return '{}ってなに?'.format(input)
