#bubblesort review
# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
# 针对所有的元素重复以上的步骤，除了最后一个。

student_scores = input("Input a list of student scores \n").split(',')#轉換strings為list
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
for n in range(0, len(student_scores)):
    for i in range(0, len(student_scores)-1):
        if student_scores[i] > student_scores[i+1]:
            c = student_scores[i]
            student_scores[i] = student_scores[i+1]
            student_scores[i+1] = c
print(student_scores)
print(f'The highest score in the class is: {student_scores[-1]}')

#僅取最大值 不排序時
#highest_score = 0
#for score in student_scores:
#if score > highest_score:
#highest_score = score

