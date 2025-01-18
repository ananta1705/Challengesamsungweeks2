a = 2
b = 3
c = 4

nilai = [a, b, c]
nilai.sort(reverse=True)

if nilai == [a, b, c]:
    print("ABC")
elif nilai == [b, a, c]:
    print("BAC")
elif nilai == [c, a, b]:
    print("CAB")
elif nilai == [a, c, b]:
    print("ACB")
elif nilai == [b, c, a]:
    print("BCA")
elif nilai == [c, b, a]:
    print("CBA")