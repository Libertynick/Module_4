from math import inf
def divide(first, second):
    if second == 0:
        return inf
    else:
        fake = first / second
        return fake

if __name__ == '__main__':
    print(divide(2,0))