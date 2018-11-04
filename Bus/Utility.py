import csv
from datetime import*
class Utility:
    bus_Stops = ['Ellicott', 'Lee Loop', 'Flint']
    d = {}
    def __init__(self):
        filename = "Schedule.csv"

        with open(filename, 'r', encoding='utf-8-sig') as file:
            csvreader = csv.reader(file)
            
            for line in csvreader:
                self.d[line[0]] = []
                for t in line[1:]:
                    try:
                        time = datetime.strptime(t,"%H:%M")
                        self.d[line[0]].append(time.time())
                    except ValueError:
                        continue
                break

    def getNextBusTime(self, location, currentTime):
        if location in self.bus_Stops:
            listOfTime = self.d[location]
            for time in listOfTime:
                if time > currentTime:
                    return time
            return None


                


