from string import ascii_letters

def encrypt(string, key):
    alpha = ascii_letters
    result=''

    for ch in string :
        if ch not in alpha :
            result += ch
        else :
            new_key = (alpha.index(ch)+key) % len(alpha)
            result += alpha[new_key]
    return result


print(encrypt('hamedZ', 4))


def decrypt(string, key):
    key *= -1
    return encrypt(string, key)

print(decrypt('leqihd', 4))


def brute_force(string):
    alpha = ascii_letters
    key = 1
    result =''
    brute_force_date = {}


    while key <= len(alpha):
        result = decrypt(string,key)
        brute_force_date[key]= result
        result=''
        key += 1
    return brute_force_date


print(brute_force('eqmv'))