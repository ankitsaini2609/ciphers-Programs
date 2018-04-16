import math
def main():
    print("Enter the the message which you want to encrypt/decrypt")
    e = input()
    print("Enter the key")
    k = int(input())
    print("Enter the mode 1-encrypt,2-decrypt")
    m = int(input())
    if (m == 1 or m == 'encrypt'):
        print(encrypt(k,e))
    elif (m == 2 or m == 'decrypt'):
        print(decrypt(k,e))
    else:
        print("Wrong choice baby")

def encrypt(k,e):
    l = len(e)
    cipher_text = ''
    for i in range(k):
        pointer = i
        while pointer < l:
            cipher_text+=e[pointer]
            pointer += k
    return cipher_text
    
def decrypt(k,e):
    l = len(e)
    numberofRows = k
    numberofCols = math.ceil(l/k)
    cols = 0
    rows = 0
    ciphertext = ['']*numberofCols
    shaded = (numberofRows*numberofCols) - l
    for i in e:
        ciphertext[cols]+=i
        cols+=1
        if(cols == numberofCols or (cols==numberofCols-1 and rows >= numberofRows - shaded)):
            cols = 0
            rows += 1
    return ''.join(ciphertext)

if __name__=='__main__':
    main()
