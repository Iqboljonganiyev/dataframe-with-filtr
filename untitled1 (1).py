# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aXFx1UGQXYd-obfmH_rf-uRnWgHGMnPe
"""

import pandas as pd
baza={
  "FISH" :[  "Do'ltaboyev Muhammadjon", "Abdullayev Abror", "Abdusattorov Abdulloh", "Salayiddinov Lazizjon", "Ergashev Saydullo","Ashurmatov Ahadjon","Isaqov Muhammadqodir","Azimov Abdullajon","Muxtorov Nurullo","Nurmuhammadov Muhammadjon"  ],
  "Yoshi" :[ '19', '19', '19',  '20',  '19',  '18',  '20',  '21',  '17',  '19' ] ,
  "Maktabi" :[' 2-maktab',' 3-maktab',' 4-maktab',' 5-maktab',' 6-maktab',' 7-maktab',' 8-maktab',' 9-maktab',' 10-maktab',' 2-maktab'  ],
  "Jinsi" :[ "o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola" ],
  "Manzili" :["Dang'ara", "Qo'qon","Beshkapa","Bag'dod","Qo'qon","Andijon","Quva","Vodil","Dang'ara","Qo'qon" ],
}
db=pd.DataFrame(baza)
print(db)

filtr=db[db['Yoshi']=="19"]
print(filtr)

filtr=db[(db['Yoshi']=="19") & (db['Manzili']=="Qo'qon")]
print(filtr)