import transpositionalcipher,detectenglish

def main():
    message = input("Type your message \n")
    hackedmessage = hackTransposition(message)
    if hackedmessage == None:
        print("Failed to hack encrypted message")
    else:
        print("message is ==>")
        print(hackedmessage)

def hackTransposition(message):
    print("Hacking...")
    print("Press ctrl+c or ctrl+d to interrupt")
    for key in range(1,len(message)):
        print("key ",key)
        decrypted = transpositionalcipher.decrypt(key,message)
        if detectenglish.isEnglish(decrypted):
            print()
            print("Possible Decryption")
            print(decrypted)
            print("Enter d for done and enter for continue:")
            s = input()
            s = s.strip()
            if s.startswith('d'):
                return decrypted
    return None


if __name__=='__main__':
    main()
