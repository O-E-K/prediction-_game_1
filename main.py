num_attempt = 0
num_correct = 0
predict = 0
current_state = 0
next_state = 0
accuracy = (num_correct / num_attempt)

# getting the user input
def attempt():
    global predict
    global num_attempt
    predict = input("What is the next sequence? ")
    num_attempt += 1

# checking user input for correctness    
def check():
    global predict
    global next_state
    global num_correct
    if predict == next_state:
        num_correct += 1
        #add string letter check
    else:
        pass
