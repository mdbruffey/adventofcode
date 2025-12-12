import time
import heapq
import itertools

def is_contained(c1, c2, edges):
    x1, y1 = c1
    x2, y2 = c2
    c3 = (x1, y2)
    c4 = (x2, y1)

    # The four sides. The directions aren't really true necessarily, 
    # but it doesn't really matter
    sides = [
        (x1,x1,y1,y2), # "left"
        (x1,x2,y1,y1), # "top"
        (x2,x2,y1,y2), # "right"
        (x1,x2,y2,y2), # "bottom"
    ]
    for side in sides:
        for edge in edges:
            if intersects(side, edge):
                return False
    if is_outside(c3, edges) or is_outside(c4, edges):
        return False
    
    return True

def intersects(side, edge):
    if side[0] == side[1]: #side is vertical
        return (
            edge[2] == edge[3] and #edge is horizontal
            edge[2] > min(side[2:]) and edge[2] < max(side[2:]) and #edge y-value is within the y-range of the side
            side[0] > min(edge[:2]) and side[0] < max(edge[:2]) #side x value is within the x-range of the edge
        )
               
    else: #side is horizontal
        return (
            edge[0] == edge[1] and #edge is vertical
            edge[0] > min(side[:2]) and edge[0] < max(side[:2]) and #edge x value is within the x-range of the side
            side[2] > min(edge[2:]) and side[2] < max(edge[2:]) #side y value is within the y-range of the edge
        )
    
def is_outside(c, edges):
    x, y = c
    intersections = [0,0,0,0]
    #I'm just going to look in all four directions. If I don't intersect any edges in a direction, the point is outside
    #look right
    for edge in edges:
        #check if there are any intersections to the right of the point
        if edge[0] >= x and edge[0] == edge[1] and max(edge[2:]) >= y and min(edge[2:]) <= y:
            intersections[0] += 1
        #check if there are any intersections to the left of the point
        elif edge[0] <= x and edge[0] == edge[1] and max(edge[2:]) >= y and min(edge[2:]) <= y:
            intersections[1] += 1
        #check if there are any intersections above the point
        elif edge[2] >= y and edge[2] == edge[3] and max(edge[:2]) >= x and min(edge[:2]) <= x:
            intersections[2] += 1
        #check if there are any intersections below the point
        elif edge[2] <= y and edge[2] == edge[3] and max(edge[:2]) >= x and min(edge[:2]) <= x:
            intersections[3] += 1
    return 0 in intersections

def part1(vertices):
    vals = [(sum(vertex), vertex) for vertex in vertices]
    c1 = heapq.nsmallest(1, vals, key=lambda x: x[0])[0][1]
    c2 = heapq.nlargest(1, vals, key=lambda x: x[0])[0][1]
    area = (abs(c2[0]-c1[0])+1)*(abs(c2[1]-c1[1])+1)
    return area

def part2(vertices):
    edges = set()
    for i in range(len(vertices)):
        curr = vertices[i]
        next = vertices[i+1] if i+1 < len(vertices) else vertices[0]
        #edge = (x1,x2,y1,y2)
        edge = (curr[0], next[0], curr[1], next[1])         #    +-------------+  
        edges.add(edge)                                     # (x1,y1)       (x2,y2)
    largest = 0
    for c1,c2 in itertools.combinations(vertices, 2):
        area = (abs(c2[0]-c1[0])+1)*(abs(c2[1]-c1[1])+1)
        #if area is smaller than the largest found, no reason to check containment
        if area <= largest or c1[0] == c2[0] or c1[1] == c2[1]: 
            continue
        if is_contained(c1,c2,edges):
            largest = area
    return largest
    

with open("input.txt") as file:
    data = [tuple(map(int, line.split(","))) for line in file.read().split("\n")]

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")