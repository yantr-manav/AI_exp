N = 3  # Number of disks


class State:
    def __init__(self):
        # Initialize 3 pegs with N disks
        self.pegs = [[0] * N for _ in range(3)]
        self.top = [-1, -1, -1]  # Initialize tops of each peg to -1


def initialize_state(state):
    for i in range(3):
        state.top[i] = -1
    for i in range(N):
        state.pegs[0][i] = N - i
        state.top[0] = i


def display_state(state):
    print("\nCurrent State:")
    for i in range(N - 1, -1, -1):
        for j in range(3):
            if i <= state.top[j]:
                print(f" {state.pegs[j][i]} ", end="")
            else:
                print(" | ", end="")
        print()
    print("-------------------\n A B C \n")


def is_valid_move(state, from_peg, to_peg):
    if state.top[from_peg] == -1:
        return False
    if state.top[to_peg] == -1:
        return True
    return state.pegs[from_peg][state.top[from_peg]] < state.pegs[to_peg][state.top[to_peg]]


def move_disk(state, from_peg, to_peg):
    state.top[to_peg] += 1
    state.pegs[to_peg][state.top[to_peg]
                       ] = state.pegs[from_peg][state.top[from_peg]]
    state.top[from_peg] -= 1


def evaluate_heuristic(state):
    score = 0
    for i in range(state.top[2] + 1):
        if state.pegs[2][i] == i + 1:
            score += 1
    return score


def hill_climbing(state):
    display_state(state)
    while evaluate_heuristic(state) < N:
        best_state = state
        best_score = evaluate_heuristic(state)
        from_peg, to_peg = -1, -1
        for i in range(3):
            for j in range(3):
                if i != j and is_valid_move(state, i, j):
                    new_state = State()
                    new_state.__dict__ = state.__dict__.copy()  # Deep copy state
                    move_disk(new_state, i, j)
                    new_score = evaluate_heuristic(new_state)
                    if new_score > best_score:
                        best_state = new_state
                        best_score = new_score
                        from_peg = i
                        to_peg = j
        if best_score == evaluate_heuristic(state):
            print("\nLocal Maxima reached, no further progress possible.\n")
            break
        print(
            f"\nMoving disk from Peg {chr(ord('A') + from_peg)} to Peg {chr(ord('A') + to_peg)}\n")
        state = best_state
        display_state(state)
    print("\nGoal State Reached!\n")


def main():
    state = State()
    initialize_state(state)
    hill_climbing(state)


if __name__ == "__main__":
    main()
