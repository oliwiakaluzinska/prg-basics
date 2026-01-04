def occurs(number, array):
    for i in array:
        if i != number:
            x = False
        else:
            x = True
            return x
    
        
if __name__ == "__main__":
    print(occurs(13 ,[15, 38, 7, 23, 14]))