import csv

def activity(a):
    with open("static/data/stream.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        return((int(data[0][a])/int(data[0][1]))*360)

def activitytype():
    with open("static/data/stream.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        print(data)
        if int(data[0][0])==0:
            return ('normal')
        if int(data[0][0])==1:
            return ('suspicious')
        else:
            return('processing')

def criminalname():
    with open("static/data/facecount.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        print(data)
        return(data[0][1])

def criminalcount():
    with open("static/data/facecount.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        return(data[0][0])
    

    
