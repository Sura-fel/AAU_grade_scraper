import requests, lxml.html
from pandas import read_html
import argparse

parser = argparse.ArgumentParser(
    usage="%(prog)s -u 'Username' -P 'password' [-o file_name]",
    description="Scrape your grade from portal.aau.edu.et"
    )

parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s 1.0'
    )   
parser.add_argument(
    '--username',
    '-u',
    required=True,
    help='Pass your username for the portal.'
    )
parser.add_argument(
    '--password',
    '-p',
    required=True,
    help='Pass your password for the portal.'
    )
parser.add_argument(
    '--output',
    '-o',
    required=False,
    default="Grade",
    help='Specify filename which your grades will be saved into.'
    )

args = parser.parse_args()

login_url = 'https://portal.aau.edu.et/login'
home_url = 'https://portal.aau.edu.et/Home'
grade_url = 'https://portal.aau.edu.et/Grade/GradeReport'

aa = requests.session()
login = aa.get(login_url)

login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')

form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
form['UserName'] = args.username
form['Password'] = args.password

response = aa.post(login_url,data=form)
grade_html = aa.get(grade_url).content

df_list = read_html(grade_html)

for i, df in enumerate(df_list):
    df.to_csv('{}{}.csv'.format(args.output,i))
    print('saved to {}{}.csv'.format(args.output,i))