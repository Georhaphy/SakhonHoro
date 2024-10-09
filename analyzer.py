listofyearpillar = []


def calyearpillar(day,month,year) :
  if len(day) = 1:
      day1 = str(0)+str(day)
  if len(month) = 1:
      month1 = str(0)+str(month) 
  year1 = int(year)-543
  yearraw = int(str(year1)+str(month1)+str(day1))
  if yearraw - int(str(year1)+str(02)+str(04)) >= 0:
      yeartocal =   yearraw  
  else :
      yeartocal =   yearraw-1
  yearpillar = (yeartocal%60)-3
  return  yearpillar
