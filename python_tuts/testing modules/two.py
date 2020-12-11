import one
print('top level in two.py')
one.function()
if __name__ == '__main__':
    print('two.py is being run direclty')
else:
    print('two.py is imported')