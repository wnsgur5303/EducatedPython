import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/product/detect'
MYAPP_KEY = '15846e51cb8ace77e040eaac2bb7fbbf'

def detect_product(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

def show_products(image_url, detection_result):
    try:
        image_resp = requests.get(image_url)
        image_resp.raise_for_status()
        file_jpgdata = BytesIO(image_resp.content)
        image = Image.open(file_jpgdata)
    except Exception as e:
        print(str(e))
        sys.exit(0)

    draw = ImageDraw.Draw(image)
    for obj in detection_result['result']['objects']:
        x1 = int(obj['x1']*image.width)
        y1 = int(obj['y1']*image.height)
        x2 = int(obj['x2']*image.width)
        y2 = int(obj['y2']*image.height)
        draw.rectangle([(x1,y1), (x2, y2)], fill=None, outline=(255,0,0,255))
        draw.text((x1+5,y1+5), obj['class'], (255,0,0))
    del draw
    return image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect Products.')
    parser.add_argument('image_url', type=str, nargs='?',
        default="http://seoulfashionfestival.co.kr/wp-content/uploads/2017/08/Top-10-Street-Style-Trends-From-AW-2017-Fashion-Weeks-770x450.jpg",
        help='image url to show product\'s rect')

    args = parser.parse_args()

    detection_result = detect_product(args.image_url)
    image = show_products(args.image_url, detection_result)
    image.show()