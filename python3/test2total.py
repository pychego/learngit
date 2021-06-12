import exifread
from pprint import pprint
import logging
import requests

logging.basicConfig(level=logging.INFO)


class Jpg2info:
    def __init__(self, path: 'image_path'):
        """
        path: 照片的路径
        ak: 百度地图ak
        """
        self.path = path
        self.ak = 'wast7e2bTIRK80KiBKpiHdEtyumbptTy'
        self.location = self.get_photo_gps()

    def get_photo_gps(self, ):
        """得到照片的经纬度信息"""
        with open(self.path, 'rb') as f:
            tags = exifread.process_file(f)
            try:
                lat = tags['GPS GPSLatitude'].printable[1:-1] \
                    .replace(" ", "").replace("/", ",").split(",")
                latitude = float(lat[0]) + float(lat[1]) / 60 \
                           + float(lat[1]) / float(lat[2]) / 3600

                lon = tags['GPS GPSLongitude'].printable[1: -1] \
                    .replace(' ', '').replace('/', ',').split(',')
                longitude = float(lon[0]) + float(lon[1]) / 60 \
                            + float(lon[1]) / float(lon[2]) / 3600
            except KeyError as e:
                logging.exception(e)
                return '照片不是原图或者是heic格式'
            else:
                return latitude, longitude



    def get_photo_info(self, ):
        info = {}
        with open(self.path, 'rb') as f:
            tags = exifread.process_file(f)
            try:
                info['time'] = tags['EXIF DateTimeOriginal']
                info['phone'] = tags['Image Make']
                info['model'] = tags['Image Model']
                print('Time:', info['time'])
                print('Phone:', info['phone'])
                print('Model:', info['model'])
                return info
            except KeyError as e:
                logging.exception(e)
                return '照片不是原图或者是heic格式'



    def get_location(self):
        params = {
            'ak': self.ak,
            'output': 'json',
            'coordtype': 'bd09ll',
            'extensions_town': 'true',
            'extensions_road': 'true'
        }
        url = 'http://api.map.baidu.com/reverse_geocoding/v3/?location={},{}' \
            .format(*self.location)
        response = requests.get(url, params=params).json()
        # response 是请求返回的信息
        address = response['result']['formatted_address']
        town = response['result']['addressComponent']['town']
        print('详细地址:' + address + '(' + town + ')')


if __name__ == '__main__':
    main = Jpg2info('zhu3.jpg')
    main.get_photo_info()
    main.get_location()
