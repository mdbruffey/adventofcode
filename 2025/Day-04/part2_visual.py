import asyncio

from batgrl.app import App
from batgrl.gadgets.scroll_view import ScrollView
from batgrl.gadgets.text import Text
from collections import deque

def get_neighbors(loc, data):
    x, y = loc
    neighbors = []
    for dy in range(-1,2):
        for dx in range(-1,2):
            if x+dx >= 0 and y+dy >= 0 and x+dx < len(data[y]) and y+dy < len(data):
                if data[y+dy][x+dx] == "@" and (dx != 0 or dy != 0):
                    neighbors.append((x+dx, y+dy))
    return neighbors

def remove_rolls(removed, grid):
    for j, i in removed:
        grid.canvas["ord"][i][j] = ord(".")
    removed.clear()

with open("input.txt") as file:
    RAW = file.read()

data = RAW.split("\n")

class Visual(App):
    async def on_start(self):
        grid = Text()
        grid.set_text(RAW)
        sv = ScrollView(
            size_hint={"height_hint": 1.0, "width_hint": 1.0}, dynamic_bars=True
        )
        sv.view = grid
        self.add_gadget(sv)

        to_remove = deque()
        remove_set = set()
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "@" and len(get_neighbors((j,i), data)) < 4:
                    to_remove.append((j,i))
                    remove_set.add((j,i))
        count = 0
        removed = set()
        while len(to_remove):
            j,i = curr = to_remove.pop()
            data[i] = data[i][:j] + "." + data[i][j+1:]
            removed.add(curr)
            count += 1
            for neighbor in get_neighbors(curr, data):
                if neighbor not in remove_set and len(get_neighbors(neighbor, data)) < 4:
                    to_remove.append(neighbor)
                    remove_set.add(neighbor)
            if count%20 == 0:
                remove_rolls(removed, grid)
                await asyncio.sleep(1/60)
        remove_rolls(removed, grid)

Visual().run()