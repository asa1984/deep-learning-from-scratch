from and_gate import AND
from xor_gate import XOR

def HALF_ADDER(a,b):
    s = XOR(a,b)
    c = AND(a,b)
    return s, c

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = HALF_ADDER(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))