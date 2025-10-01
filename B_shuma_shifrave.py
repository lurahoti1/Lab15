def shuma_shifrave(n: int) -> int:
    """
    Kthen shumën e shifrave të n për n >= 0.
    Rasti bazë: n < 10 → kthe n
    Rast rekursiv: (n % 10) + shuma_shifrave(n // 10)
    n < 0 → kthe -1
    """
    if n < 0:
        return -1
    elif n < 10:
        return n
    else:
        return (n % 10) + shuma_shifrave(n // 10)

if __name__ == "__main__":
    n = int(input("n: "))
    rezultati = shuma_shifrave(n)
    if rezultati == -1:
        print("Gabim")
    else:
        print(rezultati)
