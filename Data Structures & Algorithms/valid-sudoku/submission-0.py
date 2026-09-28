class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1) check every row, check every col, check every square -> 3 passes
        # 2) 3x dict[set]s + single pass -> 1 pass

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                box_index = ((r // 3) * 3 + (c // 3))
                if num in rows[r] or num in cols[c] or num in boxs[box_index]:
                    return False
                else:
                    rows[r].add(num)
                    cols[c].add(num)
                    boxs[box_index].add(num)
        return True                    
