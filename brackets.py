def brackets(expression):
    base = [int(expression[i]) for i in range(0, len(expression), 2)]
    pre_values = base[:]

    operation_length = 3
    shift = 0
    while operation_length <= len(expression):
        while (shift + 1)*operation_length <= len(expression):
            start_ind = shift*operation_length
            end_ind = (shift + 1)*operation_length -1
            cur_values = []
            for i in range(len(pre_values)):
                back_operation = i*(operation_length - 2) - 1
                front_operation = i*(operation_length - 2) + 1


    
    operation_length += 2

brackets("1*0-0+1")