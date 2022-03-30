from stack import Stack


def check_bracket_sequence(sequence, stack):
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for item in sequence:
        if item in bracket_pairs:
            stack.push(item)
        elif stack.peek()[0] == -1:
            return 'Несбалансированно'
        elif item == bracket_pairs.get(stack.peek()):
            stack.pop()
        elif item != bracket_pairs.get(stack.peek()):
            return 'Несбалансированно'  
            
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

if __name__ == "__main__":
    print(check_bracket_sequence('[{()}](', Stack()))