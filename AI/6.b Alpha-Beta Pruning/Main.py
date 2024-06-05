# Python3 program to demonstrate
# working of Alpha-Beta Pruning

# Initial values of Alpha and Beta
MAX, MIN = 1000, -1000

# Returns optimal value for the current player
# (Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminating condition, i.e.,
    # leaf node is reached
    if depth == 3:
        print(f"Leaf Node: [{depth}, {nodeIndex}] Value: {values[nodeIndex]}")
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN
        print(f"Max Node: [{depth}, {nodeIndex}] Alpha: {alpha} Beta: {beta}")
        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)  # Alpha Beta Pruning
            print(f"Max Node: [{depth}, {nodeIndex}] Updated Best: {best} Alpha: {alpha} Beta: {beta}")
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        print(f"Min Node: [{depth}, {nodeIndex}] Alpha: {alpha} Beta: {beta}")
        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning
            print(f"Min Node: [{depth}, {nodeIndex}] Updated Best: {best} Alpha: {alpha} Beta: {beta}")
            if beta <= alpha:
                break
        return best

# Driver Code
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))

