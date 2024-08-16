def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1
print_params(4, 'qwerty')
print_params(7, 'asdfg', False)
print_params(15)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

# 2
values_list = [15, True, 'zxcvb']
values_dict = {'a': 245.75, 'b': 'abcdef', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
