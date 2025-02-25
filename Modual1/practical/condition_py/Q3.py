# Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"  
    elif percentage >= 80:
        return "A"   
    elif percentage >= 70:
        return "B+" 
    elif percentage >= 60:
        return "B"   
    elif percentage >= 50:
        return "C+"  
    elif percentage >= 40:
        return "C"
    else:
        return "F"   
percentage = float(input("Enter the percentage: "))

grade = calculate_grade(percentage)
print(f"The grade for {percentage}% is: {grade}")
