class Todo:
    #Конструктор класса Todo, добавляет словарь дел и счетчики.
    def __init__(self):
        self.issue = {}#Словарь дел
        self.transfer_issue = {}#Словарь перенесенных дел.
        self.count = 0
        self.__count_no_complete = 0
        self.__count_transfer = 0
    
    #Функция добавляет новое дело
    def add_issue(self,issue,clock,complete,transfer):
        self.issue[issue] = [clock,complete,transfer]
        #создание временного словаря и сортировка по времени
        sort_issue = dict(sorted(self.issue.items(), key = lambda item: (int(item[1][0].split(':')[0]),int(item[1][0].split(':')[1]))))
        #замена старого словаря на отсортированный
        self.issue = sort_issue
        self.init_count()
    
    #Функуия удаляет дело
    def delete_issue(self,issue):
        self.issue.pop(issue)
        #Проверка наличия дела в словаре перенесенных дел
        if self.transfer_issue.get(issue):
            #Удаление дела из словаря перенесенных дел
            self.transfer_issue.pop(issue)
        #создание временного словаря и сортировка по времени
        sort_issue = dict(sorted(self.issue.items(), key = lambda item: (int(item[1][0].split(':')[0]),int(item[1][0].split(':')[1]))))
        #замена старого словаря на отсортированный
        self.issue = sort_issue
        self.init_count()
    
    #Возвращает общее колличество дел    
    def get_count(self):
        return self.count
    
    #Возвращает колличество не выполненных дел
    @property
    def count_no_complete(self):
        return self.__count_no_complete
    
    #Возвращает колличество перенесенных дел
    @property
    def count_transfer(self):
        return self.__count_transfer
    
    #Закладывает значение в колличество не выполненных дел
    @count_no_complete.setter
    def count_no_complete(self,count_no_complete):
        self.__count_no_complete = count_no_complete
        
    #Закладывает значение в колличество перенесенных дел
    @count_transfer.setter
    def count_transfer(self,count_transfer):
        self.__count_transfer = count_transfer
        
        
    #Изменяет состояние дела Выполнено\Не выполнено
    def change_issue(self,issue):
        temp = self.issue.get(issue)
        if temp[1] == False:
            temp[1] = True
        else:
            temp[1] = False
            
        self.issue.update({issue:temp})
        self.init_count()
    
    #Изменяет состояние дела Перенесено\Не перенесено
    def change_transfer(self,issue, new_time):
        temp = self.issue.get(issue)
        if temp[2] == False:
            temp[2] = True
            self.transfer_issue[issue] = [new_time,False,False]#добавляем дело в новый словарь   
            
        else:
            temp[2] = False
            self.transfer_issue.pop(issue)#удаляем дело из нового словаря
        
        self.issue.update({issue:temp})
        self.init_count()
    
    #Обновляет данные счетчитков на актуальные    
    def init_count(self):
        c_complete = 0
        c_transfer = 0
        count = 0
        for value in self.issue.values():
            count += 1
            if value[1] == False:
                c_complete += 1
            if value[2] == True:
                c_transfer += 1
        self.count_no_complete = c_complete
        self.count_transfer = c_transfer
        self.count = count
            
    def new_issue(self):
        task = input('Введите название дела: ') #Вводим дело
        time = input('Введите время в формате ЧЧ:ММ - ')#Вводим время
        busy_time = []
        for i in self.issue.values():
            busy_time.append(i[0])
        if time not in busy_time:
            self.add_issue(task,time,False,False)
        else:
            print('Укажите другое время')
        
    
    #Выводит информацию о всех делах
    def show(self):
        nums = 1
        for key,value in self.issue.items():
            print(f'{nums}.{key} time:{value[0]} {'Выполнено'if value[1] else 'Не выполнено'} {'Перенесено'if value[2] else 'Не перенесено'}')
            nums += 1
        print(f'Не выполненные дела: {self.count_no_complete}')
        print(f'Перенесенные дела: {self.count_transfer}')
        print(f'Общее колличество дел: {self.count}')
        


todo = Todo()
todo.add_issue('Завтрак','8:30', False,False)
todo.add_issue('Уборка','10:00', False,False)
todo.add_issue('Корм.Кот','12:30', False,False)
todo.add_issue('Ожид.Курьера','10:45', False,False)
todo.add_issue('Починка крана','12:15', False,False)
todo.new_issue()
todo.show()


#добавить
#прокоментировать функцию new_issue

