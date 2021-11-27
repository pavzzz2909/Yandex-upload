import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str, file_path: str):
        self.token = token
        self.file_path = file_path

    def get_headers(self):
        return {
                'Content-Type':'application/json',
                'Authorization':'OAuth {}'.format(self.token)
        }

    def get_params(self):
        return {
                'path':file_path,
                'overwrite':'true'
        }

    def upload_file(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        files_url='https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = self.get_params()
        response = requests.get(url=files_url, headers=headers, params=params).json()
        pprint(response)
        upload = requests.put(url=response['href'], data=open(file_path, 'rb'), params=params, headers=headers)
        pprint(upload.status_code)

if __name__ == '__main__':
    file_path = input('Введите путь и название загружаемого файла\n')
    token = input('Введите токен пользователя\n')
    upload = YaUploader(token,file_path)
    result = upload.upload_file(file_path)
