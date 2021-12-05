flag = [0, 54, 26, 32, 59, 62, 16, 21, 4, 41, 54, 104, 34, 41, 32, 29, 34, 112, 59, 62, 63, 114, 49, 13, 117, 42, 102, 12, 34, 113, 37, 112, 121, 40]

key = "ABRAXUS"

for i in range(len(flag)):
    print(chr(flag[i] ^ ord(key[i % len(key)])), end = '')
