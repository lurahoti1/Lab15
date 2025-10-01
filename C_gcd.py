def gcd(a: int, b: int) -> int:
    """
    Kthen GCD(a,b) për a,b >= 0, jo të dy 0.
    Rasti bazë: b == 0 → kthe a
    Rast rekursiv: gcd(b, a % b)
    Nëse a < 0 ose b < 0 → kthe -1
    Nëse a == 0 dhe b == 0 → kthe -1
    """
    if a < 0 or b < 0 or (a == 0 and b == 0):
        return -1
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    rezultati = gcd(a, b)
    if rezultati == -1:
        print("Gabim")
    else:
        print(rezultati)
