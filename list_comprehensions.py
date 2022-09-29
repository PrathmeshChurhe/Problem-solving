Problem Statement : Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.



#  this code shows the list and its all functions based on what the list survives
# 1. Brute force method
# 2. Optimal method

1. Brute Force method (me) -

    if __name__ == '__main__':
    N = int(input())
    var=[]
    var.insert(0,5)
    var.insert(1,10)
    var.insert(0,6)
    print(var)
    var.remove(6)
    var.append(9)
    var.append(1)
    var.sort()
    print(var)
    var.pop()
    var.reverse()
    print(var)  
    
2.  Optimal Method (google)

if __name__ == '__main__':
    N = int(input())
command=[]
for i in range(N):
    command.append(input().split())

result=[]
for i in range(N):
    if command[i][0]=='insert':
        result.insert(int(command[i][1]),int(command[i][2]))
    elif command[i][0]=='print':
        print(result)
    elif command[i][0]=='remove':
        result.remove(int(command[i][1]))
    elif command[i][0]=='append':
        result.append(int(command[i][1]))
    elif command[i][0]=='pop':
        result.pop()
    elif command[i][0]=='sort':
        result.sort()
    elif command[i][0]=='reverse':
        result.reverse()
