stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

stops.append("Edinburgh Waverley") #1
stops = ["Glasgow Queen St"] + stops #2
stops.insert(4, "Polmont") #3
print(stops.index("Linlithgow")) #4 // Output: 5
stops.remove("Livingston") #5 // Output: ['Glasgow Queen St', 'Croy', 'Cumbernauld', 'Falkirk High', 'Polmont', 'Linlithgow', 'Haymarket', 'Edinburgh Waverley']
stops.pop(2) #6 // Output: ['Glasgow Queen St', 'Croy', 'Falkirk High', 'Polmont', 'Linlithgow', 'Haymarket', 'Edinburgh Waverley']
print(len(stops)) #7 // Output: 7
print(sorted(stops)) #8 // Output: ['Croy', 'Edinburgh Waverley', 'Falkirk High', 'Glasgow Queen St', 'Haymarket', 'Linlithgow', 'Polmont']
print(sorted(stops, reverse=True)) #9 // Output: ['Polmont', 'Linlithgow', 'Haymarket', 'Glasgow Queen St', 'Falkirk High', 'Edinburgh Waverley', 'Croy']

#10
for stop in stops:
    print(stop)


#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop
