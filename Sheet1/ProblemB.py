# Omar is a student in Kindergarten, He is learning to differentiate between odd numbers and even numbers in class. The Teacher is testing the children's counting of the odd numbers and he asks them to write odd numbers from 1 to n Help Omar to answer The question
n = int(input())
for i in range(1, n+1,2):
    print(str(i) + " ")
    # add 2 cause each odd is more than before by 2