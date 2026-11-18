
number_list= [i^2 for i in range(100)]
def method_1():
    print(f"list of numbers:{number_list}")
    sorted_list = sorted(number_list)
    print(sorted_list)
    print((sorted_list[-2]))

method_1()