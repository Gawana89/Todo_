issue = {}

issue['Завтрак'] = ['8:00',False, False]
issue['Корм.Кота'] = ['10:30',False, False]
issue['Уборка'] = ['8:20',False, False]




sort_issue = dict(sorted(issue.items(), key = lambda item: (int(item[1][0].split(':')[0]),int(item[1][0].split(':')[1]))))
for key,value in sort_issue.items():
    print(key,value)


    