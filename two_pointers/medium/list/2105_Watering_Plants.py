# Alice and Bob want to water n plants in their garden. 
# The plants are arranged in a row and are labeled from 0 to n - 1 
# from left to right where the ith plant is located at x = i.

# Each plant needs a specific amount of water. Alice and Bob have a watering can each, initially full. They water the plants in the following way:

# Alice waters the plants in order from left to right, starting from the 0th plant. Bob waters the plants in order from right to left, starting from the (n - 1)th plant. They begin watering the plants simultaneously.
# It takes the same amount of time to water each plant regardless of how much water it needs.
# Alice/Bob must water the plant if they have enough in their can to fully water it. Otherwise, they first refill their can (instantaneously) then water the plant.
# In case both Alice and Bob reach the same plant, the one with more water currently in his/her watering can should water this plant. If they have the same amount of water, then Alice should water this plant.
# Given a 0-indexed integer array plants of n integers, where plants[i] is the amount of water the ith plant needs, and two integers capacityA and capacityB representing the capacities of Alice's and Bob's watering cans respectively, return the number of times they have to refill to water all the plants.

def minimumRefill(plants: list[int], capacityA: int, capacityB: int) -> int:
    alice_fill, bob_fill = 0,0
    temp_capacityA = capacityA
    temp_capacityB = capacityB
    left, right = 0, len(plants)-1
    while left < right:   
        if temp_capacityA < plants[left]:
            temp_capacityA = capacityA
            alice_fill += 1

        temp_capacityA -= plants[left]
        left += 1

        if temp_capacityB < plants[right]:
            temp_capacityB = capacityB
            bob_fill += 1

        temp_capacityB -= plants[right]
        right -= 1

    if left == right:
        max_capacity = max(temp_capacityB, temp_capacityA)
        if max_capacity < plants[left]:
            alice_fill += 1
    return bob_fill + alice_fill

print(minimumRefill(plants = [2,2,5,2,2], capacityA = 5, capacityB = 5))