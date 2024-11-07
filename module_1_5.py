immutable_var = "Hello", 62.0, 55, False
print (immutable_var)
#immutable_var[3] = 512 # невозможно обратиться к элементу кортежа, так как этот элемент
# не является списком

mutable_list = [15, 55, 124., "Bye"]
mutable_list[0] = "Fifteen"
print (mutable_list)