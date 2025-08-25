# You are given two categories of theme park attractions: land rides and water rides.

# Land rides
# landStartTime[i] – the earliest time the ith land ride can be boarded.
# landDuration[i] – how long the ith land ride lasts.
# Water rides
# waterStartTime[j] – the earliest time the jth water ride can be boarded.
# waterDuration[j] – how long the jth water ride lasts.
# A tourist must experience exactly one ride from each category, in either order.

# A ride may be started at its opening time or any later moment.
# If a ride is started at time t, it finishes at time t + duration.
# Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.
# Return the earliest possible time at which the tourist can finish both rides.
def earliestFinishTime(landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
    min_time = 0
    for i in range(len(landStartTime)):
        for j in range(len(waterStartTime)):
