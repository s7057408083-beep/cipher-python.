
# Вспомогательная функция: алфавит
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# 1. Шифр Цезаря
def caesar_encrypt(text, shift):
    text = text.upper()
    result = ''
    for c in text:
        if c in ALPHABET:
            idx = (ALPHABET.index(c) + shift) % 26
            result += ALPHABET[idx]
        else:
            result += c
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# 2. Шифр Виженера
def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ''
    key_index = 0
    for c in text:
        if c in ALPHABET:
            shift = ALPHABET.index(key[key_index % len(key)])
            idx = (ALPHABET.index(c) + shift) % 26
            result += ALPHABET[idx]
            key_index += 1
        else:
            result += c
    return result

def vigenere_decrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ''
    key_index = 0
    for c in text:
        if c in ALPHABET:
            shift = ALPHABET.index(key[key_index % len(key)])
            idx = (ALPHABET.index(c) - shift) % 26
            result += ALPHABET[idx]
            key_index += 1
        else:
            result += c
    return result


# 3. Шифр замены
def substitution_encrypt(text, key_map):
    text = text.upper()
    result = ''
    for c in text:
        if c in ALPHABET:
            result += key_map[ALPHABET.index(c)]
        else:
            result += c
    return result

def substitution_decrypt(text, key_map):
    inverse_map = ['']*26
    for i, c in enumerate(key_map):
        inverse_map[ALPHABET.index(c)] = ALPHABET[i]
    result = ''
    for c in text:
        if c in ALPHABET:
            result += inverse_map[ALPHABET.index(c)]
        else:
            result += c
    return result
import random
#омофонический шифр
def homophonic_encrypt(text):
    text = text.upper()
    mapping = {c: [str(i) for i in range(10*c_idx, 10*c_idx+10)] for c_idx, c in enumerate(ALPHABET)}
    result = []
    for c in text:
        if c in ALPHABET:
            result.append(random.choice(mapping[c]))
        else:
            result.append(c)
    return ' '.join(result)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi
    while e > 0:
        q = temp_phi // e
        r = temp_phi - q * e
        x = x2 - q * x1
        y = d - q * y1
        temp_phi, e = e, r
        x2, x1 = x1, x
        d, y1 = y1, y
    if temp_phi == 1:
        return d + phi
    return None


print("Цезарь:", caesar_encrypt("HELLO WORLD", 3))
print("Виженер:", vigenere_encrypt("HELLO WORLD", "KEY"))
key_map = list(ALPHABET)
random.shuffle(key_map)
print("Замена:", substitution_encrypt("HELLO WORLD", key_map))
print("Омофонический шифр:", homophonic_encrypt("HELLO"))

