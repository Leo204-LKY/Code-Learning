# while statement
# allow us to execute a block of code repeatedly provided a certain condition is True
# also referred to as indefinite execution
# >>> while <condition>:
# >>>     body
# Example:
i = 0
while i < 10: # condition, it will check everytime before the loop
    print(i)  # body
    i += 1    # i + 1
# When i < 10 is False, the loop will exit

# break statement
# used to exit a loop and prevent the loop body from executing regardless of whether the while condition is true
# Example:
i = 0
while i < 5:
    if i == 3:
        break
    # When i == 3 is True, the while loop will exit
    i += 1
    print(i)

# continue statement
# allow us to stop the current literation (stop the while loop body from executing) and move to the next literation
# Example:
i = 0
while i < 5:
    i += 1
    if not i % 2:
        continue
    print(i)