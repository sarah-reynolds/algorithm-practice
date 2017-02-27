

# with open('numbers.txt') as file:
# 	file_contents_as_list = file.readlines()
# 	el = str(file_contents_as_list[0])
# 	print el
# 	sp = el.split()
# 	print int(el)
# 	sum = 0
# 	for i in str(el):
# 		print i
# 		sum = sum + i
# 	print sum

with open("numbers.txt") as file:
   file_contents_as_list = file.readlines();

   # print file_contents_as_list
new_list = [];
for line in file_contents_as_list:
   split_line = line.split()
   # print split_line
   for num in split_line:
       if int(num):
           new_list.append(int(num));
# print new_list
doubley_new_list = [];
for line in new_list:
   for digit in str(line):
       doubley_new_list.append(int(digit))

# print sum(doubley_new_list);

# =========

# with open('numbers.txt') as file:
#    file_contents_as_list = file.readlines()
# sum_per_line = []
# for line in file_contents_as_list:
#     # print line;
#     sum_of_line = 0
#     for digit in line:
#         # print digit
#         if digit.isdigit():
#             sum_of_line += int(digit)
#     # print sum_of_line
#     sum_per_line.append(sum_of_line)
# print sum_per_line
# numsum = (sum(sum_per_line))
# print numsum;