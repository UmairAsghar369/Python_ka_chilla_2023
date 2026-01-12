# defining a function
# 1 
def print_codanics():
    print("Line printed using function ")

print_codanics()

# 2 
def print_codanics1():
    text = "We are learning with Ammar"
    print(text)

print_codanics1()

# 3 
def print_codanics2(text):
    print(text)

print_codanics2("umair")


# defining a functio with if, elif and else statements
def school_calculator(age):
    if age == 5:
        print("you can go to school")
    elif age > 5:
        print("You are eligible for secondary schooling")
    else :
        print("You can not go to school")

school_calculator(3)
    
# defining a function of future 
def future_function(age):
    future_age = age+20
    return future_age

future_predicted_age = future_function(19)
print(future_predicted_age)

# i understand fuctions really well