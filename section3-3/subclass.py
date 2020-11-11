from pandas import DataFrame

class SubclassedDataFrame(DataFrame):
  def __init__(self,rawData):
    super().__init__(rawData)
  def print_data(self):
    print(self)


df = SubclassedDataFrame({'column0': [1, 2, 3], # DataFrame을 상속받은 서브클래스를 활용하여 값을 출력한다.
            'column1': [10, 20, 30]
            })

df.print_data()