import math as math
import random as random

# Helper function to group our list
def group(A, stepSize = 5):
  for i in range(0, len(A), stepSize):
    yield A[i:i+stepSize]    # Returns an object that can be iterated


def MedianOS(A):
  # Need to divide our list into groups of 5
  # If our last list i less than 5 members we find median of that
  # Repeat
  a = list(group(A))
  QSort(A , 0 , len(A) - 1)

def QSort(A, s, t):
  if s < t:
    p = RandomizedPivot(A, s, t)
    QSort(A, s, p)
    QSort(A, p + 1 , t)

def KthSmallest(B, s, t, k):
  if k > 0 and k <= t-s+1:
    p = RandomizedPivot(B, s, t)
    if (p - s) == (k - 1):  # position of pivot vs index of kth element
      return B[p]
    if (p - s) <= (k - 1):
      return KthSmallest(B, p + 1, t, k-p+s-1) #Repositions k with respect to the second half of list
    return KthSmallest(B, s, p - 1, k)


def RandomizedPivot(B, s, t):
  l = t - s + 1
  pivot = random.randrange(l)
  B[pivot + s], B[t] = B[t], B[pivot + s]
  count = s; #points to current index to compare to pivot
  for i in range(s, t):
    if B[i] <= B[t]:
      B[i],B[count] = B[count],B[i]
      count += 1
  B[count],B[t] = B[t],B[count]
  return count

