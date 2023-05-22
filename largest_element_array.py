# program to find maximum in arr[] of size n
def largest(arr, n):
	ans = max(arr)
	return ans;

# Driver code
if __name__ == '__main__':
	arr = [10, 324, 45, 90, 9808, 1002544]
	n = len(arr)
	print ("Largest in given array ", largest(arr, n))
