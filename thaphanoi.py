# bài toán tháp Hà Nội 

def thaphanoi(n , source, destination, auxiliary):
	if n==1:
		print ("di chuyển đĩa 1 từ nguồn",source,"đến đích",destination)
		return
	thaphanoi(n-1, source, auxiliary, destination)
	print ("di chuyển đĩa",n,"từ nguồn",source,"đến đích",destination)
	thaphanoi(n-1, auxiliary, destination, source)
def main():
  n = int(input("n:"))
  thaphanoi(n,'A','B','C')
if __name__=="__main__":
	main()

