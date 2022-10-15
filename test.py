import sys
from model import Valuta
from model import Crypto

def main():

    n = int(sys.argv[1])
    l = []
    if n > 0:
        for i in range(n):
            line = input()
            k = line.split(";")
            if len(k) == 3:
                l.append(Valuta(k[0], k[1], float(k[2])))
            elif len(k) == 4:
                l.append(Valuta(k[0], k[1], float(k[2]), k[3]))
            else:
                print("hibás input")
        else:
            print("az argumentum hibás")

        l.sort()
        for valuta in l:
            print(valuta)

if __name__ == "__main__":
    main()