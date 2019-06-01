def main():
    ## Program to take a CSV file exported from a GPS device and extract
    ## waypoint names and coordinates for display
    waypoints = GPStoList("GPS.csv")
    printWaypoints(waypoints)

def GPStoList(fileName):
    ## Opens CSV file and split records into a list
    infile = open(fileName, 'r')
    listOfRecords = [line.rstrip() for line in infile]
    infile.close()

    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(',')

    return listOfRecords

def printWaypoints(waypoints):
    ## Display waypoint name and Lat/Lon
    print("{0:20}{1:10}{2:10}".format("Waypoint Name", "Latitude", "Longitude"))
    for i in range(len(waypoints)):
        print("{0:20}{1:10}{2:10}".format(waypoints[i][1], waypoints [i][2],waypoints[i][3]))
    
main()
