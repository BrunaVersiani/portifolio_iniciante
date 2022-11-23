from faker import Faker
import pandas as pd
fake = Faker()
data = [fake.profile() for i in range(90)]
data = pd.DataFrame(data)
print(data.head())

#Criar dados fakes, pode ser bem util para estudos.