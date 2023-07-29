import requests_html as rh
import pandas as pd

login_url = 'https://portal.aau.edu.et/login'
home_url = 'https://portal.aau.edu.et/Home'
grade_url = 'https://portal.aau.edu.et/Grade/GradeReport'

def scrape(args):
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
