'''
assume a=0,b=1,c=2 ... z=25
1. Suppose you are given with an affine cipher with the following encryption function: c=5m+7 (mod 26).
What’s the ciphertext of the plaintext “helpme”?
'''


def affine_encrypt(message): # c=5m+7%26
    alphabet = [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7), ('i', 8), ('j', 9),
                ('k', 10),
                ('l', 11), ('m', 12), ('n', 13), ('o', 14), ('p', 15), ('q', 16), ('r', 17), ('s', 18), ('t', 19),
                ('u', 20), ('v', 21),
                ('w', 22), ('x', 23), ('y', 24), ('z', 25)]
    cipher = []
    for x,y in alphabet:
        z=((5*y)+7)%26
        new_element = (x,z)
        cipher.append(new_element)
    print(alphabet)

    cipher2=[]
    for x,y in alphabet:
        z=((11*y)+2)%26
        new_element = (x,z)
        cipher2.append(new_element)

    print(cipher2)
    '''encrypted_message = ''
    for letter in message:
        for element in alphabet:
            if letter == element[0]:
                encrypted_letter = ((5*element[1])+7)%26
                encrypted_message= encrypted_message +encrypted_letter

    print(encrypted_message)
'''
def main():
    bruteforcemessage='beeakfydjxuqyhyjiqryhtyjiqfbqduyjiikfuhcqd'

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plaintext = ''
    i=0
    while i < 26:
        for char in bruteforcemessage:
            index = (alphabet.index(char)+1)%26
            #take char lookup index in alphabet and then mod 26
            plaintext= plaintext + alphabet[index]
            #print(plaintext)
        #print result
        print('Round: ',i, 'Message: ', plaintext)
        #convert bruteforced plaintext to new bruteforcemessage
        bruteforcemessage = plaintext
        #reset plaintext
        plaintext = ''
        i += 1




    '''for letter in bruteforcemessage:
        for x, y in alphabet:
            print('x',x, 'y',y)
            if letter == x:
                #next_x = (alphabet.index(x)+1) %26
                #plaintext = plaintext + str(x+1)
                continue
    print(plaintext,'plaintext')
    '''




























# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    #affine_encrypt('helpme')
