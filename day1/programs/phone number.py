
def getPhoneNumber(s):
    # Write your code here
    word_to_digit = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
        'double': '2', 'triple': '3'
    }

    words = s.split(' ')
    result = ""
    i = 0
    while i < len(words):
        if words[i] in word_to_digit.keys():
            if words[i] == 'double' or words[i] =='triple':
                result += int(word_to_digit[words[i]])*word_to_digit[words[i+1]]
                i+=2
                continue
            else:
                result += word_to_digit[words[i]]
                i+=1

    return result
            
            
            
if __name__ == '__main__':

    s = input()

    result = getPhoneNumber(s)

    print(result)
