import math as math;
import random as random


def MedianOS(A):
  #Need to divide our list into groups of 5
  #If our last list i less than 5 members we find median of that
  #Repeat
  l = len(A);
  g = math.floor(l / 5);
  h = l % 5;
  B = [];
  C = [];
  tmp = [];
  for i in range(0,g):
    x = (i * 5); 
    for j in  range(x, x+5):
      tmp.append(A[j]);
    B.append(tmp[:]); #REMEMBER TO APPEND THE VALUES NOT THE OBJECT REFERENCE
    tmp.clear();
  if h != 0:
    for i in range(g*5,(g*5)+h):
      C.append(A[i]);
  return B;


def KthSmallest(B, s, t, k):
  if k > 0 and k <= t-s+1:
    p = RandomizedPivot(B, s, t)
    if (p - s) == (k - 1):  #position of pivot vs index of kth element
      return B[p];
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

