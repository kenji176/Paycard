import io
import imghdr
import datetime
import requests
from PIL import Image,ImageDraw,ImageFont





class card:
    def __init__(self):#下準備
        self.img_format = ["png","PNG","jpg","JPG","jpeg","JPEG","gif","GIF","webp","WEBP"]
        self.offset = 2
        self.font = ImageFont.truetype(r'Font\BIZ-UDGOTHICB.TTC',80)
        self.yen_font = ImageFont.truetype(r'Font\BIZ-UDGOTHICB.TTC',300)

    def paypay(self,True_or_False,image_url,name,amount):
        if True_or_False=="True":
            Tpay_im = Image.open(r'Image\PayPay0.png')
            dt_now = datetime.datetime.now()
            Byte_Image = io.BytesIO(requests.get(image_url).content)
            Res_Image = Image.open(Byte_Image).convert('RGBA')
            mask = Image.new("L", Res_Image.size)
            draw = ImageDraw.Draw(mask)
            draw.ellipse([(self.offset, self.offset), (Res_Image.size[0] - self.offset, Res_Image.size[1] - self.offset)], 255)
            Res_Image.putalpha(mask)
            Res_Image = Res_Image.resize((500,500))
            Tpay_im.paste(Res_Image,(round(Tpay_im.size[0]/2-Res_Image.size[0]/2),50),Res_Image)
            draw = ImageDraw.Draw(Tpay_im)
            draw.text((round(Tpay_im.size[0]/2-draw.textsize(f"{name}さんから支払い", self.font)[0]/2),700),f"{name}さんから支払い", fill=(0, 0, 0),font=self.font)
            draw.text((round(Tpay_im.size[0]/2-draw.textsize(f"{amount}円", self.yen_font)[0]/2),900),f"{amount}円", fill=(0, 0, 0),font=self.yen_font)
            draw.text((round(Tpay_im.size[0]/2-draw.textsize(dt_now.strftime('%Y年%m月%d日 %H時%M分%S秒'), self.font)[0]/2),1830),dt_now.strftime('%Y年%m月%d日 %H時%M分%S秒'), fill=(0, 0, 0),font=self.font)
            del draw
            image_bytes = io.BytesIO()
            Tpay_im.save(image_bytes,format="png")
            image_bytes.seek(0)
            return image_bytes
        else:
            dt_now = datetime.datetime.now()
            Fpay_im = Image.open(r'Image\PayPay1.png')
            Byte_Image = io.BytesIO(requests.get(image_url).content)
            if [n for n in self.img_format if n == imghdr.what(None, h=Byte_Image.getvalue())]:#画像判定
                Res_Image = Image.open(Byte_Image).convert('RGBA')
                mask = Image.new("L", Res_Image.size)
                draw = ImageDraw.Draw(mask)
                draw.ellipse([(self.offset, self.offset), (Res_Image.size[0] - self.offset, Res_Image.size[1] - self.offset)], 255)
                #del draw
                Res_Image.putalpha(mask)
                Res_Image = Res_Image.resize((500,500))
                Fpay_im.paste(Res_Image,(round(Fpay_im.size[0]/2-Res_Image.size[0]/2),50),Res_Image)
                draw = ImageDraw.Draw(Fpay_im)
                draw.text((round(Fpay_im.size[0]/2-draw.textsize(f"{name}さんから支払い", self.font)[0]/2),700),f"{name}さんから支払い", fill=(0, 0, 0),font=self.font)
                draw.text((round(Fpay_im.size[0]/2-draw.textsize(f"{amount}円", self.yen_font)[0]/2),900),f"{amount}円", fill=(0, 0, 0),font=self.yen_font)
                draw.text((round(Fpay_im.size[0]/2-draw.textsize(dt_now.strftime('%Y年%m月%d日 %H時%M分%S秒'), self.font)[0]/2),1830),dt_now.strftime('%Y年%m月%d日 %H時%M分%S秒'), fill=(0, 0, 0),font=self.font)
                del draw
                image_bytes = io.BytesIO()
                Fpay_im.save(image_bytes,format="png")
                image_bytes.seek(0)
                return image_bytes
            else:
                print("指定されたURLには画像データが存在しません")
        # MyClass のインスタンスを生成
