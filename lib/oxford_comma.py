# import ipdb

def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    if len(items) == 2:
        return " and ".join(items)
    elif len(items) > 2:
        except_last =  ", ".join(items[0:len(items) - 1])
        return except_last + f', and {items[-1]}'
        
# items = ['kiwi', 'durian', 'starfruit', 'mangos', 'dragon fruits']

# ipdb.set_trace()
