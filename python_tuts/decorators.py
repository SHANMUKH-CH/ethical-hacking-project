#decorators - allow you decorate a fucntion
#retunring a function by calling other fucntion
def hello(name='shan'):
    print('hello() func has been called')
    def greet():
        return ' this is inside the greet() function'
    #print(greet())
    def welcome():
        return '   this is inside the welcome() function'
    #print(welcome())
    if name == 'shan':
        return greet
    else:
        return welcome
x= hello('shan')
print(x())
print('\n')
#exhibit b
def hello():
    return 'hii shan'
def other(func):
    print('someone greeted me')
    print(func())
other(hello)
#wraping
def new_dec(func):
    def wrapper():
        print('some code before ex func')
        func()
        print('code here, after executing func()')
    return wrapper
@new_dec
def func_needed_decorator():
    print('please decorate me')
#instead of below line we put @function name
#func_needed_decorator=new_dec(func_needed_decorator) 
func_needed_decorator()