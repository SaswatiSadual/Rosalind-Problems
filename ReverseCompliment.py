Pattern = input("Enter the pattern")

Compliment_p = [0]*(len(Pattern))
rev_compliment = [0]*(len(Pattern))
def ReverseCompliment(Pattern):
    for i in range(len(Pattern)):
        if (Pattern[i] == 'A'):
            Compliment_p[i] = 'T'
        elif (Pattern[i] == 'T'):
            Compliment_p[i] = 'A'
        elif (Pattern[i] == 'G'):
            Compliment_p[i] = 'C'
        elif (Pattern[i] == 'C'):
            Compliment_p[i] = 'G'
        else:
            print("Invalid")

    for i in range(len(Pattern)):
        if(isPalindrome(Pattern) == True):
            rev_compliment[i] = Compliment_p[i]
        else:
            k = len(Pattern) - i - 1
            rev_compliment[i] = Compliment_p[k]

    return rev_compliment

def isPalindrome(num):
    if(num == num[::-1]):
        return True
    else:
        return False

c = ReverseCompliment(Pattern)
print(''.join(c))
