import pytest
from main import get_cat_image

def test_get_cat_image_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    cat_image_data = get_cat_image()
    assert cat_image_data == 'https://example.com/cat.jpg'

def test_get_cat_image_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    cat_image_data = get_cat_image()
    assert cat_image_data == None


