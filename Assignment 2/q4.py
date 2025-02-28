def isAnagram(s1,s2):
    list1=list(s1)#split the letters of s1 into list1 
    list2=list(s2)#split the letters of s2 into list2 
    list1.sort()#sort the letters so that their order is the same
    list2.sort()
    if list1 == list2:#it means the two lists have the same letter,which is anagram
        return True
    return False#In other case, they are not anagram

word1=input('Please enter a word:')
word2=input('Please enter another word:')
if isAnagram(word1, word2):#if the function return True, it is an anagram
    print(word1,'and',word2,'is an anagram')
else:#if the function return False, it is not an anagram
    print(word1,'and',word2,'is not an anagram')
    