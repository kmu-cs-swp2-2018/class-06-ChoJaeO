def factorial_function(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return str(result)

def binary_function(num):
    bin_num = str(bin(num))
    bin_num = bin_num[2:]
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
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    dec_num = 0
    cnt = 0
    for value, letters in romans:
        while n.find(letters) == 0:
            dec_num += value
            n = n[len(letters):]
            cnt += 1
    if cnt == 0:
        return "Error"
        """
        while cnt < len(num)+1:

            

            if len(letters) == 1:
                if num[-cnt] == letters:
                    dec_num += value
                    cnt += 1
                else:
                    break
            elif len(letters) == 2 and len(num)-cnt >= 1:
                if num[-cnt] + num[-(cnt+1)] == letters:
                    dec_num += value
                    cnt += 1
                else:
                    break
            else:
                break
        """
    else:
        return dec_num


if __name__ == '__main__':
    print(romantodec("XLV"))