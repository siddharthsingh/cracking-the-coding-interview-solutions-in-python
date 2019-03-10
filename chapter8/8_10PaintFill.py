import queue
grid = [
    [ 0, 0, 0,-1,0,0],
    [ 0,-1, 0, 0,0,0],
    [ 0, 0,-1, 0,0,0],
    [-1, 0, 0, 0,0,0],
    [ 0, 0, 0, 0,0,0],

]
n = (len(grid))
m = (len(grid[0]))


"""
This is a simple graph traversla problem. You can solve it using BFS or DFS. 
The time complexity would be same for both which is O(mn) as in the worst case all the cells of the matrix might need
to be colored.
"""


def using_dfs(r,c, old_color, new_color):
    # if row or column goes beyond bounds of matrix return
    if r<0 or c<0 or r>len(grid)-1 or c > len(grid[0])-1:
        return
    if grid[r][c] == old_color:
        grid[r][c] = new_color
        using_dfs(r-1,c,old_color,new_color) #go up
        using_dfs(r+1,c,old_color,new_color) #go down
        using_dfs(r,c-1,old_color,new_color) #go left
        using_dfs(r,c+1,old_color,new_color) #go right


def get_valid_neighbours(point):
    ans = []
    x = point[0]
    y = point[1]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == j or (i == 1 and j == -1) or (i == -1 and j == 1) or x+i<0 or y+j<0 or x+i>=n or y+j>=m or grid[x+i][y+j] == -1:
                continue
            ans.append((x+i,y+j))

    return ans

parent = {}


def find_way():
    q = queue.Queue()
    q.put((0,0))
    global grid
    grid[0][0] = -1
    while not q.empty():
        point = q.get()
        valid_nieghbours = get_valid_neighbours(point)
        for valid_nieghbour in valid_nieghbours:
            parent[valid_nieghbour] = point
            grid[valid_nieghbour[0]][valid_nieghbour[1]] = -1
            q.put(valid_nieghbour)

# find_way()
using_dfs(0,0,0,2)
print(grid)

