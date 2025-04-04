def sort_key(player_stats):
    return (player_stats[1] * 3 + player_stats[2] - player_stats[3])


def final_sort_key(player_stats):
    return player_stats[1]['Puntos']


def rankings(rounds):
    text = "Jugador  Kills Asistencias   Muerte  MVPs  Puntos"
    final_stats = {}

    # Iteración por ronda
    for round in "01234":
        round_stats = []
        mvp = ""
        max_score = 0
        actual = rounds[int(round)]
        round = int(round) + 1
        print(f"Ranking ronda {round}:")
        print(text)
        print(f"{'-':-^50}")
        
        # Iteración por jugador en la ronda actual
        for player in actual:
            # Guardo la información del jugador en la ronda actual
            kills = actual[player]['kills']
            assists = actual[player]['assists']
            
            if actual[player]['deaths']:
                deaths = 1
            else:
                deaths = 0
            
            # Agrego la información del jugador actual a mi lista de estadísticas de la ronda actual
            round_stats.append((player, kills, assists, deaths))
            score = (kills * 3) + assists - deaths
            
            # Verifico si el puntaje calculado del jugador actual de la ronda actual es el mayor de todos hasta el momento para registrar el mvp        
            if score > max_score:
                max_score = score
                mvp = player
            
            # Si el jugador todavía no apareció nunca en el diccionario que va a contener los resultados totales del conjunto de rondas, lo inicializo
            if player not in final_stats:
                final_stats[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0, 'Puntos': 0}
            
            # Cuando ya esté, incremento sus estadísticas totales en base a las de la ronda actual
            final_stats[player]['kills'] += kills
            final_stats[player]['assists'] += assists
            final_stats[player]['deaths'] += deaths
            final_stats[player]['Puntos'] += score
        
        # Por cada ronda, en el registro final de estadísticas se incrementará en una unidad la cantidad de veces que el jugador que fue seleccionado como mvp fue MVP
        if mvp:
            final_stats[mvp]['MVPs'] += 1
        
        # Por cada ronda, ordeno en orden decreciente por los puntos totales
        round_stats.sort(key=sort_key, reverse=True)
        
        # Se recorre la lista ya ordenada y va mostrando los datos de cada jugador en la ronda actual de manera descendente
        # :<número alinea hacia la izquierda y lo ajusta a un ancho de número caracteres, termina completando con espacios
        for player, kills, assists, deaths in round_stats:
            print(f"{player:<8} {kills:<6} {assists:<11} {deaths:<7} {final_stats[player]['MVPs']:<5} {final_stats[player]['Puntos']:<6}")
        
        print(f"{'-':-^50}")

    print("Ranking final: ")
    print(text)
    print(f"{'-':-^50}")
    
    # .items() convierte el diccionario en una lista de tuplas llevándolo a la forma (player, stats)
    # final_sort_key y reverse para determinar el orden de manera descendente en base a los puntos
    final_rank = sorted(final_stats.items(), key=final_sort_key, reverse=True)
    
    for player, stats in final_rank:
        print(f"{player:<8} {stats['kills']:<6} {stats['assists']:<11} {stats['deaths']:<7} {stats['MVPs']:<5} {stats['Puntos']:<6}")
    
    print(f"{'-':-^50}")
