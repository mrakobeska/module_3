def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = ['ляляля', 7, False]
values_dic = {'a': 9, 'b': 7, 'c': 2}
values_list_2 = [782, 'пампарам']
print_params(*values_list)
print_params(**values_dic)
print_params(*values_list_2, 42)
print_params(b = 25)
print_params(c = [1,2,3])
print_params()
