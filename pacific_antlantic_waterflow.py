def pacific_atlantic_waterflow(land):
    ROWS, COLS = len(land), len(land[0])
    atl_visited, pac_visited = set(), set()
    result = []

    def dfs(r, c, visited, prev_height):
        # invalid conditions
        if (
            r >= ROWS or 
            c >= COLS or 
            r < 0 or 
            c < 0 or 
            (r, c) in visited or 
            land[r][c] < prev_height
        ):
            return
        
        # condition is valid, add current cell to the visited set
        visited.add((r, c))
        cur_height = land[r][c]

        # use depth-first search to check the next four possible directions
        dfs(r, c - 1, visited, cur_height)
        dfs(r - 1, c, visited, cur_height)
        dfs(r, c + 1, visited, cur_height)
        dfs(r + 1, c, visited, cur_height)

    # starting point for left and right... prev_height is the value of cell at this starting point
    for r in range(ROWS):
        dfs(r, 0, pac_visited, land[r][0])
        dfs(r, COLS - 1, atl_visited, land[r][COLS - 1])

    # starting point for top and bottom
    for c in range(COLS):
        dfs(0, c, pac_visited, land[0][c])
        dfs(ROWS - 1, c, atl_visited, land[ROWS - 1][c])

    # process results
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in atl_visited and (r, c) in pac_visited:
                result.append([r, c])

    return result

if __name__ == "__main__":
    land = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]]
    
    print(pacific_atlantic_waterflow(land)) # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]