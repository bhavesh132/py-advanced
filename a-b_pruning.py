def alphabeta(depth, nodeIndex, isMax, scores, alpha, beta, h):
    if depth == h:
        return scores[nodeIndex]
    
    if isMax:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth+1, nodeIndex * 2 + i, False, scores, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
            return best
    else:
        worst = float('inf')
        for i in range(2):
            val = alphabeta(depth+1, nodeIndex * 2 + i, True, scores, alpha, beta, h)
            worst = min(worst, val)
            beta = min(beta, worst)
            if beta <= alpha:
                break
        return worst