class Node:
    def __init__(self,data,left_node,right_node):
        #클래스 내부 정의된 함수 매서드 첫번째 인자는 self
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == ".":
        left_node = None
    if right_node == ".":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

def pre_order(node): #전위 순위(root->left->right)
    print(node.data, end='') #자기 자신 먼저 처리
    if node.left_node != None: #left 있으면
        pre_order(tree[node.left_node])#재귀
    if node.right_node != None: #right 있으면
        pre_order(tree[node.right_node])

def in_order(node): #중위 순위 (left->root->right)
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None:
        in_order(tree[node.right_node])

def post_order(node): #후위 순위(left->right->root)
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end='')
    #end=''해주는 이유: \n 안되고 한줄로 출력될 수 있게


pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])