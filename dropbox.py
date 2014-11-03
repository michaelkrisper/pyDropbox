#!/usr/bin/python3
# coding=utf-8
"""
Splinter access to dropbox
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-11-03"

import time
import config
from splinter import Browser

def main():
    with Browser() as browser:
        browser.visit("https://www.dropbox.com/login")
        browser.find_by_css('.text-input-input').first.type(config.USERNAME)
        browser.find_by_css('.password-input').first.type(config.PASSWORD)
        browser.find_by_css('.login-button').first.click()

        browser.is_text_present('TUGShare_UPLOAD', wait_time=10)

        browser.find_link_by_text('TUGShare_UPLOAD').first.click()

        browser.find_by_value('TUGShare_UPLOAD')

        browser.find_by_id("global_share_button").click()

        time.sleep(15)

        print(len(browser.find_by_css("bubble_picker")))


if __name__ == "__main__":
    main()