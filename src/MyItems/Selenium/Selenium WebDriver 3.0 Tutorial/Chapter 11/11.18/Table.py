class Table(object):
    __table = '' #定义一个私有属性__table,用于存放Table对象

    def __init__(self,table): #Table类的构造方法
        self.setTable(table)

    def setTable(self,table): #对私有属性__table进行赋值操作
        self.__table = table

    def getTable(self,table): #获取私有属性__table的值
        return self.__table

    def getRowCount(self): #返回table对象中所有的行tr标签元素对象
        return len(self.__table.find_elements_by_tag_name('tr'))

    def getColumnCount(self): #获取表哥对象中的列数
        return len(self.__table.find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td'))

    def getCell(self,rowNo,colNo): #获取表格中某行某列的单元格对象
        try:
            currentRow = self.__table.find_elements_by_tag_name('tr')[rowNo - 1] #找到表格中的某一行,下标行号从0开始,例如要找第三行,下标需要计算为2,才能找到
            currentCol = currentRow.find_elements_by_tag_name('td')[colNo - 1] #找到表格中的某一列,下标行号从0开始,例如要找第三列,下标需要计算为2,才能找到
            return currentCol #返回找到的单元格对象
        except Exception as e:
            raise e

    def getWebElementInCell(self,rowNo,colNo,by,value): #获取表格中某行某列的单元格中某个页面元素对象
        try:
            currentRow = self.__table.find_elements_by_tag_name('tr')[rowNo - 1] #找到表格中的某一行,下标行号从0开始,例如要找第三行,下标需要计算为2,才能找到
            currentCol = currentRow.find_elements_by_tag_name('td')[colNo - 1] #找到表格中的某一列,下标行号从0开始,例如要找第三列,下标需要计算为2,才能找到
            element = currentCol.find_element(by = by,value = value) #获取具体某个单元格中的某个页面元素
            return element #返回找到的单元格对象
        except Exception as e:
            raise e
        
        
