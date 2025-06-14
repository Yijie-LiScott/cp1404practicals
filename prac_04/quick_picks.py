import random

MIN_NUM = 1
MAX_NUM = 45
NUM_PER_PICK = 6

num_picks = int(input("How many quick picks? "))

for _ in range(num_picks):
    pick = []
    while len(pick) < NUM_PER_PICK:
        num = random.randint(MIN_NUM, MAX_NUM)
        if num not in pick:
            pick.append(num)
    pick.sort()
    print(" ".join(f"{num:2}" for num in pick))