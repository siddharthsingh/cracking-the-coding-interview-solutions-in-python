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
    """
    This function finds the path from the top left corner of the matrix to the bottom right
    It uses a BFS approach where on each position of the matrix that we are at we find the next valid cells reachable
    from it.
    Time complexity would be O(m,n) Where mxn is size of the matrix
    space complexity would be O(m+n) (because of the queue) if we modify the original matrix to keep track of already
    visited cells and also not keep a track of parent relation(ie the path).
    If we are not allowed to change the original matrix the space complex or if we need to keep track of the paths( ie
    which node is the parent of the each node) the space complexity would be O(mn)
    :return:
    """
    # To-Do: can we use A* or bidirectional BFS for this problem?
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
            if valid_nieghbour[0] == n - 1 and valid_nieghbour[1] == m - 1:
                print("reached")
                return
find_way()

