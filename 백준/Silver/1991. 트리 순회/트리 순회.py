num = int(input())
adj_dict = {}
trail = []
for i in range(num):
    x, y, z = input().split()
    adj_dict[x] = [y, z]

def traverse1(root):
    print(root, end='')
    left = adj_dict[root][0]
    right = adj_dict[root][1]
    if left != '.':
        traverse1(left)
    if right != '.':
        traverse1(right)
        
def traverse2(root):
    left = adj_dict[root][0]
    right = adj_dict[root][1]
    if left != '.':
        traverse2(left)
    print(root, end='')
    if right != '.':
        traverse2(right)

def traverse3(root):
    left = adj_dict[root][0]
    right = adj_dict[root][1]
    if left != '.':
        traverse3(left)
    if right != '.':
        traverse3(right)
    print(root, end='')
    
traverse1('A')
print()
traverse2('A')
print()
traverse3('A')