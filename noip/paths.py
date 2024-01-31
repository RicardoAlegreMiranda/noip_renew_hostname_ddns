class Paths:
    URL = "https://www.noip.com/"
    USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36")

    BTN_LOGIN = '//*[@id="topnav"]/li[1]/a'
    TEXT_AREA_USERNAME = '//*[@id="username"]'
    TEXT_AREA_PASSWORD = '//*[@id="password"]'
    BTN_SUBMIT = '//*[@id="clogs-captcha-button"]'
    LOGIN_ERROR = '//*[@id="sign-up-wrap"]/div[2]/div[2]'
    DASHBOARD = '//*[@id="dashboard-nav"]'
    BTN_HOST_NAME = '//*[@id="content-wrapper"]/div[4]/div/div/div/div[4]/button[1]'
    BTN_CONFIRM = '//*[@id="host-panel"]/table/tbody/tr/td[6]/button[1]'
    LABEL_LAST_UPDATE = '//*[@id="host-panel"]/table/tbody/tr/td[2]/span[2]/span'
