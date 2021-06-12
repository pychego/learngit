import exifread
import requests
import logging
from pprint import pprint
logging.basicConfig(level=logging.INFO)

class GetphotoGps:
    def __init__(self, photo):
        self.photo = photo
        self.ak = 'wast7e2bTIRK80KiBKpiHdEtyumbptTy'
        self.location = [37.42118833333333, 112.58349608333333]

    def get_location(self):
        params = {
            'ak': self.ak,
            'output': 'json',
            'coordtype': 'bd09ll',
            'extensions_town': 'true',
            'extensions_road': 'true'
        }
        url = 'http://api.map.baidu.com/reverse_geocoding/v3/?location={},{}'\
        .format(*self.location)
        response = requests.get(url, params=params)
        logging.info(pprint(response.json()))

if __name__ == '__main__':
    main = GetphotoGps('zhu3.jpg')
    main.get_location()