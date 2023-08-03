def letterCombinations(digits: str):

    result = []
    digitsToChar = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'qprs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtracking(i, curStr):
        if len(curStr) == len(digits):
            result.append(curStr)
            return
        
        #recursive case to create all the combinations
        for c in digitsToChar[digits[i]]:
            #the index after i and add each character values of the key to create new combinations
            backtracking(i + 1, curStr + c)
    
    backtracking(0, '')
    return result

        
