def faktorial(n: int) -> int:
    """
    n! për n >= 0.
    Raste bazë: 0! = 1, 1! = 1
    Rast rekursiv: n! = n * (n-1)!
    Nëse n < 0 → kthe -1 si sinjal gabimi.
    """
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

if __name__ == "__main__":
    n = int(input("n: "))
    rezultati = faktorial(n)
    if rezultati == -1:
        print("Gabim")
    else:
        print(rezultati)
