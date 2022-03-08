import test




def greeting(personalize='World'):
    return 'Hello ' + personalize


def shopping_list(items, oxfordRule=True):
    result = 'I need to get: '
    arrLength = len(items)
    for i in range(len(items)):
        if i == arrLength - 1:
            result += items[i]
        elif i == arrLength - 2:
            if oxfordRule == False:
                result += items[i] + ' and '
            else:
                result += items[i] + ', and '  
        else:
            result += items[i] + ', '        
    # import pdb; pdb.set_trace()   
    return result



# def some_function():
#     import pdb; pdb.set_trace()


# some_function()