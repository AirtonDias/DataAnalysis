#Pacote de manipulação de dados
import pandas as pd
import numpy as np

#Pacotes graficos
import matplotlib.pyplot as plt
import seaborn as sns

#Pacotes de Modelagem Estatistica
import statsmodels.api as sm

df = pd.read_csv("base_funcionarios_v1.csv", sep=";", index_col= "id")
df.shape
df.head()
