print("Enter the message which you want to encrypt or decrypt")
s = input()
s = s.upper()
print("Enter the key")
key = int(input())
print("Enter the mode 1 = encrypt, 2 = decrypt")
m = int(input())
Temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[]{}\|'\"\\;:/?.><,"
a = ""
for i in range(len(s)):
    ind = Temp.find(s[i])
    if (ind == -1):
        a += s[i]
    else :
        if (m == 1):
            ind += key
            ind %= 69
            a+=Temp[ind]
        elif m == 2:
            ind -= key
            if ind < 0:
                ind += 69
            a += Temp[ind]
        else:
            print("Wrong mode selected")
            break
print("Original ",s)
print("After ",a)
