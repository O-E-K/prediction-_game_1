num_attempt = 0
num_correct = 0
predict = 0
lock_len = 0
current_lock_state = 0
next_lock_state = 0
delta_len = 0
current_delta = 0
deltas_found = [0, 0, 0, 0, 0, 0, 0, 0]
accuracy = (num_correct / num_attempt)

def setup():
    global current_lock_state
    global delta_len
    global lock_len


def attempt():
    global predict
    global num_attempt
    predict = input("What is the next sequence? ")
    num_attempt += 1


def check():
    global predict
    global next_lock_state
    global num_correct
    if predict == next_lock_state:
        num_correct += 1
        deltas_found[current_delta] = 1
        # add string letter check
    else:
        pass
