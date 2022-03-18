# create list of odd numbers to the power of 3
cub_list = []

for i in range(1000):
    if i % 2 != 0:
        cub_list.append(i ** 3)


# function for digit sum of number
def sum_num_list(number):
    # convert number to string and create list
    a = str(number)
    b = []
    for j in a:
        b.append(j)
    # convert list of strings to digits
    c = []
    for j in b:
        j = int(j)
        c.append(j)
    # make sum of all digits from list
    result = 0
    for n in c:
        result += n

    return result


# using sum_num_list() create list of sums
cub_list1 = []
for i in cub_list:
    cub_list1.append(sum_num_list(i))

# create list with //7 numbers
cub_list2 = []
for i in cub_list1:
    if i % 7 == 0:
        cub_list2.append(i)

# using only arithmetics calculate sum of cub_list2
result1 = 0
for i in cub_list2:
    result1 += i

print(result1)

# add 17 to each element of the list
cub_list3 = []
for i in cub_list2:
    cub_list3.append(i + 17)

# calculate same sum as above
cub_list4 = []
for i in cub_list3:
    cub_list4.append(sum_num_list(i))

cub_list5 = []
for i in cub_list4:
    if i % 7 == 0:
        cub_list5.append(i)

print(sum(cub_list5))
