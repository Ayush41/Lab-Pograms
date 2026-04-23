def xorTruthTable():
    print("XOR Truth Table")
    print("A B | A XOR B")

    for A in [0, 1]:
        for B in [0,1]:
            res = A^B
            print(f"{A} {B} | {res}")
xorTruthTable()
