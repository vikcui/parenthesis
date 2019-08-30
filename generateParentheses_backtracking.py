# author: YANG CUI
"""
Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

def generateParenthesis_aux(n):
    listOfParentheses = []
    resultString = ""
    leftCount = 0
    rightCount = 0
    generateParenth(n, resultString, leftCount, rightCount, listOfParentheses)
    return listOfParentheses



def generateParenth(N, resultString, leftCount, rightCount, listOfParentheses) :
    if len(resultString) == 2 * N:
        listOfParentheses.append(resultString)
        return

    if leftCount < N:
        # choose
        resultString = resultString + "("
        leftCount += 1
        # explore
        generateParenth(N, resultString, leftCount, rightCount, listOfParentheses)
        leftCount -= 1
        # unchoose
        resultString = resultString[:len(resultString) - 1]

    if rightCount < leftCount:
        # choose
        resultString = resultString + ")"
        rightCount += 1
        # explore
        generateParenth(N, resultString, leftCount, rightCount, listOfParentheses)
        # unchoose
        rightCount -= 1
        resultString = resultString[:len(resultString) - 1]

# print(generateParenthesis_aux(3))

