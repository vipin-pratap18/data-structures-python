from Stack import Stack

def is_matched(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_balanced(paren):

    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren) and is_balanced:
        parenthesis = paren[index]
        if parenthesis in "([{":
            s.push(parenthesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_matched(top, parenthesis):
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced("((((()))))"))
print(is_paren_balanced("((((()}))))"))