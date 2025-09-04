# There is a school that has classes of students and each class will be having a final exam. 
# You are given a 2D integer array classes, where classes[i] = [passi, totali]. 
# You know beforehand that in the ith class, there are totali total students, 
# but only passi number of students will pass the exam.

# You are also given an integer extraStudents. 
# There are another extraStudents brilliant students that are guaranteed to pass 
# the exam of any class they are assigned to. 
# You want to assign each of the extraStudents students to a class in 
# a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class 
# that will pass the exam divided by the total number of students of the class. 
# The average pass ratio is the sum of pass ratios of all the classes divided by 
# the number of the classes.

# Return the maximum possible average pass ratio after assigning the extraStudents students. 
# Answers within 10-5 of the actual answer will be accepted.

def maxAverageRatio(classes: list[list[int]], extraStudents: int) -> float:
    cur_passes = []
    for i in range(len(classes)):
        cur_passes.append((classes[i][0]/classes[i][1]))

    while extraStudents > 0:
        updated_passes = []

        # Create range updated passes
        for i in range(len(classes)):
            updated_passes.append(((classes[i][0]+1)/(classes[i][1]+1)))

        # Find max delta and set max_delta_index
        max_delta = 0
        cur_delta = 0
        max_delta_indx = 0
        for i in range(len(updated_passes)):
            cur_delta = updated_passes[i] - cur_passes[i]

            if cur_delta > max_delta:
                max_delta = cur_delta
                max_delta_indx = i

        # Set new value for passes
        cur_passes[max_delta_indx] = updated_passes[max_delta_indx]
        classes[max_delta_indx][0] += 1
        classes[max_delta_indx][1] += 1
        extraStudents -= 1

    return sum(cur_passes)/len(cur_passes)
            


print(maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2))
