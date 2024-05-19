import random

# 全局变量，用于存储地图数据
maze = None

def generate_maze(rows, cols,callback=None):
    global maze_data

    # 生成迷宫数据
    maze = []
    for i in range(rows):
        maze.append([])
        for j in range(cols):
            maze[i].append(1 if random.random() < 0.4 else 0)

    # 设置入口和出口
    entranceX = 2
    entranceY = 2
    exitX = cols - 3
    exitY = rows - 3
    maze[entranceY][entranceX] = 0
    maze[exitY][exitX] = 0

    # 将地图数据存储到全局变量中
    return  {
        'type':'maze',
        'maze': maze,
        'entranceX': entranceX,
        'entranceY': entranceY,
        'exitX': exitX,
        'exitY': exitY
    }
    
    # print(maze_data)

