A = [6, 1, 4, 6, 3, 2, 7, 4]
K = 5
L = 3

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K, L):
    AppleChoices = A
    AliceTrees = K
    BobTrees = L

    # Handle lack of choice condition
    if len(AppleChoices) < AliceTrees + BobTrees:
        return -1

    # use sliding window approach
    # get the first window for Alice and Bob
    Alice_sum = sum([AppleChoices[i] for i in range(AliceTrees)])
    Bob_sum = sum([AppleChoices[i] for i in range(AliceTrees, AliceTrees + BobTrees)])

    # Store these totals as our best so far
    best_bob = Bob_sum
    best_alice = Alice_sum

    # Do the sliding window for Bob over the remaining tree rows
    for i in range(AliceTrees, len(AppleChoices)-BobTrees):
        Bob_sum = Bob_sum - AppleChoices[i] + AppleChoices[i + BobTrees]
        if Bob_sum > best_bob:
            best_bob = Bob_sum

    # Our best total for our alice is added to the best possible bob
    best_total = best_bob + best_alice

    # get the other alice windows
    for i in range(len(AppleChoices)-AliceTrees):
        # Get the alice sum
        Alice_sum = Alice_sum - AppleChoices[i] + AppleChoices[i + AliceTrees]

        # Once alice moves from the first row Bob now has
        # two areas to potentially go to we create these two options here
        Bob_Choice1 = AppleChoices[:i]
        Bob_Choice2 = AppleChoices[i+AliceTrees:]

        # Save running sliding door if the lenghth is perfect or smaller for bob
        if len(Bob_Choice1) <= BobTrees:
            best_bob_1 = sum([i for i in Bob_Choice1])
        else:
            # run the sliding door on the list
            Bob_tot_1 = sum([Bob_Choice1[i] for i in range(BobTrees)])
            best_bob_1 = Bob_tot_1
            for i in range(len(Bob_Choice1)-BobTrees):
                Bob_tot_1 = Bob_tot_1 - Bob_Choice1[i] + Bob_Choice1[i + BobTrees]
                # If we get a new best bob for choice one save it as the best
                if best_bob_1 < Bob_tot_1:
                    best_bob_1 = Bob_tot_1

        # Repeat the same as above but for the second list
        if len(Bob_Choice2) <= BobTrees:
            best_bob_2 = sum([i for i in Bob_Choice2])

        else:
            Bob_tot_2 = sum([Bob_Choice2[i] for i in range(BobTrees)])
            best_bob_2 = Bob_tot_2
            for i in range(len(Bob_Choice2)-BobTrees):
                Bob_tot_2 = Bob_tot_2 - Bob_Choice2[i] + Bob_Choice2[i + BobTrees]
                if best_bob_2 < Bob_tot_2:
                    best_bob_2 = Bob_tot_2

        # Figure out which bob option was best
        if best_bob_1 > best_bob_2:
            pick_total = best_bob_1 + Alice_sum
        else:
            pick_total = best_bob_2 + Alice_sum

        # If weve found a new best alice and bob position save it
        if pick_total > best_total:
            best_total = pick_total

    # Once the loop has completed return the highscore
    return best_total

# print(A[1+K:])
# for i in range(len(A)-K):
#     print("choices:", A[:i], A[i+K:])

print(solution(A, K, L))
print(solution(A, L, K))
