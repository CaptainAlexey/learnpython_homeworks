scores_students = [
    {"school_class": "4a", "scores":[5,1,4,9,8,3,2]},
    {"school_class": "5b", "scores":[2,3,3,5,8,10,5]},
    {"school_class": "2k", "scores":[1,1,11,10,7,9,6]},
    {"school_class": "5g", "scores":[7,7,9,14,3,7,2]},
    {"school_class": "8v", "scores":[6,8,1,13,12,1,1]}
]
average_score_school = 0
len_school = 0
average_score_class = 0 

for average_score in scores_students:
    average_score_school += sum(average_score["scores"])
    len_school += len(average_score["scores"])
average_score_school /= len_school
print(f"Общая средняя оценка по школе: {average_score_school}")

for average_score in scores_students:
    average_score_class += sum(average_score["scores"])
    school_class = average_score["school_class"]
    average_score_class /= len(average_score["scores"])
    print(f"Средняя оценка {school_class} класса составляет: {average_score_class}")
