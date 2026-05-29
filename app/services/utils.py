BASE62_ALPHABETS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_base62(num: int)-> str:
    if num == 0:
        return BASE62_ALPHABETS[0]
    
    arr = []
    base = len(BASE62_ALPHABETS)

    while num > 0:
        num, rem = divmod(num,base)
        arr.append(BASE62_ALPHABETS[rem])

    return "".join(reversed(arr)) # reverse because the last remainder is most significant digit