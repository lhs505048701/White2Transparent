from PIL import Image
import os

for filename in os.listdir(r'C:/Users/Linn/Desktop/gif_loading_refresh_aiqiyi'):
  img = Image.open('C:/Users/Linn/Desktop/gif_loading_refresh_aiqiyi/'+ filename)
  img = img.convert("RGBA")
  print('C:/Users/Linn/Desktop/gif_loading_refresh_aiqiyi/'+ filename)
  pixdata = img.load()


  for y in range(img.size[1]):
    for x in range(img.size[0]):
      if pixdata[x,y][0]==255 and pixdata[x,y][1]==255 and pixdata[x,y][2]==255 and pixdata[x,y][3]==255:
        pixdata[x,y] = (255, 255, 255, 0)
    try:
    	img.save("C:/Users/Linn/Desktop/gif_loading_refresh_trans/icon_frame_"+filename, "PNG")
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
