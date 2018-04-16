import transpositionalcipher,os,sys,time
def main():
    print("Enter the path of the file which you want to encrypt")
    file = str(input())
    if not os.path.exists(file):
        print("Please Enter the correct file name")
        sys.exit()
    print("Enter the output filename in which you want to take output")
    output = str(input())
    if os.path.exists(output):
        print("This file already exist,you want to (C)ontinue or (q)uit")
        s= input()
        if (s.startswith('q')):
            sys.exit()
    
    print("Enter the Key")
    mykey = int(input())
    print("Enter the mode Encrypt or Decrypt")
    mode = input()
    fo = open(file,'r')
    content = fo.read()
    oo = open(output,'w')
    print(content)
    starttime = time.time()
    if mode == 'Encrypt':
        oo.write(transpositionalcipher.encrypt(mykey,content))
    elif mode == 'Decrypt':
        oo.write(transpositionalcipher.decrypt(mykey,content))
    else :
        print("Wrong choice Baby")
    
    print(round(time.time()-starttime,2))
if __name__ == '__main__':
    main()
