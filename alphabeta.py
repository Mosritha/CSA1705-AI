# A simple Python3 program to find
# maximum score that
# maximizing player can get
import math

def alphabeta (curDepth, nodeIndex,
			maxTurn, scores, 
			targetDepth):

	# base case : targetDepth reached
	if (curDepth == targetDepth): 
		return scores[nodeIndex]
	
	if (maxTurn):
		return max(alphabeta(curDepth + 1, nodeIndex * 2, 
					False, scores, targetDepth), 
				alphabeta(curDepth + 1, nodeIndex * 2 + 1, 
					False, scores, targetDepth))
	
	else:
		return min(alphabeta(curDepth + 1, nodeIndex * 2, 
					True, scores, targetDepth), 
				alphabeta(curDepth + 1, nodeIndex * 2 + 1, 
					True, scores, targetDepth))
	
# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)


print("The optimal value is : ", end = "")
print(alphabeta(0, 0, True, scores, treeDepth))

# This code is contributed
# by rootshadow
