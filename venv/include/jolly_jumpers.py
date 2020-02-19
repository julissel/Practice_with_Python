# The program is checking a sequence for its being "Jolly jumper".
# The sequence is called "Jolly jumper" if the values of the absolute differences of consecutive elements take all
# possible values between 1 and (N-1). [1, 3, 5] is not "Jolly", while [4] and [1, -3, -4, -1, 1] are "Jolly".


list_of_elements = [int(val) for val in input().split(" ") if val != " "]
max_abs_differ_for_sequent_elem = len(list_of_elements) - 1

if max_abs_differ_for_sequent_elem < 0 or max_abs_differ_for_sequent_elem >= 10000:
    print("Not jolly")
else:
    result_set = {abs(list_of_elements[i] - list_of_elements[i + 1]) for i in range(0, max_abs_differ_for_sequent_elem)}

    check_set = {i for i in range(1, max_abs_differ_for_sequent_elem + 1)}

    if len(result_set.symmetric_difference(check_set)) == 0:
        print("Jolly")
    else:
        print("Not jolly")
