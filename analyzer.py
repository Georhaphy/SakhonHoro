listofyearpillar = []
dictofmonth = {"01":"มกราคม", "02":"กุมภาพันธ์", "03":"มีนาคม", "04":"เมษายน", "05":"พฤษภาคม", "06":"มิถุนายน",
     "07":"กรกฎาคม", "08":"สิงหาคม", "09":"กันยายน", "10":"ตุลาคม", "11":"พฤศจิกายน", "12":"ธันวาคม"} 
day1 = '0'
def calyearpillar(day,month,year) :
     global day1
  if len(day) == 1:
      day1 = str(0)+str(day)
  
  year1 = int(year)-543
  month1= [k for k,v in dictofmonth.items() if v == month]
  yearraw = int(str(year1)+str(*month1)+str(day1))
  if yearraw - int(str(year1)+str('02')+str('04')) >= 0:
      yeartocal =   yearraw  
  else :
      yeartocal =   yearraw-1
  yearpillar = (yeartocal%60)-3
  return  yearpillar
