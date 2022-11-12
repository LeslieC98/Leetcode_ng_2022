"""class desertTraversal():
    def __init__(self, desert):
        self.desert = desert

    def dfs_desert(self, x, y, gas, numSteps, visited):
        temp = str(x) + "-" + str(y)
        if (temp in visited):
            return False
        visited.append(temp)
        if not (0 <= x < len(self.desert)) or not (0 <= y < len(self.desert[0])) or self.desert[x][
            y] == 'r' or numSteps > gas:
            return False

        if self.desert[x][y] == 'o':
            return True

        # if self.desert[x][y].isnumeric(): ##doesnt work if string is not unicode
        if self.desert[x][y] != 'c' and self.desert[x][y] != 'r' and self.desert[x][y] != '.' and self.desert[x][
            y] != 'o':
            # print(int(self.desert[x][y]))
            numSteps -= int(self.desert[x][y])

        found = self.dfs_desert(x + 1, y, gas, numSteps + 1, visited) \
                or self.dfs_desert(x - 1, y, gas, numSteps + 1, visited) \
                or self.dfs_desert(x, y + 1, gas, numSteps + 1, visited) \
                or self.dfs_desert(x, y - 1, gas, numSteps + 1, visited)

        return found

    def check_reach_oasis_in_gas(self, gas):
        # find car

        if not self.desert:
            return False

        for r in range(len(self.desert)):
            for c in range(len(self.desert[0])):
                if self.desert[r][c] == 'c':
                    numSteps = 0
                    result = self.dfs_desert(r, c, gas, numSteps, [])
                    break
        return result"""
import collections


class reach_oasis:
    def solution2(self, matrix, gas):
        start = []
        end = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'c':
                    start = [i,j]
                elif matrix[i][j] == 'o':
                    end = [i,j]

        queue = collections.deque([start[0], start[1], gas, 1])
        visited = [start[0] + "," + start[1] + "," + gas + ",1"]
        dirs = [{-1, 0}, {0, 1}, {1, 0}, {0, -1}]
        while queue:
            node = queue.popleft()
            i, j, cur_gas, refill = node[0], node[1], node[2], node[3]
            if i == end[0] and j ==end[1]:
                return True
            if cur_gas == 0:
                continue
            for dir in dirs:
                x, y = i+dir[0], j+dir[1]
                if x<0 or x >= m or y < 0 or y >= n:
                    continue
                next_gas = cur_gas -1
                if matrix[x][y].isdigit() and refill == 1:
                    next_gas += matrix[x][y] - '0'
                if (x + "," + y + "," + next_gas + ",0") in visited:
                    continue
                queue.append([x, y, next_gas, 0])
        return False
                



























