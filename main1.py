issue = {}

issue['Завтрак'] = ['8:30',False, False]
issue['Уборка'] = ['10:30',False, False]
issue['Корм.Кота'] = ['12:00',False, False]

for key,value in issue.items():
    print(key,value)

delete = issue.pop('Завтрак')
print(delete)