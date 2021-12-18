import pytest
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db
from unittest.mock import MagicMock


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(db.session)
    movie1 = Movie(id=1,
                   title="movie1",
                   description="movie1_description",
                   trailer="movie1_trailer",
                   year=2021,
                   rating=10,
                   genre_id=1,
                   genre="Genre1",
                   director_id=1,
                   director="Director1")

    movie2 = Movie(id=2,
                   title="movie2",
                   description="movie2_description",
                   trailer="movie2_trailer",
                   year=2022,
                   rating=11,
                   genre_id=2,
                   genre="Genre2",
                   director_id=2,
                   director="Director2")

    movie3 = Movie(id=3,
                   title="movie3",
                   description="movie3_description",
                   trailer="movie3_trailer",
                   year=2023,
                   rating=12,
                   genre_id=3,
                   genre="Genre3",
                   director_id=3,
                   director="Director3")

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(returm_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService():
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        breakpoint()
        movie = self.movie_service.get_one(1)

