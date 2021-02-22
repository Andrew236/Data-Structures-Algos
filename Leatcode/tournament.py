
def tournamentWinner(competitions, results):
    # Write your code here.
    result_dict = {}
    count = 0
    index = 0
    team = ''
    length = len(competitions)

    while index < length:
        if results[index] == 0:
            team = competitions[index][1]
            if team in result_dict:
                result_dict[team] += 1
            else:
                result_dict[team] = 1
            index += 1
        else:
            team = competitions[index][0]
            if team in result_dict:
                result_dict[team] += 1
            else:
                result_dict[team] = 1
            
            index += 1

    print(max(result_dict, key=result_dict.get))



tournamentWinner([["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]], [0, 1, 1])