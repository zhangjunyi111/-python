import copy
import sys

# 构造节点类


class ListNode:
    def __init__(self, val, nextaddr):
        self.val = val
        self.next = nextaddr

# 处理输入信息


node_info = {}
head_input = input().split()
head_addr = head_input[0]
node_count = int(head_input[1])

listnodes = [input().split(" ") for i in range(node_count)]

for i in listnodes:
    addr = i[0]
    val = int(i[1])
    nextaddr = i[2]
    tmp_node = ListNode(val, nextaddr)
    node_info[addr] = tmp_node

size = 1
cur = 0
head_node = node_info[head_addr]
tmp_head = copy.copy(head_node)
# tmp_head = head_node
while tmp_head.next != "-1":
    size += 1
    tmp_head = node_info[tmp_head.next]
# print()
while head_node.next != "-1":
    if int(size/2) == cur:
        print(head_node.val)
        break
    head_node = node_info[head_node.next]
    cur += 1







