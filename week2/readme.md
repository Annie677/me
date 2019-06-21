TODO: Reflect on what you learned this week and what is still unclear.

The "def" means defining the function and then the things inside the () is arguement. 
so 
def add_1(a_number):
    the_answer = a_number + 1
    return the_answer
the "Adding one process" is defined as a function "add_1" 
a_number is more like a "x" unknown number 
therefore, the answer is equal to x + 1 = a_number + 1

In the end, the "return the_answer" gives the answer 

The string decides the type of texts. The command 
a_string.upper()
let me to change the texts from lowercase into uppercase.

If I need to add more texts behind the string, the texts need to be inside the ""
The string can only add number behind when the number is turned into a string. Therefore
a_string + str(a_number)

The inyerpunction in coding is supper important! I tried many times which all gave me the red color. That all because of the [] wasn't completed. 

"For loop" is able to select the items from a list or string. 
".append" command will provide a new list for showing the selected items.

To create a list with two arguments for example:
item = "A", the amount of items = 3
then 
list = [item] * the_amount_of_items
ps, it also works for the list * list or list * number


I didn't quite get the loops_3 question in exercise3, so I create 10 lists which doesn't looks like a good way to solve this problem. I have no idea how to create 10 repeated lists with the range(10). :(
    
The "range" example
for idx in range(5):
    print (indx)

This will show, "[0,1,2,3,4]"

2. for idx in range(len(my_list)):

3. 
my_list = [10, 23, 48,99,102]
idx = 0
    while idx < len(my_list):
    print (my_list[idx])
    idx = idx + 1

4. list(range(5))
this will show " [0, 1, 2, 3, 4]

list (range(1,5))
this will show "[1, 2, 3, 4]

list(range(10,20,2))
this will show:
[10, 12, 14, 18]