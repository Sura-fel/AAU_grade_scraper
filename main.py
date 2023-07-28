import requests, lxml.html
import pandas as pd

username = "YOUR_USER_ID" #UGR/0000/00
password = "YOUR_PASSWORD" #1234
login_url = 'https://portal.aau.edu.et/login'
home_url = 'https://portal.aau.edu.et/Home'
grade_url = 'https://portal.aau.edu.et/Grade/GradeReport'

aa = requests.session()

login = aa.get(login_url)
login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

form['UserName'] = username
form['Password'] = password

response = aa.post(login_url,data=form)
grade_html = aa.get(grade_url).content
df_list = pd.read_html(grade_html)

for i, df in enumerate(df_list):
    print(df)
    df.to_csv('table {}.csv'.format(i))

