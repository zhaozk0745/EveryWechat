# coding=utf-8
from GFWeather import gfweather


def run():

    gfweather().run()


def test_run():

    gfweather().start_today_info(is_test=False)

if __name__ == '__main__':
    # test_run()
    run()



