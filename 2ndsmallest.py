Numbers = [2,2,15,14,7,71,52,209,551]

def sort(array):
    Numbers = array
    for i in range(len(Numbers)-1, 0, -1):
        for j in range(i):
            if Numbers[j] > Numbers[j+1]:
                Numbers[j], Numbers[j+1] = Numbers[j+1], Numbers[j]
    return Numbers

sorted_array = sort(Numbers)

smallest = sorted_array[0]
for i in range(1,len(sorted_array)-1,1):
    if sorted_array[i] > smallest:
        print("2nd smallest ", sorted_array[i])
        break

