import unittest
from appium import webdriver
desired_caps = dict(
    platformName='Android',
    platformVersion='10',
    automationName='uiautomator2',
    deviceName='Android Emulator',
    app=PATH("C:/Users/user/Downloads/Chess_v2.7.4_apkpure.com.apk")
    )
self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
C:\\Usersuser\\Downloads\\Chess_v2.7.4_apkpure.com.apk



	