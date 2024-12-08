# input from the user
text = input('Enter your desired text:')
# function
def countVowels(str):
    count = 0
    # for loop
    for st in str:
        if st == 'a' or st == 'A' or\
        st == 'e' or st == 'E' or\
        st == 'i' or st == 'I' or\
        st == 'o' or st == 'O' or\
        st == 'u' or st == 'U':
        count +=1
    return count
print(text, countVowels(text))
    
