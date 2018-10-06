from helpers import alphabet_position, rotate_character

def encrypt(textMsg, numRot):
    
    encrypted = ""
    
    for char in textMsg:
        encrypted+= rotate_character(char, numRot)
        
    return encrypted

def main():
               
  
    print("Input a string to rotate:")
    msgStr = input()
              
    print("What is the key:")
    keyStr = input()
                         
    print(encrypt(msgStr,int(keyStr)))

    

if __name__ == "__main__":
    main()
