import traceback
from src.constants import TaskStatus

from .base_service import BaseService
from src.exceptions import ErrorCode, WebapiException

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieSuggestService(BaseService):
    def suggest_movie(self, title):
        try:
            df = pd.read_csv('data/movie_dataset.csv')
            self.pre_processing(df)

            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df["combined_features"])
            cosine_sim = cosine_similarity(count_matrix)
            movie_index = self.get_index_from_title(df,title)
            similar_movies = list(enumerate(cosine_sim[movie_index]))
            
            sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)
            result_movie = []
            for movie in sorted_similar_movies[:5]:
                result_movie.append(self.get_title_from_index(df, movie[0]))
            return result_movie
        except: 
            raise WebapiException(ErrorCode.INVALID_CONTENT_FORMAT)

    def pre_processing(self,df):
        features = ['keywords', 'cast', 'genres', 'director']
        for feature in features:
            df[feature] = df[feature].fillna('')
        df["combined_features"] = df.apply(self.combined_features, axis =1)
  
    def combined_features(self, row):
        return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']

    def get_index_from_title(self,df,title):
        return df[df.title == title]["index"].values[0]
    
    def get_title_from_index(self,df,index):
        return df[df.index == index ]["title"].values[0]