############## List Spinner

list_awal = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ]

# output: [[4, 8, 12, 16]
#         [3, 7, 11, 15],
#         [2, 6, 10, 14],
#         [1, 5, 9, 13]]
def counterClockwise(list_awal):
    angka = [[],[],[],[]]
    y = len(list_awal[0])-1
    for i in range(len(list_awal[0])):
        for j in range(len(list_awal[0])):
            angka[i].append(list_awal[j][y-i])
    return angka

print(counterClockwise(list_awal))


