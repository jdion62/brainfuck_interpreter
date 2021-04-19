from BrainFuckState import state
import sys

def walk(node):
    node_type = node[0]
    if(node_type in dispatch_dict):
        node_func = dispatch_dict[node_type]
        return node_func(node)
    else:
        raise ValueError("Invalid node type: " + node_type)

def sequenceNode(node):
    (node_type, s1, s2) = node
    assert(node_type == 'seq')

    walk(s1)
    walk(s2)

    return

def nilNode(node):
    (node_type, ) = node
    assert(node_type == 'nil')
    return

def lshiftNode(node):
    (node_type, ) = node
    assert(node_type == 'lshift')
    if(state.dataIndex > 0):
        state.dataIndex -= 1
    else:
        raise ValueError("Tried to access negative dataIndex")

def rshiftNode(node):
    (node_type, ) = node
    assert(node_type == 'rshift')
    if(state.dataIndex < 30000):
        state.dataIndex += 1
    else:
        raise ValueError("Tried to access dataIndex greater than 30000")

def plusNode(node):
    (node_type, ) = node
    assert(node_type == 'plus')
    if(state.memory[state.dataIndex] < 255):
        state.memory[state.dataIndex] += 1
    else:
        raise ValueError("Exceeds maximum value (1 Byte)")

def minusNode(node):
    (node_type, ) = node
    assert(node_type == 'minus')
    if(state.memory[state.dataIndex] > 0):
        state.memory[state.dataIndex] -= 1
    else:
        raise ValueError("Value would be negative")

def outputNode(node):
    (node_type, ) = node
    assert(node_type == 'output')
    if(state.memory[state.dataIndex] >= 32):
        print(chr(state.memory[state.dataIndex]), end="")
    else:
        print(state.memory[state.dataIndex], end="")

def inputNode(node):
    (node_type, ) = node
    assert(node_type == 'input')
    word = input()
    if(len(word) != 1):
        raise ValueError("Please provide only one character to the input at a time!")
    char = word[0]
    
    if(char in [" ", "\t", "\n"]):
        state.memory[state.dataIndex] = 0
    else:
        state.memory[state.dataIndex] = ord(char)


def blockNode(node):
    (node_type, body) = node
    assert(node_type == 'block')
    while state.memory[state.dataIndex] != 0:
        walk(body)
        

dispatch_dict = { 
                "seq":sequenceNode,
                "nil":nilNode,
                "lshift":lshiftNode,
                "rshift":rshiftNode,
                "plus":plusNode,
                "minus":minusNode,
                "output":outputNode,
                "input":inputNode,
                "block":blockNode
                }
