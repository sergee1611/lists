immutable_var = ('f', 's', 1, 4, ['f','h','g'])
print(immutable_var)
# immutable_var[0] = 9 нельзя тк кортеж неизменяемый
mutable_list = [1.2, 3, 5, 'list', False]
mutable_list[1:3] = 'true', 'false'
print(mutable_list)
