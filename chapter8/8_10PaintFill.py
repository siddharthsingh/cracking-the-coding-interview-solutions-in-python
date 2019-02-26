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

# def using_dfs(r,c):
#     if r>=len(grid):
#         return
#     using_dfs(r+1,c)
#     for i

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

find_way()
print(grid)

