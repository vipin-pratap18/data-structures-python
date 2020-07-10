from Stack import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    binary_num = ""
    while not s.is_empty():
        binary_num += str(s.pop())

    return binary_num


print(div_by_2(242))