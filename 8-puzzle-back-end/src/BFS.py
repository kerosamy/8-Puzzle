from collections import deque
import time
from typing import List
from helper import *

class BFS:
    def __init__(self):
        self.total_cost: int = 0
        self.nodes_expanded: int = 0
        self.search_depth: int = 0
        self.running_time: float = 0.0  # in ms
        self.path_to_goal: List[str] = []  # like U, D, L, R
        self.max_ram_use: float = 0.0
        self.steps: list[tuple]=[]
        self.depth: map = {}
        self.parent_dir: map = {} 
        self.parent_state: map = {} 
        self.visited: set = set ()

    def solve(self, matrix: List[List[int]])-> List[int]:
        start_time=time.time()
        initial_state=tuple(sum(matrix, []))
        self.depth[initial_state]=0
        self.parent_dir[initial_state]=None
        self.parent_state[initial_state]=None
        self.search_depth=0
        found_goal= False
        queue=deque()
        queue.append(initial_state)
        self.visited.add(initial_state)

        while queue and not found_goal:
            current_state=queue.popleft()
            current_depth=self.depth[current_state]
            if current_depth>self.search_depth:
                self.search_depth=current_depth
            self.nodes_expanded+=1
            if current_state==goal_state:
                self.total_cost=self.depth[current_state]
                self.path_to_goal,self.steps=reconstruct_path(current_state,self.parent_state,self.parent_dir)
                found_goal= True
                break
            for move in ['U','D','L','R']:
                new_state=make_move(current_state, move)
                if new_state and new_state not in self.visited and new_state not in queue:
                    queue.append(new_state)
                    self.visited.add(new_state)
                    self.parent_state[new_state]=current_state
                    self.parent_dir[new_state]=move
                    new_depth=self.depth[current_state]+1
                    self.depth[new_state]=new_depth
        end_time=time.time()
        self.running_time=(end_time-start_time)*1000
        return self.path_to_goal

# puzzle = [
#     [1, 2, 5],
#     [3, 4, 0],
#     [6, 7, 8]
# ]

puzzle = [
    [1, 0, 2],
    [7, 5, 4],
    [8, 6, 3]
]



solver = BFS()
path = solver.solve(puzzle)

print("Path to goal:", path)
print("states steps:" , solver.steps)
print("Nodes expanded:", solver.nodes_expanded)
print("Search depth:", solver.search_depth)
#print("depth arr", solver.depth)
print("Total cost:", solver.total_cost)
print("Running time (ms):", solver.running_time)




       
        