import sys
n = int(sys.stdin.readline())
company = {}
for _ in range(n):
    name, status = sys.stdin.readline().split()

    if status == "enter":
        company[name] = True
    else:
        if name in company:
            del company[name]
remain_people = list(company.keys())
remain_people.sort(reverse=True)
for person in remain_people:
    print(person)