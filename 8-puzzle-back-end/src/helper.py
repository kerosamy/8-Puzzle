from typing import List, Optional, Tuple


goal_state=(0, 1, 2, 3, 4, 5, 6, 7, 8)
def find_zero_index(state: Tuple[int]) -> int:
    return state.index(0)

def make_move(state: Tuple[int], move: str) -> Optional[Tuple[int, ...]]:
    new_state=list(state)
    zero_index=find_zero_index(state)
    if move=='U' and zero_index>2:
        idx=zero_index-3
    elif move=='D' and zero_index<6:
        idx=zero_index+3
    elif move=='L' and zero_index%3!=0:
        idx=zero_index-1
    elif move=='R' and zero_index%3!=2:
        idx=zero_index+1
    else:
        return None
    new_state[zero_index],new_state[idx]=new_state[idx],new_state[zero_index]
    return tuple(new_state)

def reconstruct_path(state: Tuple[int], parent_state: dict, parent_dir: dict) -> Tuple[List[str], List[Tuple[int]]]:
        path=[]
        steps=[]
        while parent_state[state] is not None:
            path.append(parent_dir[state])
            steps.append(state)
            state=parent_state[state]
        steps.append(state)
        path.reverse()
        steps.reverse()
        return path,steps
