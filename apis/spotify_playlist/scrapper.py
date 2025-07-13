import random

from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime as dt, timedelta


class BillboardScrapper:

    def __init__(self):
        self.date = self.get_date()
        self.soup = self.get_parser()
        self.songs = self.get_song_titles()
        self.bands = self.get_band_names()

    def get_date(self) -> str:
        """Asks the user for a date to scan. If invalid, uses today's ranking"""
        travel_date = input("What day would you like to scan? (YYYY-MM-DD)\n")
        # years to consider 1970 and older
        date_format = re.compile('^(19[7-9][0-9]|20[0-2][0-9])-((0[1-9])|(1[0-2]))-([0-2][1-9]|3[0-1])$')
        if not date_format.match(travel_date):
            print("Invalid date format - assuming today's date")
            return (dt.now() - timedelta(days=1)).strftime(format='%Y-%m-%d')
        return travel_date

    def date_has_ranking(self) -> bool:
        """Validates if that dates has songs in the ranking"""
        return len(self.get_song_titles()) > 0

    def get_yesterdays_top(self):
        """The selected date has no ranking, check the day before"""
        current_date = dt.strptime(__date_string=self.date, __format='%Y-%m-%d')
        self.date = (current_date - timedelta(days=1)).strftime(format='%Y-%m-%d')
        self.get_parser()

    def get_parser(self):
        """ Gets the ranking for the specified date and returns the soup object"""
        # print(f"Checking ranking for {self.date}")
        top100 = requests.get(url=f"https://www.billboard.com/charts/hot-100/{self.date}/")
        top100.raise_for_status()
        self.soup = BeautifulSoup(top100.content, "html.parser")
        if self.date_has_ranking():
            return self.soup
        else:
            self.get_yesterdays_top()

    def get_song_titles(self) -> list:
        """Scraps the billboard Top 100 for song titles and return a clean list of songs"""
        raw_song_titles = self.soup.find_all(name="h3", class_=re.compile(
            'c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 *'))
        return [re.sub(pattern='[\t|\n]*', repl='', string=song.getText()) for song in raw_song_titles]

    def get_band_names(self) -> list:
        """Scraps the billboard Top 100 for the band names and returns a clean list of bands"""
        raw_band_names = self.soup.find_all(name="span", class_=re.compile(
            'c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max *'))
        return [re.sub(pattern='[\t|\n]*', repl='', string=band.getText()) for band in raw_band_names]

    def band_song_combined(self) -> list:
        return [f"{self.bands[_]} - {self.songs[_]}" for _ in range(0, len(self.songs))]
