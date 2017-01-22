


def dec(func):
    def new_func():
        print ('function called:' + func.__name__)
        return func()
   

@dec
def hello():
    return "ごぶさた!"

print (hello())
