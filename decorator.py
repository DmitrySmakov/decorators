from datetime import datetime
from functools import wraps
import requests


def logger(function):
    @wraps(function)
    def new_function(*a, **b):
        file_name = 'output.txt'
        with open(file_name, 'a') as output:
            date_time = datetime.now()
            result = function(*a, **b)
            res = f'Вызов функции {function.__name__}, время - {date_time}, параметры: {a},{b} рузультат: {result} \n'
            output.write(res)
            print(str)
        return result
    return new_function


def logger_with_param(file_name):
    def logger(function):
        @wraps(function)
        def new_function(*a, **b):
            with open(file_name, 'a') as output:
                date_time = datetime.now()
                result = function(*a, **b)
                res = f'Вызов функции {function.__name__},время:{date_time}, параметры: {a},{b}, рузультат: {result}\n'
                output.write(res)
                print(str)
            return result
        return new_function
    return logger


@logger_with_param(file_name='output.txt')
def most_intelligence(names: list, token):
    power_tmp = 0
    hero = ''
    for name in names:
        request_uri = f"https://superheroapi.com/api/{token}/search/" + name  # 'Thanos'
        response = requests.get(request_uri)
        dic = response.json()
        power = int(dic['results'][0]['powerstats']['intelligence'])
        print(f'{name}: {power}')
        if power_tmp < power:
            hero = name
            power_tmp = power
    print(f'Самый умный {hero}: {power_tmp}')


if __name__ == '__main__':
    file_name = 'output.txt'
    names = ['Hulk', 'Captain America', 'Thanos']
    token = 2619421814940190
    most_intelligence(names, token)
