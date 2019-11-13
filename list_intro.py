#  how do i define a list?

grocery_list = ['egg','milk','bread']

# how do i get one item from the list
len(grocery_list)
#  python list indexes start from 0.
#  to add stuff to the list
# grocery_list.append('beer')
# grocery_list
# ['egg', 'milk', 'bread', 'beer']

#  to access multiple item
# grocery_list[0:3] # slicing 
# ['egg', 'milk', 'bread']

# what is itteration in list

# for item in grocery list:
#     print(f"you need to buy{item}")

# after the loop ends the loop variable is still exist and holds the last assignment

# grocery_list[1]
# 'milk'
# >>> grocery_list[1] = ' Almond milk'
# >>> grocery_list
# ['egg', ' Almond milk', 'bread', 'beer']
# slice to access multiple items
# replacing multiple list item
for item in grocery_list:
    index = 0
    while index < len(grocery_list)
       print(grocery_list[index])
       grocery_list[index] ="cheese"
       index += 1

#  for loop does not access for index
#  to update a list use while loop
# to replace the items you have to know the name of LHS

#  combine list

# grocery_list.extends(snacks)
#  concatinate a list grocery list + snacks
# to change from string to list - magic_word is string - list(magic_word)
# join  .join(magic_list)
#  how do i creat a lists?
# chris_dir = ['jonathan', 'tedge']
# sean_dir = ['evan', 'alleric']
# all_dir = [chris_dir,sean_dir]
# all_dir[0]-jhonatan, tedge
# all_dir[0][1]-tedge-from outer to inner list
# nested for Loop