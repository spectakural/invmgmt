from pandas import read_excel

class item:
    
    def __init__(self, data): 
        self.slno, self.dop, self.firmname, self.pname, self.cat, self.consumption, self.vvn, self.qty, self.units, self.price, self.totalprice, self.netprice, self.pgno, = data
        self.values = data
    
    def __repr__(self):
        return str(self.values)


class records:
    def __init__(self, filename = ""):
        if filename:
            df = read_excel(filename)
            self.values = []
            for i in df.iterrows():
                self.values.append(item(i.tolist()))

 
 
        else:
            pass
        print(self.values)
        
    def addRow(self, ):
        pass

            

items = records('./static/Book1.xlsx')
