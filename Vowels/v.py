# input from the user
text = input('Enter your desired text:')
# function
def countVowels(str):
    count = 0
    # for loop
    for st in str:
        # if condition 
        # string A
        if st == 'a' or st == 'A' or\
        st == 'e' or st == 'E' or\
        st == 'i' or st == 'I' or\
        st == 'o' or st == 'O' or\
        st == 'u' or st == 'U':
        # Count
        count +=1
    # return
    return count
# print statemrnt
print(text, countVowels(text))
    
