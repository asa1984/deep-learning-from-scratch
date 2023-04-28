from half_adder import HALF_ADDER
from or_gate import OR

def FULL_ADDER(a,b,c_i):
    (s1,c1) = HALF_ADDER(a,b)
    (s, c2) = HALF_ADDER(s1,c_i)
    c = OR(c1, c2)
    return (s,c)

if __name__ == '__main__':
    for xs in [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]:
        y = HALF_ADDER(xs[0], xs[1], xs[2])
        print(str(xs) + " -> " + str(y))
