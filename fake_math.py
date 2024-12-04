def divide(first, second):
    if second == 0:
        return 'Error'
    else:
        fake = first / second
        return fake

if __name__ == '__main__':
    print(divide(2, 2))