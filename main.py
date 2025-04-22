#MapPlot.py
#Name:Ryder A
#Date:04/19/2025
#Assignment:Lab 10 


import coffee
import pandas
import matplotlib.pyplot as plt
coffee = coffee.get_coffee()

#print(coffee[0]["Data"]["Scores"]["Total"])

years = []
scores = []

for nuc in coffee:
    year = nuc["Year"]
    score = nuc["Data"]["Scores"]["Total"]
    if score != 0: 
        years.append(year)
        scores.append(score)
    #print(year, score)

df = pandas.DataFrame({"Year": years,
                        "Score": scores})

print(df)
df.plot(kind = 'scatter', x = 'Year', y = 'Score' )
#plt.plot(years, scores, 'ro')
plt.savefig("output")