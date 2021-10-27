import os
from PIL import Image
cata = ["addedLane", "curveLeft", "curveRight", "dip", "intersection", "laneEnds", "merge", "pedestrianCrossing", 
        "signalAhead", "slow", "stop", "stopAhead","thruMergeLeft", "thruMergeRight", "turnLeft", "turnRight", 
        "yield", "yieldAhead", "doNotPass", "keepRight", "rightLaneMustTurn", "speedLimit15", "speedLimit25", 
        "speedLimit30", "speedLimit35", "speedLimit40", "speedLimit45", "speedLimit50", "speedLimit55", 
        "speedLimit65", "truckSpeedLimit55","speedLimitUrdbl","school", "rampSpeedAdvisory20", "rampSpeedAdvisory35",
        "rampSpeedAdvisory40", "rampSpeedAdvisory45","rampSpeedAdvisory50","rampSpeedAdvisoryUrdbl","schoolSpeedLimit25",
        "thruTrafficMergeLeft","noLeftTurn", "noRightTurn", "zoneAhead25","zoneAhead45", "doNotEnter","roundabout"]
csv = open('allAnnotations.csv','r')
csv.readline()
csv = csv.readlines()
train = open('train.txt','a')
test = open('test.txt','a')
count=0
temppath=""
for line in csv:
    line_string = line.split(";")
    path = line_string[0]

    if path != temppath:
        train.write('data/'+path+"\n")
    
    count += 1
    if count%20 == 0:
        test.write('data/'+path+"\n")

    splitpath = path.split("/")
    txtname = splitpath[2]
    splitfile = txtname.split(".")
    filename = splitpath[0]+'/'+splitpath[1]+'/'+splitfile[0]+'.'+splitfile[1]+".txt"
    annotation = open(filename,'a')
    cata_num = cata.index(line_string[1])
    img = Image.open(path)
    x_center = (int(line_string[2])+int(line_string[4])) / (2 * img.size[0])
    y_center = (int(line_string[3])+int(line_string[5])) / (2 * img.size[1])
    width = (int(line_string[4])-int(line_string[2])) / img.size[0]
    height = (int(line_string[5])-int(line_string[3])) / img.size[1]
    s = str(cata_num)+' '+str(x_center)+' '+str(y_center)+' '+str(width)+' '+str(height)
    if path != temppath:
        annotation.write(s)
    if path == temppath:
        annotation.write("\n"+s)
    annotation.close()
    temppath = path

train.close()
test.close()


