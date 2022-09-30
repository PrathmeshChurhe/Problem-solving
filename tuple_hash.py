# problem statement : Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .  Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# optimal solution of the probelm

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int,input().split())
    
    intger_list=tuple((integer_list))
    print(hash(intger_list))
