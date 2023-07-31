# Scrape your grade from [AAU Portal](https://portal.aau.edu.et)
## Setup
clone the repository.
```sh
git clone https://github.com/Sura-fel/AAU_grade_scraper
```
Change directory.
```sh
cd AAU_grade_scraper
```
Install required 3rd party libraries.
```sh
pip3 install requirements.txt
```
Run the [main.py](https://github.com/Sura-fel/AAU_grade_scraper/blob/main/main.py) with the --username and --password args\(optionally add -o flag for output file name\) .
```sh
python main.py --username ugr/0000/00 --password 1234
```
## Requirements
- Python version 3.x, tested on python 3.11.4
- pip3, tested on pip3 23.2.1
