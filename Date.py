


class Date:
    def __init__(self, day = 17, month = 2, year = 2020):
        self.day = day
        self.month = month
        self.year = year

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def setDay(self, day):
        self.day = day

    def setMonth(self, month):
        self.month = month

    def setYear(self, year):
        self.year = year

    def getDate(self):
        return '%d%s%d%s%d' % (self.day, '/', self.month, '/', self.year)

    def getDateWithSep(self):
        return '%d%s%d%s%d' % (self.day, '-', self.month, '-', self.year)

    def forDay(self, day):
        if day > 0 and day <= 31:
            self.setDay(day)
        else:
            print(ValueError)

    def forMonth(self, month):
        if month > 0 and month <= 12:
            self.setMonth(month)
        else:
            print(ValueError)

    def forYear(self, year):
        if year > 0:
            self.setYear(year)
            
    def setDate(self, day, month, year):
    
        """
            sets the date of the clss object
            exmple imput can be '12', 1, 2020
            @Params: day (type: int), 
            @Params: month (type: int),
            @Params: year (type: int),
            @returns nothing
        """
        x = [4, 6, 9, 11]
    
        if year % 4 == 0:   #if the yeri is a good year
            if month == 2:
                if day > 29:
                    print(ValueError)
                else:
                    self.forYear(year)
                    self.forDay(day)
                    self.forMonth(month)

            for i in x:
                if month == i:
                    if day > 30:
                        print(ValueError)
                    else:
                        self.forYear(year)
                        self.forDay(day)
                        self.forMonth(month)
            else:
                self.forYear(year)
                self.forDay(day)
                self.forMonth(month)
            
                
        else:
            if month == 2:
                if day > 28:
                    print(ValueError)
                else:
                    self.forYear(year)
                    self.forDay(day)
                    self.forMonth(month)

            for i in x:
                if month == i in x:
                    if day > 30:
                        print(ValueError)
                    else:
                        self.forYear(year)
                        self.forDay(day)
                        self.forMonth(month)
            else:
                self.forYear(year)
                self.forDay(day)
                self.forMonth(month)
            
            

    
                
            
            
    def setDateFromString(self, date):
        """
          sets the date of the clss object
          @Params: '12/23/0202', '12-23-2020', 
        """
        int(self.setDay(day))
        int(self.setMonth(month))
        int(self.setYear(year))
        
