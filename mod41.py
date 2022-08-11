#Python script to produce flag for picoCTF basic-mod2
#Written by Nigel Evans 2022        https://www.linkedin.com/in/nigel-a-evans
#GNU General Public License v3.0

def main ():
    myfile = open('message.txt','r')       #Open the file and read contents into 'data'
    data = myfile.read()
    dataList = data.split(' ')             #Split the data into a list, delimiter = ' '
    myfile.close()                         
    del dataList[-1]                       #Remove the trailing '' from the list

    modList = []                           #Initialize list to hold post modulus values
    modInvList = []                        #Initialize inverse modulus values list
    masterList = []                        #Initialize master list (Cipher key)
    flag = ''                              #Initialize variable to hold our flag

    print('*** Script to solve picoCTF Basic-mod2 ***')
    print('Your list contains the following', len(dataList), 'elements:\n')
    print(dataList)
    print('')

    for i in range(0, len(dataList)):      #Iterate through the list
        ph = int(dataList[i])              #ph = placeholder, convert value to int
        modList.append(ph % 41)            #Mod 41 dataList values, append to modList

    print('Modulus operation successful\n')    
    print('Your new list contains the following', len(dataList), 'post-modulus values:\n')
    print(modList)
    print('')

    def upAlpha():                         
        return list(map(chr, range(65,91))) #Map uppercase chars into a list  
        
    def numList():                          
        return list(map(chr, range(48,58))) #Map decimal digits into a list       
        
    for i in range(0, len(upAlpha())):      #Append upAlpha elements into masterList
        masterList.append(upAlpha()[i])
        
    for i in range(0, len(numList())):      #Append numList elements into masterList
        masterList.append(numList()[i])

    masterList.append('_')                  #Append an underscore to the end of masterList

    for i in range(0, len(modList)):        #Build our list of inverse mod values
        modInvList.append(pow(modList[i],-1,41))

    for i in range(0, len(modInvList)):     #Build our flag
        ph = int(modInvList[i] - 1)         #ph = placeholder, convert value to int
        flag += masterList[ph]              # -1 otherwise index out of range

    print('Your inverse mod values list:\n')  
    print(modInvList)   
    print('')    
    print('Your flag is: picoCTF{' + flag + '}')    #Print flag in correct format
 
main()            

