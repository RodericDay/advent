A, *B = text.split('\n\n')
calls = [int(n) for n in A.split(',')]
boards = [[[int(n) for n in ln.split()] for ln in b.splitlines()] for b in B]

win_scores = []
for n in calls:
    pending = []
    for board in boards:
        board[:] = [[None if m == n else m for m in row] for row in board]
        win_rows = any(all(n is None for n in row) for row in board)
        win_cols = any(all(n is None for n in col) for col in zip(*board))
        if win_cols or win_rows:
            total = sum(sum(n for n in row if n is not None) for row in board)
            win_scores.append(total * n)
        else:
            pending.append(board)
    boards = pending

ans1 = win_scores[0]
ans2 = win_scores[-1]
