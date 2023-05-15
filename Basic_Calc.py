## This is a basic calculator project
## It will ask a user to input a first digit, input an operator and then input a second digit


## Code modified to prevent a user from getting an error when he enters an alphabet instead of a number 


def calcops():
    while True:
        try:
            
            nums1=float(input("Enter the first Digit: "))
            print("\n")
            operator=input("Input your operator: ")
            print("\n")
            nums2=float(input("Enter second digit: "))
            print("\n")
    

            match operator:
                case "+":
                    result=nums1+nums2
                case "-":
                    result=nums1-nums2
                case "*":
                    result=nums1*nums2
                case "/":
                    result=nums1/nums2
                case "//":
                    result=nums1//nums2
                case "%":
                    result=nums1%nums2
                case "**":
                    result=nums1**nums2
                case _:
                    result="You have entered an incorrect operand"
                    
        except ValueError:
            print("Enter numbers only")
            
            
        else:
            break
                        
    return result
    


output=calcops()
print("The result of this maths operation is: ",output) 
print("\n")   
    
        
        
