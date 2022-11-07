class desertTraversal():
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
        return result
