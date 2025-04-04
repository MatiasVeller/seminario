def sort_key(player_stats):
    puntos = player_stats[1] * 3 + player_stats[2] - player_stats[3]
    return (puntos, player_stats[1], player_stats[2], - player_stats[3])  

def final_sort_key(player_stats):
    return player_stats[1]['Puntos']



