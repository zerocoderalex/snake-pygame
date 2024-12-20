import requests

def get_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Извлекаем URL изображения
        cat_image_url = data[0]['url']
        return cat_image_url
    else:
        print(f"Ошибка при получении изображения: {response.status_code}")
        return None

# Пример использования
if __name__ == "__main__":
    cat_image = get_cat_image()
    if cat_image:
        print(f"Случайное изображение кошки: {cat_image}")
