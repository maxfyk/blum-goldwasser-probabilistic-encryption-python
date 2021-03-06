from math import factorial

MIN_VALUE = 10  # min p and q value


def is_prime(x): return factorial(x - 1) % x == x - 1


def text_to_bin(text): return "".join(f"{ord(i):08b}" for i in text)


def bin_to_text(text):
    return "".join(chr(int(text[i*8:i*8+8], 2)) for i in range(len(text)//8))


def get_nx():
    """Returns n and x for BBS generator"""
    while True:
        p = int(input("Enter p:"))
        q = int(input("Enter q:"))
        if p == q:
            print("p shouldn't be equal to q")
        elif not is_prime(p) or p < MIN_VALUE or p % 4 != 3:
            print(f"P must be prime and > {MIN_VALUE} and p ≡ 3 mod 4")
        elif not is_prime(q) or q < MIN_VALUE or q % 4 != 3:
            print(f"q must be prime and > {MIN_VALUE} and q ≡ 3 mod 4")
        else:
            break
    while True:
        x = int(input("Enter x:"))
        if not is_prime(x):
            print("x must be prime")
        elif x % p == 0 or x % q == 0:
            print("x should not be divisible by p and q")
        else:
            break
    return p * q, x


def generator(n, xi):
    """Yields xi, si numbers generated by BBS"""
    while True:
        xi = (xi)**2 % n
        si = xi % 2
        yield si


def XOR(text, n, x, binary=False):
    """Applies XOR operation to every byte in text + generator value"""
    gen = generator(n, x)
    text = text.encode('utf8').decode('utf8')
    text = text_to_bin(text) if not binary else text
    en_text = ""
    for i in range(0, len(text)):
        en_text += str(int(text[i]) ^ next(gen))
    return bin_to_text(en_text) if binary else en_text


def main():
    # TEST: 19, 23, 233
    choice = ''
    while(choice not in ['d', 'e']):
        choice = input("Enter d to decrypt/e to encrypt: ")
    n, x = get_nx()
    if choice == 'e':
        inp = input("Enter text to encode:")
        text = XOR(inp, n, x)
    elif choice == 'd':
        inp = input("Enter bits to decode:")
        text = XOR(inp, n, x, True)
    print(text)


if __name__ == '__main__':
    main()
