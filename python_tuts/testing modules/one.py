def function():
    print('func() in one.py')
print('top level in one.py')
if __name__=='__main__':
    print('one.py is being run direclty')
else:
    print('one.py has been imported')