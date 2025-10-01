def kthim_teksti(s: str) -> str:
    """
    Kthen tekstin mbrapsht.
    Rasti bazë: len(s) <= 1 → kthe s
    Rast rekursiv: s[-1] + kthim_teksti(s[:-1])
    """
    if len(s) <= 1:
        return s
    else:
        return s[-1] + kthim_teksti(s[:-1])

if __name__ == "__main__":
    s = input("Teksti: ")
    print(kthim_teksti(s))
