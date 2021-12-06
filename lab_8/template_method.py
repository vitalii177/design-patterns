from abc import ABCMeta, abstractmethod
import pandas as pd


class Pipeline(metaclass=ABCMeta):
    def __init__(self):
        self.dataset = None
        self.columns = []

    def template_method(self):
        self.read_data()
        self.extract_features()
        column = str(input('Enter column name to visualize it\n> '))
        self.visualize_features(column)
        request = int(input('REQUESTS: 1-Special rows, 2-All rows\n> '))
        if request == 1:
            self.proceed_request_1()
        if request == 2:
            self.proceed_request_2()

    def read_data(self):
        file = 'playstation_4_games.csv'
        self.dataset = pd.read_csv(file)

    def extract_features(self):
        self.columns = self.dataset.columns

    def visualize_features(self, column):
        if column in self.columns:
            print(self.dataset[column])

    @abstractmethod
    def proceed_request_1(self, *args):
        pass

    @abstractmethod
    def proceed_request_2(self, *args):
        pass


class GenreProcessor(Pipeline):
    def proceed_request_1(self, *args):
        genres = self.dataset['Genre']
        games = self.dataset['GameName']
        genre_name = str(input('Enter Genre of the Game: '))
        for genre in genres:
            if genre_name == genre:
                print(f'{genre_name}\n{games}')

    def proceed_request_2(self, *args):
        genres = self.dataset['Genre']
        games = self.dataset['GameName']
        print('Genre\t\t\t\t\tGameName')
        for i in range(len(genres)):
            print(f'{genres[i]}\t\t\t\t\t{games[i]}')


class DeveloperProcessor(Pipeline):
    def proceed_request_1(self, *args):
        developers = self.dataset['Developer']
        games = self.dataset['GameName']
        developer_name = str(input('Enter Developer of the game: '))
        for developer in developers:
            if developer_name == developer:
                print(f'{developer_name}\n{games}')

    def proceed_request_2(self, *args):
        developers = self.dataset['Developer']
        games = self.dataset['GameName']
        print('Developer\t\t\t\t\tGameName\n')
        for i in range(len(developers)):
            print(f"{developers[i]}\t\t\t\t\t{games[i]}")


# The client code
processor_choice = int(input('COLUMNS: 1-Developer, 2-Genre\n> '))
if processor_choice == 1:
    processor = DeveloperProcessor()
    processor.template_method()
elif processor_choice == 2:
    processor = GenreProcessor()
    processor.template_method()
