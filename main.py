nric = input('Enter an NRIC number: ')

# Type your code below
letterStart = ["S", "T", "F", "G"]
digitWeightTable = [2, 7, 6, 5, 4, 3, 2]
letterTable = {
  "ST": ["J", "Z", "I", "H", "G", "F", "E", "D", "C", "B", "A"], 
  "FG": ["X", "W", "U", "T", "R", "Q", "P", "N", "M", "L", "K"]
}

if(len(nric.strip()) == 9):
  if(letterStart.count(nric[0]) > 0 and nric[1:7].isdigit() and nric[8].isalpha()):
    # print("NRIC format is valid.")
    #Part 1 Complete!
    sum = 0
    if(nric[0] == "T" or nric[0] == "G"):
      sum = 4
    i = 1
    while (i <= 7):
      sum += int(nric[i]) * digitWeightTable[i-1]
      i+=1
      
      

    quotient, checkdigit = divmod(sum, 11)
    # print(checkdigit)
    if(nric[0] == "T" or nric[0] == "S"):
      key = "ST"
    else: 
      key = "FG"
    # print(letterTable[key][checkdigit])
    # print(nric[8])
    if(letterTable[key][checkdigit] == nric[8]):
      print("NRIC is valid.")

    else:
      print("NRIC is invalid.")
  else:
    print("NRIC is invalid.")
else:
  print("NRIC is invalid.")
