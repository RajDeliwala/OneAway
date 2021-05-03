'''
Cracking the coding interview
Chapter 1 - Arrays and Strings page 91
One Awat
Problem Statement: There are three types of edit that can be performed on strings: insert a character, remove a character, or replace a chracter. Given 2 strings, write a function to checck if they are one edit or zero edits away

example:
pale , ple -> True only need to add the "a" from the first string to get an equal string
pales, pale -> True only need to remove the "s" from the first string to get an equal string
pale , bale -> True only need to replace the "p" from the first string to get an equal string
pale , bake -> False, need to make multiple changes to get equal with the first string
    
Constraits or Questions you need to ask:
-Take into account 2 different senarios, are both strings the same length or different

Solution notes:
-Can only have 1 unmatch
'''
#Creating a solution in O(n)

def is_one_away_same_length(string1, string2):
    #Variable to count how many un matches we find, if more than 1, return false
    count = 0
    #loop in the range of string 1 since they're both equal
    for i in range (len(string1)):
        if string1[i] != string2[i]:
            #if any instance of the string 1 doesnt match string 2 then we update count 
            count +=1
            #More than 1 difference in the count means a false
            if count > 1:
                return False
    return True


def is_one_away_diff_length(string1, string2):
    i = 0
    counter = 0
    #While 0 < string 2 length, iterate
    while i < len(string2):
        #Iterate through the strings to see if any differences
        #Using i + counter to catch the next char in string 1 and still look back at string 2's previous instance
        if string1[i + counter] == string2[i]:
            i += 1
        else:
            counter += 1
            #If difference is more than 1, return False
            if counter > 1:
                return False
    #Return True if difference is 1 or less
    return True

def is_one_away(string1, string2):
    #Check if the difference of the lengths of both string is more than 2, that means auto false
    if len(string1) - len(string2) >= 2 or len(string2) - len(string1) >= 2:
        return False
    #else if the length of the 2 strings is the same run that function
    elif len(string1) == len(string2):
        return is_one_away_same_length(string1, string2)
    elif len(string1) > len(string2):
        return is_one_away_diff_length(string1,string2)
    else:
       return is_one_away_diff_length(string2, string1)

print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False