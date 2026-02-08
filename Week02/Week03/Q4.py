monday_class = {"Alice", "Bob", "Charlie", "Diana"}


wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")
print("Monday Class", monday_class)
print("Wednesday Class", wednesday_class)

both_classe = monday_class & wednesday_class
print("Attend both classes: ", both_classes)

all_students = monday_class | wednesday_class
print("Attend either class: ", all_students)

only_monday = monday_class - wednesday_class
print("Only Monday: ", only_monday)

only_one = monday_class ^ wednesday_class
print(" Only one class: ", only_one)
print("Is monday the subset of all students?" monday_class <= all_students)

