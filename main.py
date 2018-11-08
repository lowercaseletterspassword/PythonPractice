counter = 0
score_total = 0
test_score = 0

while test_score != 999:
    test_score = int(input("Enter test score: "))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1

Average_score = round(score_total / counter)

print("Total score: " + str(score_total))
print("Average score: " + str(Average_score))
