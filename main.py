class Stack():
    def __init__(self, stack: str = ''):
        self.items = list(stack)

    def is_empty(self):
        return self.items == []

    def push(self, bracket):
        self.items.append(bracket)

    def pop(self):
        return self.items.pop()

    def peek(self):
        # вернуть последнее значение не удалив его
        return self.items[-1]

    def size(self):
        return len(self.items)


list_brackets = ['()', '{}', '[]']


def balance(stack_bracket: Stack):
    bracket_revers = Stack()

    if stack_bracket.size() % 2 != 0: #or stack_bracket.is_empty() == []:
        return "Несбалансированнно"


    while not stack_bracket.is_empty():
        current_item = stack_bracket.pop()
        next_item = stack_bracket.peek()
        is_closed = (next_item + current_item) in list_brackets
        if bracket_revers.size() > stack_bracket.size():
            return "Несбалансированнно"
        if not is_closed:
            bracket_revers.push(current_item)
            continue
        stack_bracket.pop()

        while not bracket_revers.is_empty():
            next_item = stack_bracket.peek()
            current_item = bracket_revers.peek()
            is_closed = (next_item + current_item) in list_brackets
            if is_closed:
                next_item = stack_bracket.pop()
                current_item = bracket_revers.pop()
            if not is_closed and stack_bracket.is_empty():
                return "Несбалансированнно"
            if not is_closed:
                break
    return "Сбалансированно"

    # Муторный но рабочий
    # while not stack_bracket.is_empty():
    #     if bracket_revers.size() == stack_bracket.size():
    #         while not stack_bracket.is_empty():
    #             if stack_bracket.peek() + bracket_revers.peek() in list_brackets:
    #                 stack_bracket.pop()
    #                 bracket_revers.pop()
    #                 if stack_bracket.is_empty() and bracket_revers.is_empty():
    #                     return "Сбалансированно"
    #             if stack_bracket.peek() + bracket_revers.peek() not in list_brackets:
    #                 return "Несбалансированнно"
    #     current_item = stack.pop()
    #     next_item = stack.peek()
    #
    #     if (next_item + current_item) in list_brackets:
    #         stack_bracket.pop()
    #
    #     if bracket_revers.size() > stack_bracket.size():
    #         return "Несбалансированнно"
    #
    #     if (next_item + current_item) not in list_brackets:
    #         bracket_revers.push(current_item)
    #
    #     if stack_bracket.peek() + bracket_revers.peek() in list_brackets:
    #         n = bracket_revers.size()
    #         while n > 0:
    #             n -= 1
    #             if stack_bracket.peek() + bracket_revers.peek() in list_brackets:
    #                 stack_bracket.pop()
    #                 bracket_revers.pop()
    #                 if stack_bracket.is_empty() and bracket_revers.is_empty():
    #                     return "Сбалансированно"


if __name__ == '__main__':
    stack = Stack("[([])((([[[]]])))]{()}({})") # Сбалансированно
    print(balance(stack))
    stack = Stack("{[([])((([[[]]])))]}{()}({})") # Сбалансированно
    print(balance(stack))
    stack = Stack("[([])((([[[((]]])))]{()}({})") # Несбалансированно
    print(balance(stack))
    stack = Stack("((([])))])") # Несбалансированнно
    print(balance(stack))
    stack = Stack("{{)") # Несбалансированнно
    print(balance(stack))
    stack = Stack("({})") # Сбалансированно
    print(balance(stack))
    stack = Stack("(((([{}]))))") # Сбалансированно
    print(balance(stack))
    stack = Stack("{{[()]}}") # Сбалансированно
    print(balance(stack))
    stack = Stack("}{}") # Несбалансированнно
    print(balance(stack))
    stack = Stack("{{[(])]}}") # Несбалансированнно
    print(balance(stack))
    stack = Stack("[[{())}]") # Несбалансированнно
    print(balance(stack))
