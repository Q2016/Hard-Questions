Question:
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.










Solution: Backtracking
  
Explanation
First find out where the start and the end is.
Also We need to know the number of empty cells.

We we try to explore a cell,
it will change 0 to -2 and do a dfs in 4 direction.

If we hit the target and pass all empty cells, increment the result.


Complexity
Time complexity is as good as dp,
but it take less space and easier to implement.  
  
    def uniquePathsIII(self, A):
        self.res = 0
        m, n, empty = len(A), len(A[0]), 1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    x, y = (i, j)
                elif A[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0): return
            if A[x][y] == 2:
                self.res += empty == 0
                return
            A[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            A[x][y] = 0
        dfs(x, y, empty)
        return self.res  

