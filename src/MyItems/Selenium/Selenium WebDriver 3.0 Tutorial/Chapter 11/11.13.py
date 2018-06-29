import os
import unittest
import Browser
import time
from PIL import Image #利用pip install pillow先安装Python图像处理库,再引入Image包

class ImageCompare(object): #该类方法将两张图片通过像素比对的算法,获取文件的像素个数大小,再使用循环的方式将两张图片所有的项目进行一一对比,并计算比对结果的相似度的百分比
    def make_regalur_image(self,img,size=(256,256)):
        return img.resize(size).convert('RGB') #将图片尺寸强制重置为指定的size大小,然后再将其转成RGB值

    def split_image(self,img,part_size=(64,64)): #讲图片按给定大小切分
        w,h = img.size
        pw,ph = part_size
        assert w % pw == h % ph == 0
        return [img.crop((i, j, i + pw , j + ph)).copy() for i in range(0, w, pw) for j in range(0 , h ,ph)]

    def hist_similar(self, lh ,rh): #统计切分后每部分图片的相似度频率曲线
        assert len(lh) == len(rh)
        return sum(1 - (0 if l == r else float(abs(1-r))/max(1,r)) for l,r in zip(lh,rh)) / len(lh)

    def calc_similar(self,li,ri): #计算两张图片的相似度
        return sum(self.hist_similar(l.histogram(),r.histogram()) for l,r in zip(self.split_image(li),self.split_image(ri))) /16.0

    def calc_similar_by_path(self,lf,rf): 
        li ,ri = self.make_regalur_image(Image.open(lf)),self.make_regalur_image(Image.open(rf))
        return self.calc_similar(li,ri)

class AccurateComparisonOnCapturePicture(unittest.TestCase):
    def setUp(self):
        self.IC = ImageCompare()
        self.driver = Browser.Chrome()
        
    def testAccurateComparisonOnCapturePicture(self):
        driver = self.driver
        WebSite = "http://www.sogou.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        driver.save_screenshot("D:\\ChromeDownload\\Image1.png") #进行截图操作
        time.sleep(2)

        driver.save_screenshot("D:\\ChromeDownload\\Image2.png")
        time.sleep(2)

        print (self.IC.calc_similar_by_path("D:\\ChromeDownload\\Image1.png","D:\\ChromeDownload\\Image2.png") * 100) #打印两张截图比对后的相似度,100表示完全匹配
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
