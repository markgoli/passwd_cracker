import hashlib

flag = 0

pass_hash = input('Enter the md5 hash: ')

wordlist = input("Enter the file: ")  # file containing the list of passwords 


try :
    pass_file = open(wordlist, "r")

except:
    print('No file found.')
    quit()

for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    # print(word)
    # print(digest)
    # print(pass_hash)



    if digest == pass_hash:
        print('Password found.')
        print(f'password is {word}')
        flag = 1
        break 


if flag == 0:
    print('password/pass phrase is not in the list.')