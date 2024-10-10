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
        self.init_count()
    
    #Функуия удаляет дело
    def delete_issue(self,issue):
        self.issue.pop(issue)
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
    def change_transfer(self,issue):
        temp = self.issue.get(issue)
        if temp[2] == False:
            temp[2] = True
        else:
            temp[2] = False
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
            
        
        
    
    #Выводит информацию о всех делах
    def show(self):
        nums = 1
        for key,value in self.issue.items():
            print(f'{nums}.{key} time:{value[0]} {'Выполнено'if value[1] else 'Не выполнено'} {'Перенесено'if self.transfer_issue.get(key) else 'Не перенесено'}')
            nums += 1
        print(f'Не выполненные дела: {self.count_no_complete}')
        print(f'Перенесенные дела: {self.count_transfer}')
        print(f'Общее колличество дел: {self.count}')  


todo = Todo()
todo.add_issue('Завтрак','8:30', False,False)
todo.add_issue('Уборка','10:00', False,False)
todo.add_issue('Корм.Кот','12:30', False,False)
todo.change_transfer('Уборка')
todo.show()

#Удалить флан перенесено и разграничить хранение дел.
