# функция умножения
def mi(a, b):
    return a * b

# новый текст
text = 'new'

# функция деления
def pul(a, b):
    return a / b

# вывод
if __name__ == '__main__':
    print(mi(10, 2))
    print(pul(10, 2))
    print(mi(10,2 + pul(10,5)))
