class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        # ass: operations are all valid
        # + comes after 2+ nrs
        # D comes after 1+ nrs
        # C comes after 1+ nrs

        for op in operations:
            if op == '+':
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                scores.append(scores[-1] * 2)
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)
        