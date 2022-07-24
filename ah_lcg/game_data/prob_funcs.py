def done_percent(result, chaos_bag_values, num=0):
    done = [i+result for i in chaos_bag_values if i+result >= num]
    count_of_tokens = len(chaos_bag_values)
    success = len(done)
    done_procent = round((success/count_of_tokens) * 100)
    return done_procent


def counting_points_cycle(result, chaos_bag_values, num=0):
    done_percent_list = []
    for add in range (1, 20): #counting points cycle
        count_of_tokens = len(chaos_bag_values)
        new_result = result + add
        new_done = [i+new_result for i in chaos_bag_values if i+new_result >= num]
        new_success = len(new_done)
        new_done_percent = round((new_success/count_of_tokens) * 100)
        if new_done_percent > 0:
            done_percent_list.append((add, new_done_percent)) 
        if new_done_percent >= round((count_of_tokens-1) / count_of_tokens * 100):
            return done_percent_list


#print(done_percent(0, [1,2,3,4,5], 2))
#print(f'If you add {add} point(s), done_procent is {new_done_percent}%')

print(counting_points_cycle(2, [-1,-2,-3,-4,-5, -5, -2, -6, -2, -1], 0))