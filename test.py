# row_width = [3, 5, 7, 9]
# # l = [[j for j in range(row_width[i])] for i in range(len(row_width))]
#
# l = []
#
# for i in range(len(row_width)):
#     res = []
#     for j in range(row_width[i]):
#         res.append(j)
#     l.append(res)
#
# for i in range(len(l)):
#     res = ""
#     for j in range(len(l[i])):
#         res += str(l[i][j])
#     print(res)

for i in range(4, -1, -2):
    print(i)