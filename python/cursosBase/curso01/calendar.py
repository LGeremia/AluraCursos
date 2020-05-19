class Date(object):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def show(self):
        print("%s/%s/%s" % (self.day,self.month,self.year))