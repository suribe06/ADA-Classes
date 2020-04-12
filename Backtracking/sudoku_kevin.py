from sys import stdin
global call_count
call_count = 0

def compute_move(S, r, c):
    ans, i = set(str(x) for x in range(1, 10)), 0
    fr, fc = r-(r%3), c-(c%3)
    while len(ans) != 0 and i != 9:
        if S[r][i] != '.':
            ans.discard(S[r][i])
        if S[i][c] != '.':
            ans.discard(S[i][c])
        if S[fr+(i//3)][fc+(i%3)] != '.':
            ans.discard(S[fr+(i//3)][fc+(i%3)])
        i += 1
    return list(ans)

def solve(S, r, c, p):
    global call_count
    call_count += 1
    ans = None
    if p == 0:
        ans = True
    else:
        nr, nc = r, c+1
        if nc == 9:
            nr, nc = nr + 1, 0
            if S[r][c] == '.':
                move = compute_move(S, r, c)
                ans, i = False, 0
                while not(ans) and i != len(move):
                    S[r][c] = move[i]
                    ans = solve(S, nr, nc, p-1)
                    i += 1
                if not(ans):
                    S[r][c] = '.'
            else:
                ans = solve(S, nr, nc, p)
    return ans

def main():
    global call_count
    line = stdin.readline()
    while len(line) != 0:
        S = list()
        row = [x for x in line.strip()]
        S.append(row)
        for i in range(8):
            row = [x for x in stdin.readline().strip()]
            S.append(row)
        pnding = 0
        for r in range(9):
            for c in range(9):
                if S[r][c] == '.':
                    pending += 1
        call_count = 0
        ans = solve(S, 0, 0, pending)
        if ans:
            print("\n".join([''.join(x) for x in S]))
        else:
            print("No solution")
        print("recursive calls = {0}".format(call_count))
        line = stdin.readline()

main()
