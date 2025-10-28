from heapq import heapify
import heapq
import time
from typing import List
from helper import *

class A:
    def __init__(self, Heuristic):
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
        self.g: dict = {}
        self.Heuristic=Heuristic
    
    def calcuate_distance(self, state):
        distance=0
        for i in range(1,9):
            current_index=state.index(i)
            goal_index=goal_state.index(i)
            x1,y1=divmod(current_index,3)
            x2,y2=divmod(goal_index,3)
            if self.Heuristic=="manhattan":
                distance+=abs(x1-x2)+abs(y1-y2)
            elif self.Heuristic=="euclidean":
                distance+=((x1-x2)**2+(y1-y2)**2)**0.5
        return distance
            
    def solve(self, matrix: List[List[int]])-> List[int]:
        start_time=time.time()
        initial_state=tuple(sum(matrix, []))
        heap=[]
        g0=0
        h0=self.calcuate_distance(initial_state)
        heapq.heappush(heap,(g0+h0,g0,initial_state))
        self.g[initial_state]=0
        self.depth[initial_state]=0
        self.parent_dir[initial_state]=None
        self.parent_state[initial_state]=None
        found_goal=False

        while heap and not found_goal:
            f,g,current_state=heapq.heappop(heap)
            if g>self.g.get(current_state,float('inf')):
                continue
            self.nodes_expanded+=1
            self.visited.add(current_state)
            self.search_depth=max(self.search_depth,g)
            if current_state==goal_state:
                self.path_to_goal,self.steps=reconstruct_path(current_state,self.parent_state,self.parent_dir)
                self.total_cost=g
                found_goal= True
                break
            for move in ['U','D','L','R']:
                new_state=make_move(current_state, move)
                if not new_state:
                    continue
                new_g=self.g[current_state]+1
                h=self.calcuate_distance(new_state)
                new_f=new_g+h
                if new_g<self.g.get(new_state,float('inf')):
                    self.g[new_state]=new_g
                    heapq.heappush(heap,(new_f,new_g,new_state))
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

solver = A('euclidean')
path = solver.solve(puzzle)

print("Path to goal:", path)
print("states steps:" , solver.steps)
print("Nodes expanded:", solver.nodes_expanded)
print("Search depth:", solver.search_depth)
#print("depth arr", solver.depth)
print("Total cost:", solver.total_cost)
print("Running time (ms):", solver.running_time)