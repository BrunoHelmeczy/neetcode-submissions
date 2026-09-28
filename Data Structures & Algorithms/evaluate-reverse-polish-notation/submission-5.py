class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # all operations: apply to last 2 nrs only
        # div: integer div (round to zero)
        # ass: all token arrays are valid
            # starts w 2 nrs
            # n(operands) = n(operators) + 1
        stack = []

        for t in tokens:
            if t in '+-/*':
                n1 = stack.pop()
                n2 = stack.pop()
                if t == '+':
                    n3 = n2 + n1
                if t == '-':
                    n3 = n2 - n1 
                if t == '*':
                    n3 = n2 * n1
                if t == '/':
                    n3 = n2 / n1
                stack.append(int(n3))
            else:
                stack.append(int(t))
        return stack[-1]


        