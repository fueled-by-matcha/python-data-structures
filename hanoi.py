from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create Stacks
stacks = []
left_stack = Stack("Left")
right_stack = Stack("Right")
middle_stack = Stack("Middle")

# add stacks to list
stacks.append(left_stack)
stacks.append(right_stack)
stacks.append(middle_stack)

# set up game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

# check for 3 or more disks
while num_disks < 3:
  num_disks = int(input("\nEnter a number greater than or equal to 3\n"))

# fill up first stack
for item in range(num_disks, 0, -1):
  left_stack.push(item)

num_optimal_moves = 2**num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves\n")

# Get user input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(0, len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f"\nEnter {letter} for {name}\n")
    user_input = input("")
    if user_input in choices:
      for i in range(0, len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
          
# play the game
num_user_moves = 0



