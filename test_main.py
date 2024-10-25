from python_library.average import average, calculate_time_memory

data_path = "data/movie_ratings_16_17.csv"


def test_average():
    result = average("data/movie_ratings_16_17.csv")
    expected_result = 53.62

    assert result == expected_result, "Test has failed."


def test_calculate_time_memory():
    result = calculate_time_memory("data/movie_ratings_16_17.csv")

    assert result is not None, "Test has failed."


if __name__ == "__main__":
    test_average()
    test_calculate_time_memory()
