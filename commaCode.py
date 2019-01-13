def commaCode(in_list):

    if (len(in_list) == 1):
        print(in_list[0])
    elif (len(in_list) == 0):
        print('Your list is empty.')
    else:
        for i in range(len(in_list) -1):
            print(in_list[i] + ', ', end='')
    
    if (len(in_list) > 1):
        print('and ' + in_list[-1] + '.')

            
input_list = ['apples', 'bananas', 'tofu', 'cats']
commaCode(input_list)

    

