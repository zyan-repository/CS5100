# (a)
# first win: 1 3 4
# second win: 0 2

# When n = 5, the first player can change the number to 4, 2, 1. 
# Meanwhile, it become the other player's turn.
# We know when n = 2, the second player must be winning. So when n = 5, the first player must be winning.
# So, I can use a arrary to present first player's status:
#   status[1] = status[3] = status[4] = true
#   status[0] = status[2] = false
#   for i in range(5, n):
#     status[i] = (not status[i - 1]) or (not status[i - 3]) or (not status[i - 4])
# When status[i] = true, first player will win, otherwise the second one.

# (b)
status = [False] * 2025
status[1] = True
status[3] = True
status[4] = True
for i in range(5, 2025):
    status[i] = (not status[i - 1]) or (not status[i - 3]) or (not status[i - 4])
print(status[2024])
# True
# So when n = 2024, the first player will win.