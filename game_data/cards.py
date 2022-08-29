# Lucky!(если провал +2), Sure Gamble (Switch + on -), Daring Maneuver (если успех еще +2)
# Ritual Candles (+1 symbol), Crystal Pendulum (enter a number), Dark Prophecy (5 tokens),
# Defiance (nignore a token), Grotesque Statue (2 tokens instead 1), Grannie Orne (+1 or -1),
# 21 or Bust (игра в очко. интересная механика), Money Talks (че-то там с ресурсами),
# Snipe(symbols is 0), Nkosi Mabati: Enigmatic Warlock (sigil), Divination (succeed by 0),
# "Hit me!" (+1 token), Precious Memento: From a Former Life (+2 -2)

def crystal_pendulum_lvl0(result, tokens_value, chaos_bag, check):
        add_point = input('Add any point(s) if you want to correct your skill  ')
        if not add_point.isdigit():
            add_point = 0
        correction = int(add_point) + result
        abs_chaos_bag = [abs(i+correction) for i in tokens_value]
# auto-fail correction
        abs_chaos_bag.remove(99-correction)
        abs_chaos_bag.append(check)
        print(abs_chaos_bag)
        for_crystal_pendulum = {}
        for i in abs_chaos_bag:
            for_crystal_pendulum[i] = abs_chaos_bag.count(i)
        max = 1
        for i in for_crystal_pendulum.items():
            if max < i[1]:
                max = i[1]
                num = i[0]
        probe = round(max/len(chaos_bag), 2) * 100
        print(f'number for crystal pendulum = {num}, probability is {probe}%')


def Jacquilyne_Fine_special(pull_tokens):
#    result = skill - check
    pull_tokens = pull_tokens + 2
#    print(pull_tokens)
    tokens = []
    for i in range(pull_tokens):
        i = choice(chaos_bag)
        chaos_bag.remove(i)
        tokens.append(i)
    if not 'auto_fail' in tokens:
        for i in range(2):
            print(f'Tokens are {tokens}.' )
            cancelled = int(input(f'What token do you cancelled? press num from "1" to "{pull_tokens-i}": '))
            tokens.remove(tokens[cancelled-1])
        return tokens
    else:
        tokens = [i for i in tokens if not i == 'auto_fail']
        tokens.remove('auto_fail')
        return tokens

print(Jacquilyne_Fine_special(5))
