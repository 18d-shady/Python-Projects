start = int(input("start of your range: "))
end = int(input("end of your range: "))
num_list = range(start, end + 1)
ren = len(num_list)
def final_sum():
    return sum(num_list)
print("sum = ", final_sum())

def ap_sum():
    return (start + end) * ren / 2
print("the arithmetic sum = ", ap_sum())

