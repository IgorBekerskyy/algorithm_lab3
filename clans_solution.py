def form_clans(list_of_pairs):
    clans = []
    if len(list_of_pairs)!=0:
        for pair in list_of_pairs:
            if pair[0]==0 or pair[1]==0:
                continue
            else:
                clans.append([pair[0], pair[1]])
                break
        i = 0
        for pair in list_of_pairs:
            if pair[0]==0 or pair[1]==0:
                continue
            if i == 0:
                i += 1
                continue
            for clan in clans:
                if pair[0] in clan:
                    clan.append(pair[1])
                    break
                elif pair[1] in clan:
                    clan.append(pair[0])
                    break
                continue
            else:
                clans.append([pair[0], pair[1]])
    return clans


def general_amount(clan):
    girls = 0
    for clan_member in clan:
        if clan_member % 2 == 0:
            girls += 1
    boys = len(clan) - girls
    return girls, boys


def solution(clans):
    boys_in_one_clan = [general_amount(clan)[1] for clan in clans]
    girls_in_one_clan = [general_amount(clan)[0] for clan in clans]
    boys = 0
    girls = 0
    sum = 0
    for boy in boys_in_one_clan:
        boys += boy
    for girl in girls_in_one_clan:
        girls += girl
    for clan in clans:
        sum += general_amount(clan)[0] * general_amount(clan)[1]
    return boys * girls - sum