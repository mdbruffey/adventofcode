import time
import heapq
import itertools

def is_contained(c1, c2, edges):
    x1, y1 = c1
    x2, y2 = c2

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
    return True

def intersects(side, edge):
    if side[0] == side[1]: #side is vertical
        return (
            edge[2] == edge[3] and #edge is horizontal
            edge[2] >= min(side[2:]) and edge[2] <= max(side[2:]) and #edge y-value is within the y-range of the side
            side[0] >= min(edge[:2]) and side[0] <= max(edge[:2]) and #side x value is within the x-range of the edge
            not (side[2] == edge[2] or side[3] == edge[2])            #side does not terminate on the edge
        )
               
    else: #side is horizontal
        return (
            edge[0] == edge[1] and #edge is vertical
            edge[0] >= min(side[:2]) and edge[0] <= max(side[:2]) and #edge x value is within the x-range of the side
            side[2] >= min(edge[2:]) and side[2] <= max(edge[2:]) and #side y value is within the y-range of the edge
            not (side[0] == edge[0] or side[1] == edge[0])            #side does not terminate on the edge
        )

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