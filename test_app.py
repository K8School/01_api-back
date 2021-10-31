import main

def test_sentiment():
    test_str: str = "That was awesome!"
    response = main.calc_sentiment(test_str)
    assert response.phrase == test_str
    assert response.sentiment == 1.0


