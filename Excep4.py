def main():
	no1=int(input("Enter first no"))
	no2=int(input("Enter second no"))
	try:
		ans=no1/no2
	
	except ZeroDivisionError as obj:
		print("Divied by zero exception",obj)

	except Exception as eobj:
		print("Exception occurs",eobj)

	else:
		print("Divsion is:",ans)
	

if __name__=="__main__":
	main()