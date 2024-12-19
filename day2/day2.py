f = open("input2.txt", "r")
list_of_reports = []

for line in f:
    split_line = line.strip("\n")
    int_list = [int(x) for x in split_line.split(" ")]
    list_of_reports.append(int_list)

f.close()


number_of_safe_reports = 0


def is_safe(report, is_increasing):
    for index, value in enumerate(report):
        if index == len(report) - 1:
            break

        difference = report[index + 1] - value

        if (
            (difference > 0 and not is_increasing)
            or (difference < 0 and is_increasing)
            or abs(difference) < 1
            or abs(difference) > 3
        ):
            return False
    return True


def is_safe_removing_one(report):
    for i in range(len(report)):
        removed_report = report.copy()
        del removed_report[i]

        if is_safe(removed_report, True) or is_safe(removed_report, False):
            return True
    return False


for report in list_of_reports:
    this_report_is_safe = True
    is_increasing = True

    if is_safe(report, True) or is_safe(report, False):
        number_of_safe_reports += 1

    else:
        if is_safe_removing_one(report):
            number_of_safe_reports += 1
print(number_of_safe_reports)
