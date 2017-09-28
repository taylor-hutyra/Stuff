import numpy as np
import pandas as pd
from setup import *

df = pd.read_csv("guidebook_score_export.csv", names = ['Judge_ID','Poster_ID','Presenter', 'Question_ID', 'Question', 'Response','Date'])

df=df[1:]
poster_list = list(set(df["Poster_ID"]))
poster_num = len(poster_list)
display(poster_num)
