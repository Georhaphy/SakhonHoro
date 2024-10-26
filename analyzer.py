import streamlit as st

def calyearpillar(date,month,year):
  dictofyear= {7:"rat",8:"ox" ,9:"tiger" ,10:"rabbit" ,11:"dragon",0:"snake" ,1:"horse" ,2:"goat" ,3:"monkey" ,4:"rooster",5:"dog" , 6:"pig" }
  dictofyearelement = {7:"jia",8:"yi",9:"bing",0:"ding",1:"wu",2:"ji",3:"geng",4:"xin",5:"ren",6:"gui"}
  dictofearthlybranch =  {"rat":"https://img5.pic.in.th/file/secure-sv1/rat.jpg",
                         "ox":"https://img2.pic.in.th/pic/ox.jpg",
                         "tiger":"https://img2.pic.in.th/pic/tiger.jpg",
                        "rabbit":"https://img5.pic.in.th/file/secure-sv1/rabb.jpg",
                        "dragon":"https://img5.pic.in.th/file/secure-sv1/dragon.jpg",
                        "snake":"https://img5.pic.in.th/file/secure-sv1/snakebc3e231e3c143f8d.jpg",
                        "horse":"https://img2.pic.in.th/pic/horse.jpg",
                       "goat":"https://img5.pic.in.th/file/secure-sv1/wei.jpg",
                     "monkey":"https://img5.pic.in.th/file/secure-sv1/monkey.jpg",
                    "rooster":"https://img5.pic.in.th/file/secure-sv1/chick.jpg",
                        "dog":"https://img2.pic.in.th/pic/dog8c608a2c4b6d5657.jpg",
                        "pig":"https://img2.pic.in.th/pic/pig.jpg"
                        }

  dictofpichiddenstem =  {"rat":"https://img5.pic.in.th/file/secure-sv1/hiddenrat.jpg",
                         "ox":"https://img5.pic.in.th/file/secure-sv1/hiddenox.jpg",
                         "tiger":"https://img5.pic.in.th/file/secure-sv1/hiddentiger.jpg",
                     "rabbit":"https://img5.pic.in.th/file/secure-sv1/hiddenrabb.jpg",
                      "dragon":"https://img5.pic.in.th/file/secure-sv1/hiddendragon.jpg",
                      "snake":"https://img2.pic.in.th/pic/hiddensnake.jpg",
                      "horse":"https://img2.pic.in.th/pic/hiddenhorse.jpg",
                      "goat":"https://img2.pic.in.th/pic/hiddengoat.jpg",
                   "monkey":"https://img5.pic.in.th/file/secure-sv1/hiddenmonkey.jpg",
                      "rooster":"https://img5.pic.in.th/file/secure-sv1/hiddenchick.jpg",
                      "dog":"https://img5.pic.in.th/file/secure-sv1/hiddendog.jpg",
                      "pig":"https://img5.pic.in.th/file/secure-sv1/hiddenpig.jpg"
                      }
  dictofpictelement = {"jia":"https://img5.pic.in.th/file/secure-sv1/jia.jpg",
                      "yi":"https://img5.pic.in.th/file/secure-sv1/yi.jpg",
                    "bing":"https://img5.pic.in.th/file/secure-sv1/bing.jpg",
                    "ding":"https://img2.pic.in.th/pic/ding.jpg",
                      "wu":"https://img5.pic.in.th/file/secure-sv1/wu.jpg",
                      "ji":"https://img5.pic.in.th/file/secure-sv1/ji.jpg",
                    "geng":"https://img5.pic.in.th/file/secure-sv1/geng.jpg",
                     "xin":"https://img2.pic.in.th/pic/xin.jpg",
                     "ren":"https://img2.pic.in.th/pic/ren.jpg",
                     "gui":"https://img2.pic.in.th/pic/gui.jpg"
                      }
  return st.write(dictofyear[int(year)%12])
  #st.write(dictofyearelement[int(str(a)[-1])])
  #st.write(dictofpictelement[dictofyearelement[int(str(a)[-1])]])
