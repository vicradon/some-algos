def word_search(matrix, word):
    ROWS, COLS = len(matrix), len(matrix[0])

    def dfs(r, c, i):
        if len(word) == i:
            return True
        
        if r >= ROWS or c >= COLS or r < 0 or c < 0 or matrix[r][c] != word[i] or matrix[r][c] == "#":
            return False
        
        temp, matrix[r][c] = matrix[r][c], "#"
        
        found = (
            dfs(r + 1, c, i+1) or
            dfs(r, c + 1, i+1) or
            dfs(r - 1, c, i+1) or
            dfs(r, c - 1, i+1)
        )

        matrix[r][c] = temp

        return found
    
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == word[0]:
                found = dfs(r, c, 0)

                if found:
                    return True

    return False

if __name__ == "__main__":
    matrix = [
        ["A", "B", "D", "F"],
        ["E", "E", "F", "I"],
        ["E", "N", "I", "N"]
    ]
    word1 = "FEB"
    word2 = "BEN"
    word3 = "FINER"

    print(word_search(matrix, word1)) # TRUE
    print(word_search(matrix, word2)) # TRUE
    print(word_search(matrix, word3)) # FALSE

