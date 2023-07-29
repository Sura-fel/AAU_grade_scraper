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

import scraper
scraper.scrape(args)