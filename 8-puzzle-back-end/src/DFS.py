from typing import List

class DFS:
    def __init__(self):
        self.total_cost: int = 0
        self.nodes_expanded: int = 0
        self.search_depth: int = 0
        self.running_time: float = 0.0  # in ms
        self.path_to_goal: List[str] = []  # like U, D, L, R
        self.max_ram_use: float = 0.0
        self.steps: List[List[List[int]]] = []

    def solve(self, matrix: List[List[int]]) -> List[int]:
        print("Kero was here")

