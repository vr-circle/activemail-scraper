import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


# configs - 適宜変更してください
activemail_url = "https://wam.u-hyogo.ac.jp/am_bin/amlogin"
user_id = "xx00x000"
passwd = "********"
webhook_url = "https://discord.com/api/webhooks/..."


def main():
    options = Options()
    options.add_argument('--headless')
    # cron で動かそうとすると executable_path を指定する必要がある．
    driver = webdriver.Chrome(options=options)

    # 受信したメールの件名を保存したテキストファイルを開く．ないなら作ろう．
    f = open("./received_mail_titles.txt", "a+", encoding="utf-8")
    f.seek(0)
    received_mail_titles = f.read().splitlines()

    # Active!mail にアクセス
    driver.get(activemail_url)

    # ユーザID入力
    driver.find_element_by_xpath(
        "/html/body/form/div[3]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/input"
    ).send_keys(user_id)

    # パスワード入力
    driver.find_element_by_xpath(
        "/html/body/form/div[3]/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/input"
    ).send_keys(passwd)

    # 姫路工学キャンパスを選択
    Select(driver.find_element_by_xpath(
        "/html/body/form/div[3]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select"
    )).select_by_visible_text("steng.u-hyogo.ac.jp(姫路工学:学生)")

    # ログイン
    driver.find_element_by_xpath(
        "/html/body/form/div[3]/table[1]/tbody/tr[2]/td/table/tbody/tr[5]/th[2]/input"
    ).click()

    # メールタイトルがレンダリングされるまで待つ．TODO: WebDriverWait で書き換える
    import time
    time.sleep(20)

    # iframe にフォーカスする．これによりメールを指定できるようになる．．
    iframe = driver.find_element_by_id('contentIframe')
    driver.switch_to.frame(iframe)

    for i in range(2, 12):
        # メールを巡回する
        mail_title = driver.find_element_by_xpath(
            "/html/body/div[1]/div[12]/div[2]/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[" + str(i) + "]/td[6]"
        )

        # 新着メール判別
        if mail_title.text not in received_mail_titles:
            # メールを展開
            mail_title.click()
            # 展開されるまで待機
            time.sleep(5)
            # メール本文エリアを指定
            mail_content = driver.find_element_by_xpath(
                "/html/body/div[1]/div[14]/div[2]/tt"
            )

            # Discord に配信する．
            content = {
                "username": mail_title.text,
                "content": mail_content.text[:500]
            }
            requests.post(webhook_url, content)

            # 受信したメールリストに追加
            f.write(mail_title.text + "\n")

    f.close()
    driver.close()


if __name__ == '__main__':
    main()
