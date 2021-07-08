import numpy as np
import pandas as pd
import math
from info_gain import info_gain

Color=["red","blue","green","red","green","green","blue","blue","red","blue","green","red","green","green"]
Type=["suv","minivan","car","minivan","car","suv","suv","car","suv","car","suv","car","suv","minivan"]
Doors=[2,4,4,4,2,4,2,2,2,4,4,2,2,4]
Tyres=["whitewall","whitewall","whitewall","blackwall","blackwall","blackwall","blackwall","whitewall","blackwall","blackwall","whitewall","blackwall","blackwall","whitewall"]
Class=["A","B","B","B","A","B","B","A","B","B","A","A","B","B"]

probClass = [ float(Class.count(c)) / len(Class) for c in dict.fromkeys(list(Class)) ]
       
entropyClass = - sum([ p * math.log(p) / math.log(2.0) for p in probClass ])

print("entropyClass",entropyClass)

probColor= [ float(Color.count(c)) / len(Color) for c in dict.fromkeys(list(Color)) ]
       
entropyColor = - sum([ p * math.log(p) / math.log(2.0) for p in probColor ])

print("entropy Color",entropyColor)

probType= [ float(Type.count(c)) / len(Type) for c in dict.fromkeys(list(Type)) ]
       
entropyType = - sum([ p * math.log(p) / math.log(2.0) for p in probType ])

print("entropy Type",entropyType )

probDoors= [ float(Doors.count(c)) / len(Doors) for c in dict.fromkeys(list(Doors)) ]
       
entropyDoors = - sum([ p * math.log(p) / math.log(2.0) for p in probDoors ])

print("entropy Doors",entropyDoors)

probTyres= [ float(Tyres.count(c)) / len(Tyres) for c in dict.fromkeys(list(Tyres)) ]
       
entropyTyres = - sum([ p * math.log(p) / math.log(2.0) for p in probTyres ])

print("entropy Tyres",entropyTyres)

igcolor  = info_gain.info_gain(Color, Class)
print ("Color Info Gain", igcolor)

igtype  = info_gain.info_gain(Type, Class)
print ("Type Info Gain", igtype)

igdoors  = info_gain.info_gain(Doors, Class)
print ("Doors Info Gain", igdoors)

igtyres  = info_gain.info_gain(Tyres, Class)
print ("Tyres Info Gain", igtyres)




