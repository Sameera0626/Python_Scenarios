Task:
And if you have dictionay in which key will be playersname and value will the runs they score ..write the python code to write and fetch the maximum runs players scores??

#sample dictionary of players and their runs
players_score={
  "Kohli" : 85,
  "Sachin": 72,
  "Rohit Sharma" : 99,
  "Rahul" : 45,
  "hardik" : 60
}

#get the maximun run player scored
max_player=max(players_score,key=players_score)
max_score=players_score[max_player]

print(f"the player with maximum run is {max_player} with{max_score} runs")
