# practicing with lists

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
# combine the subjects and grades into a gradebook
gradebook = []
for i in range(len(grades)):
    lists = [subjects[i], grades[i]]
    gradebook.append(lists)

# combine both gradebooks
full_gradebook = last_semester_gradebook + gradebook

if __name__ == "__main__":
    # print sorted full gradebook
    for i in sorted(full_gradebook):
        for x in i:
            if x != i[-1]:
                print(f"{x}:", end=" ")
            else:
                print(f"{x}%")