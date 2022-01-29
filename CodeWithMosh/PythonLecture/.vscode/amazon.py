############################ Height of a Binary Tree ####################################

def height(root):
    if root is not None:
        return -1
    return max(height(root.left), height(root.right)) + 1

############################ Tree Level Order Traversal ####################################

def levelOrder(root):
    q = []
    q.append(root)
    
    while len(q) != 0:
        q.pop(0)
        root = q.pop
        print(root.info)
        
        if root.left is not None:
            q.append(root.left)
        if root.rigth is not None:
            q.append(root.right)
            
############################ Balanced Bracket or Balanced Parenthesis ####################################
def isBalanced(s):
    while '[]' in s or '()' in s or '{}' in s:
        s = s.replace("[]" , '')
        s = s.replace('{}' , '')
        s = s.replace('()' , '')
    return 'YES' if len(s) == 0 else 'NO'

############################ Finding the running Median ####################################
import heapq
import bisect

def running(a):
    p = []
    l = 0
    q = []
    
    for i in range(len(a)):
        l = l + 1
        bisect.insort(p, a[i])
        if(l % 2) == 1:
            q.append(p(l//2))
        else:
            q.append((p[l//2] + p[l//2 - 1])/2)
    return q

############################ Simple Array sum ####################################

def simpleArraySum(ar):
    # Write your code here
    sum = 0
    for i in ar:
        sum += i
    return sum