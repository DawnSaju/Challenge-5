def main():
    W, H, t = map(int, input().split())
    n = int(input())
    possibilities = []
    for i in range(n):
        ti, Li, Ti, Ri, Bi = map(int, input().split())
        possibilities.append((ti, Li, Ti, Ri, Bi))
    possibilities.sort(key=lambda x: x[0])
    if W == H == t == 0:
        return
    else:
        x, y = 0, 0
        for i in range(n):
            ti, Li, Ti, Ri, Bi = possibilities[i]
            if Li <= x <= Ri and Bi <= y <= Ti:
                continue
            elif Li <= x <= Ri and y < Bi:
                y = Bi
            elif Li <= x <= Ri and y > Ti:
                y = Ti
            elif x < Li and Li <= y <= Ti:
                x = Li
            elif x > Ri and Li <= y <= Ti:
                x = Ri
            elif x < Li and y < Bi:
                x, y = Li, Bi
            elif x < Li and y > Ti:
                x, y = Li, Ti
            elif x > Ri and y < Bi:
                x, y = Ri, Bi
            elif x > Ri and y > Ti:
                x, y = Ri, Ti
            else:
                print("Nothing known.")
                return
            print("Time step {}: Crime Master Gogo has been at {} {}".format(ti, y, x))
        print("Robbery #2: Crime Master Gogo has escaped.")

if __name__ == "__main__":
    main()
