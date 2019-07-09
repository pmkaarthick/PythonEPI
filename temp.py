# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
print("Hello World")

WHITE,BLACK = range(2)

Coordinate = collections.namedtuple('coordinate',('x','y'))



def search_maze(maze, s,e):
    def search_maze_helper(cur):
        if not (0<= cur.x<len(maze) and 0<=cur.y<len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y]=BLACK
        if cur == e:
            return True
        
        if any (
                map(search_maze_helper,
                    map(Coordinate,(cur.x-1,cur.x+1),cur.x,cur.x),(cur.y,cur.y,cur.y-1,cur.y+1))):
            return True
        del path[-1]
        return False
    
    path = []
    search_maze_helper(s)
    return path



#def search_maze(maze, s, e):
#
#    # Perform DFS to find a feasible path.
#    def search_maze_helper(cur):
#        # Checks cur is within maze and is a white pixel.
#        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])
#                and maze[cur.x][cur.y] == WHITE):
#            return False
#        path.append(cur)
#        maze[cur.x][cur.y] = BLACK
#        if cur == e:
#            return True
#
#        if any(
#                map(search_maze_helper,
#                    map(Coordinate, (cur.x - 1, cur.x + 1, cur.x, cur.x),
#                        (cur.y, cur.y, cur.y - 1, cur.y + 1)))):
#            return True
#        # Cannot find a path, remove the entry added in path.append(cur).
#        del path[-1]
#        return False
#
#    path = []
#    search_maze_helper(s)
#    return path
#
#x=[1, 0, 0]
#y=[0, 2]
#z=[0,1]
#search_maze(x,y,z)
print("Hello Karthick")