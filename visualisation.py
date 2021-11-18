import matplotlib.pyplot as plt
import main

helpingArr = {}
for i in range(len(main.record1)):
    helpingArr[main.record1[i][0]] = main.record1[i][1]

plt.bar(helpingArr.keys(), helpingArr.values(), width=0.5)
plt.xlabel('Типи їжі')
plt.ylabel('Кількість')
plt.show()

helpingArr = {
    'Applesauce': main.record2[0][1],
    'Baked Potato': main.record2[1][1],
    'Acai': main.record2[2][1],
    'Canned Blueberries': main.record2[3][1],
    'Canned Blackberries': main.record2[4][1],
    'Canned Cherries': main.record2[5][1],
    'Apple': main.record2[6][1],
    'Canned Apricots': main.record2[7][1],

}

fig, ax = plt.subplots()
ax.pie(helpingArr.values(), labels=helpingArr.keys(), autopct='%1.1f%%', shadow=True,rotatelabels=True)
plt.show()

helpingArr = {}
for i in range(len(main.record3)):
    helpingArr[main.record3[i][0]] = main.record3[i][1]

fig, ax = plt.subplots()
ax.plot(helpingArr.keys(), helpingArr.values(), )

plt.xlabel('Type of Food')
plt.ylabel('Number of Cal')
plt.show()