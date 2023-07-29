import argparse
import requests_html as rh
import pandas as pd

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


session = rh.HTMLSession()
login_response = session.get(login_url)
hidden = login_response.html.find('form input[type="hidden"]',first=True)

form = {hidden.attrs["name"]: hidden.attrs["value"]}
form['UserName'] = args.username
form['Password'] = args.password


response = session.post(login_url,data=form)
grade_html = session.get(grade_url).content

df = pd.read_html(grade_html)[0]
df.to_csv('{}.csv'.format(args.output))
print('saved to {}.csv'.format(args.output))
