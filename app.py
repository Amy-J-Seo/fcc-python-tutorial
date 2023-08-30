try:
    x = int(input('Enter a number: '))
    print(x)
except ValueError:
    print("Something went wrong", ValueError)
except NameError:
    print('name?')
else:
    print('nothing went wrong')
finally:
    print('finished')