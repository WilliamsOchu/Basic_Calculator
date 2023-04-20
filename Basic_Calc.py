## This is a basic calculator project
## It will ask a user to input a first digit, input an operator and then input a second digit


nums1=float(input("Enter the Digit: "))
print("\n")
operator=input("Input your operator: ")
print("\n")
nums2=float(input("Enter second digit: "))
print("\n")

def calcops():
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
    return result    


output=calcops()
print("The result of this maths operation is: ", output) 
print("\n")   
    
        
        
