import math,os
from time import time

def calcular_distancia(lat1,lon1,lat2,lon2):
  rad=math.pi/180
  dlat=lat2-lat1
  dlon=lon2-lon1
  R=6372.795477598
  a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
  distancia=2*R*math.asin(math.sqrt(a))*1000
  return distancia
