import requests_html as rh
import pdfkit


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
    filename = args.output

    
    response = session.post(login_url,data=form)
    grade_html = session.get(grade_url)
    tables_html = grade_html.html.find('table')
    for i,tabel_html in enumerate(tables_html):
        tabel_html = tabel_html.html.replace('\xa0',' ')
        pdfkit.from_string(tabel_html,'{}{}.pdf'.format(filename, i))