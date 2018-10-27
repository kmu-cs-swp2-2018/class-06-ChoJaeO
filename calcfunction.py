def factorial_function(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return str(result)

def binary_function(num):
    return str(bin(num))

def dec_function(num):
    return str(int(num,2))

def roman(num):
    try:
        n = int(num)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result

def romantodec(num):
    try:
        n = str(num)
    except:
        return 'Error!'
    romans = [
        (1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'),
        (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'),
        (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M'),
    ]

    dec_num = 0
    cnt  = 1
    for value, letters in romans:
        while cnt < len(num)+1:
            if len(letters) == 1:
                if num[-cnt] == letters:
                    dec_num += value
                    cnt += 1
                else:
                    break
            elif len(letters) == 2 and len(num)-cnt >= 2:
                if num[-cnt] + num[-(cnt+1)] == letters:
                    dec_num += value
                    cnt += 1
                else:
                    break
            else:
                break

    return dec_num


if __name__ == '__main__':
    print(romantodec("CXXIII"))