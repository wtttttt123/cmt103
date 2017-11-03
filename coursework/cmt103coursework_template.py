##CMT103 COURSEWORK 2017/18 ###
###############################
##You need to implet the following methods:
##
##Task 1
##readnumbers()  [2 marks]
##isPrime()    [5 marks]
##
##Task 2
##readsequences()  [2 marks] 
##longest_common_string() [6 marks]
##
##Task 3
##get_words() [4 marks]
##sort_tuples() [4 marks]
##get_top_10() [7 marks]
################################


###################################################
#Task 1: Check if a Given Number is a Prim Number:#
###################################################
def readnumbers(file_name): 
    '''
    Input: a file name
    Return: a list of numbers
    '''
    with open(file_name,"r") as f:
        numbers=f.read()
        number = numbers.strip("\n").split(", ")
        for i in range(len(number)):
           number[i]=int(number[i])
        return(numbe)

        


def isPrime(num):      
    '''
    Input: an integer
    Return: a boolean 
    '''
    for i in range(2,num):
        if num%i==0:
            return False    
    return True


############################################ 
#Task 2: Find the longest common substring #
#       between two strings:               #
############################################
def readsequences(file_name): 
    '''
    Input: a file name
    Return: a tuple of two strings
    '''
    with open(file_name,"r") as f:
        cont=f.read()
        lines=cont.split("\n")
        return(tuple(lines))


def longest_common_string(st1, st2): 
    '''
    Input: two string sequences
    Return: the longest common sub-string of the two strings 
    '''
    longst=""
    for i in range(len(st1)):
        for j in range(len(st1)-i+1):
            if st1[i:i+j]in st2 and len(st1[i:i+j])>len(longst):
                longst=st1[i:i+j]
    return longst
                

######################################
#Task 3: Get Top 10 ly-Words:        #
######################################
def get_words(file_name): 
    '''
    Input: the text file of a fiction
    Output: a list of all words that have occured in the file.
    '''

    import string
    with open(file_name,"r") as f:
        book=f.read()
        words=book.replace("\n"," ").replace("\r"," ")
        punc=string.punctuation
        for i in list(punc):
            words=words.replace(i," ")    
        words=words.split(" ")
        j=0
        for i in words:
            if i=='':
                j+=1
        for k in range(j):
            words.remove('')
        return(words)


def get_dic(words): 
    '''
    Input: a list of words
    Return: a dic of ly-words and its number of occurrences
    '''
    adic={}    
    for i in words: 
        if i not in adic and i[-2:]=="ly":
            adic[i]=0
        elif i in adic and i[-2:]=="ly":
            adic[i]+=1
    return adic
            
    
def get_top_10(dic): 
    '''
    Input: a dic of ly-words and its number of occurrences
    Return: a sorted list of top 10 two-element tuples.
    '''
    vlst=[]
    al=[]
    for key,value in dic.items():
        vlst+=value
    sorv=vlst.sort(reverse=true)
    for i in range(10):
        a,b=dic(sorv(i)),sorv(i)   
        c=tuple(a,b)
        al+=c
    return al
            



####### THE CODE BELOW IS FOR TESTING###################
############### DO NOT  CHANGE #########################


import sys
if __name__ == '__main__':
    #Take care of the console inputs
    if len(sys.argv)<=1:
        sys.argv = ['', "numbers.txt", "sequences.txt", "sense_and_sensitivity.txt"]
        
   
    stars = '*'*40
    print(stars)
    print("Testing Task 1 --- Is It a Prime?")
    print(stars)

    #Task 1-a
    try:
        nums = readnumbers(sys.argv[1])
        if not nums:
            print("readnumbers() returns None.")
        else:
            print("Numbers: ", nums)
            print()
    except Exception as e:
        print("Error (readnumbers()): ", e)

    #Task 1-b
    try:
        if not nums: #Task 1-a has not been implemented
            print("isPrime() skipped....")
        else:    
            for num in nums:
                result = isPrime(num)
                if result==None:
                    print("isPrime() returns None.")
                    break
                print("{} : {}".format(num, "Prime" if result else "Not Prime"))
                    
    except Exception as e:
        print("Error (isPrime()):", e)

    #testing task 2
    print("\n\n"+stars)
    print("Testing Task 2 --- Longest Common Substring")
    print(stars)

    #Task 2-a
    try:
        tup = readsequences(sys.argv[2])
        if not tup:
            print("readsequences() returns None.")
        else:
            st1, st2 = tup
            print("The first string: {}".format(st1)) 
            print("The second string: {}".format(st2)) 
    except Exception as e:
        print("Error (readsequences()):", e)

    #Task 2-b
    try:
        if not tup: #Task 2-a has not been implemented
            print("longest_common_string() skipped...")
        else:
            commonst= longest_common_string(st1, st2)
            if not commonst:
                print("longest_common_string()  returns None.")
            else:
                print("The longest common substring is {} of size {}.".format(commonst,len(commonst)))    
    except Exception as e:
        print("Error (longest_common_string()):", e)

    print("\n\n"+stars)
    print("Testing Task 3 --- Top LY Words")
    print(stars)

    #Task 3-a
    try:
        words = get_words(sys.argv[3])
        if not words:
            print("get_words()  returns None.")
        else:
            print("+ {} has a total of {} words.".format(sys.argv[3], len(words)))
    except Exception as e:
        print("Error (get_words()):", e)

    #Task 3-b
    try:
        if not words: #Task 3-a has not been implemented
            print("get_dic() skipped....")
        else:
            dic = get_dic(words)
            if not dic:
                print("get_dic()  returns None.")
            else:
                print("+ There are {} ly-words in the file.\n+ '{}' and '{}' have {}, {} occurrences respectively.\n".format(len(dic), 'only', 'hardly', dic['only'], dic['hardly']))
    except Exception as e:
        print("Error (get_dic()):", e)

    #Task 3-c
    try:
        if not words or not dic: #Task 3-a has not been implemented
            print("get_top_10() skipped....")
        else:
            results = get_top_10(dic)
            if not results:
                print("get_top_10() returns None.")
            else:
                print("+ Top 10 ly-Words in {}:".format(sys.argv[3]))
                for word, n in results:
                    print(" "*5+"{:<20} {:<}".format(word, n)) 
    except Exception as e:
        print("Error (get_top_10()):", e)


