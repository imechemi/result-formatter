import os
import re

def format(metaKeys, values, result):
  subjectCount = len(values) // 2; 

  start = 0
  for i in range(2, len(metaKeys)):
    if (re.search("[a-zA-Z]", metaKeys[i]) == None):
      start = i;
      break

  namePartsInReverse = [];

  for i in reversed(range(start)):
    if (i == 1):
      break
    namePartsInReverse.append(metaKeys[i])

  studentName = "";
  for part in reversed(namePartsInReverse):
    studentName += part + " "

  j = 0
  output = [
    metaKeys[0], metaKeys[1], studentName
  ]

  index = 0;
  subjectIndex = start
  scoreIndex = 0
  while(index < subjectCount):
    if (metaKeys[subjectIndex] != 'ABST'):
      output.append(metaKeys[subjectIndex])
    if (result == 'ABST'):
      output += [' ', ' ']
    else:
      output += [values[scoreIndex], values[scoreIndex + 1]]
    subjectIndex += 1
    scoreIndex += 2
    index += 1

  if (result == 'ABST'):
    output += [' ', ' ', ' ', result]
  else:
    for i in range(start + 5, len(metaKeys)):
      output.append(metaKeys[i])

  return output

txtFiles = os.listdir("txt_files")

for txtFile in txtFiles:

  file1 = open("txt_files/" + txtFile, "r")
  lines = file1.readlines()


  lineIndex = 0
  while (lineIndex + 1 < len(lines)):
    metaKeys = lines[lineIndex].split();
    values = lines[lineIndex + 1].split();
    result = metaKeys[len(metaKeys) - 1]
    formattedRow = format(metaKeys, values, result)
    print(','.join(formattedRow))
    if (result == 'ABST'):
      lineIndex += 1
    else: 
      lineIndex += 2

  file1.close()


