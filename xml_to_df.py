#!/usr/bin/python
# coding: utf-8 -*-

import petl as etl
import json,sys
import pandas as pd
import numpy as np

#xml
#based on the structure update args in this case : 'row' and kargs in this case
tabl = etl.fromxml('data.xml','row',{'Id':'Id','PID':'PID','Val':'Val'})
#export result to csv file
etl.tocsv(tabl,'data.csv')


####################################################################################

mpu = etl.fromxml('data2.xml','row',{'field name=MID':'field'})
#export result to csv file

MID = []
LID = []
title = []
shortTitle = []
director = []
cast = []
year = []
genre = []
description = []
shortDescription = []
trailerMID = []
review = []
countryOrigin = []
peopleScore = []
criticScore= []

for items in mpu:
    if len(items[0]) == 15:
        MID.append(items[0][0])
        LID.append(items[0][1])
        title.append(items[0][2])
        shortTitle.append(items[0][3])
        director.append(items[0][4])
        cast.append(items[0][5])
        year.append(items[0][6])
        genre.append(items[0][7])
        description.append(items[0][8])
        shortDescription.append(items[0][9])
        trailerMID.append(items[0][10])
        review.append(items[0][11])
        countryOrigin.append(items[0][12])
        peopleScore.append(items[0][13])
        criticScore.append(items[0][14])


df = pd.DataFrame(np.column_stack([MID, LID, title,shortTitle,director,cast,year,genre,description,shortDescription,trailerMID,review,countryOrigin,peopleScore,criticScore]),columns=['MID','LID','title','shortTitle','director','cast','year','genre','description','shortDescription','trailerMID','review','countryOrigin','peopleScore','criticScore'])

df.to_csv('data2.csv',encoding='utf-8')
