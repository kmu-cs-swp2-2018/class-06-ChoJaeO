romans = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
    (1, 'I')
]

def factorial_function(num):
    try:
        num_fac = int(num)
    except:
        return "Error"
    result = 1
    for i in range(1, num_fac + 1):
        result *= i
    return str(result)

def binary_function(num):
    try:
        num_bin = int(num)
    except:
        return "Error"
    prefix_index = 2
    bin_num = str(bin(num))[prefix_index:]
    return bin_num

def dec_function(num):
    try:
        dec_num = "0b" + str(num)
        dec_num = str(int(dec_num,2))
        return dec_num
    except ValueError:
        return "이진수를 입력하세요"
    except:
        return "Error"

def roman(num):
    try:
        n = int(num)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

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
        return 'Error'

    dec_num = 0
    try:
        for value, letters in romans:
            while n.find(letters) == 0:
                dec_num += value
                n = n[len(letters):]

        if dec_num == 0:
            return "Error"
        else:
            return dec_num
    except:
        return "Error"


if __name__ == '__main__':
    print(romantodec("XLV"))