from collections import deque, defaultdict
# Commented out code below was used for question 1 which I implemented as a list rather than a deque
no_of_players = 429
last_marble_value = 7090100

marble_list = deque([0])         #[0]
#current_index = 1
players_scores = defaultdict(int)   #[0]*no_of_players
#current_player_index = 0

# for x in range(1, last_marble_value):
#   if x%23 != 0:
#     current_index = (current_index + 2)%len(marble_list)
#     marble_list.insert(current_index, x)
#   if x%23 == 0:
#     current_index = (current_index - 7)%len(marble_list)
#     value_removed = marble_list.pop(current_index)
#     players_scores[current_player_index] += x + value_removed
#   current_player_index = (current_player_index + 1)%no_of_players
#   #print(marble_list)

#   if x%10000 == 0:
#     print(x/10000)
# print(max(players_scores))

for x in range(1, last_marble_value):
  if x % 23 != 0:
    marble_list.rotate(1)
    marble_list.appendleft(x)
  else:
    marble_list.rotate(-7)
    players_scores[x % no_of_players] += x + marble_list.popleft()
    marble_list.rotate(1)

print(max(players_scores.values()))




