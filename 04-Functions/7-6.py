def hide(card_number):
    add = []
    for i in range(len(card_number)):
        if i >= 2 and i <= 11:
            i = '*'
            add.append(i)
        else:
            add.append(card_number[i])
    
    return ''.join(add)
    
if __name__ == "__main__":
    print(hide("5290312400019022"))