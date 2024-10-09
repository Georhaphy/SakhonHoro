listofyearpillar = []
dictofmonth = {"01":"มกราคม", "02":"กุมภาพันธ์", "03":"มีนาคม", "04":"เมษายน", "05":"พฤษภาคม", "06":"มิถุนายน",
     "07":"กรกฎาคม", "08":"สิงหาคม", "09":"กันยายน", "10":"ตุลาคม", "11":"พฤศจิกายน", "12":"ธันวาคม"} 

def calyearpillar(day,month,year) :
  if len(day) == 1:
      day1 = str(0)+str(day)
  
  year1 = int(year)-543
  yearraw = int(str(year1)+str((dictofmonth.values()).index(month))+str(day1))
  if yearraw - int(str(year1)+str('02')+str('04')) >= 0:
      yeartocal =   yearraw  
  else :
      yeartocal =   yearraw-1
  yearpillar = (yeartocal%60)-3
  return  yearpillar
