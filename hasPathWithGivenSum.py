# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t, s):
    if t is None:
        return False
    if s == t.value and not t.left and not t.right:
        return True

    return solution(t.left, s - t.value) or solution(t.right, s - t.value)