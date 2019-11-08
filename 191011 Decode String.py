DECODE STRING

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
s = "100[leetcode]"


def decodeString(s):
    stack = []
    ans = ''       
    for i in s:
        '''Get the first set'''
        if i != ']':
            stack.append(i)
        else:
            '''When set is collected'''
            tmp = ''
            '''Chech until get to multiplication'''
            while stack and stack[-1] != '[':
                '''Remove from list end and add to tmp'''
                tmp = stack.pop() + tmp
            '''Once get to multiplication'''
            if stack and stack[-1] == '[':
                stack.pop()
            '''Get multiplication factor'''
            c = ''
            '''Incorporate longer digits'''
            while stack and stack[-1].isdigit():
                c = stack.pop() + c
            if c:
                tmp = int(c) * tmp
#                else:
#                    print("Check why empty string")
#                    tmp = ''
            stack += list(tmp)

    return ''.join(stack)