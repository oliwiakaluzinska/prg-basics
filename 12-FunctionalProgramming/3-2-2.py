sentence = 'I completely agree with you'
result = list(map(lambda no:len(no) , sentence.split()))
print(result)