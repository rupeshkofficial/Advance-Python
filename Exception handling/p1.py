try:
    a = 20 / 0
    #a = 20 /20
    print(a)
except Exception as e:
    print("Error Occured in try block",e)
else:
    print("No error occured in try block, try block executed successfully!")
finally:
    print("Finally Block Executed Successfully!")
