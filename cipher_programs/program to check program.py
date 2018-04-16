import sys,random,transpositionalcipher

def main():
    random.seed(41)
    temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(20):
        message = temp * random.randint(4,41)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        for key in range(1,len(message)):
            encrypt1 = transpositionalcipher.encrypt(key,message)
            decrypt1 = transpositionalcipher.decrypt(key,encrypt1)
            if (decrypt1 != message):
                print("Mismatch found!!!")
                print(decrypt1)
                print(message)
                sys.exit()
    print("test cases passed")
    
if __name__=='__main__':
    main()
