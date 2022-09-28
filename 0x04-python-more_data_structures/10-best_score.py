def best_score(a_dictionary):
    if len(a_dictionary) > 0:
        score_list = []
        for i in a_dictionary:
            score_list.append(a_dictionary[i])
        y = sorted(score_list)[-1]
        return(y)
    else:
        return None
