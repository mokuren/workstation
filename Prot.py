from Ptna import *

if __name__  == '__main__':

    def prompt(obj):
        return obj.get_name() + ':' + obj.get_responder_name() + '>'

    print('Ptna System prototype : ptna')
    ptna = Ptna('ptna')

    while True:
        inputs = input(' > ')
        if not inputs:
            print('バイバイ')
            break
        response = ptna.dialogue(inputs)
        print(prompt(ptna), response)
