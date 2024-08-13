from bs4 import BeautifulSoup
import requests
from googletrans import Translator


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find(name='div', id='random_word').text.strip()
        word_definition = soup.find(name='div', id='random_word_definition').text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Игра началась")
    while True:
        word_dict = get_english_words()
        word_en = word_dict.get("english_word")
        word_definition_en = word_dict.get('word_definition')
        translator = Translator()
        word = translator.translate(word_en, dest='ru').text
        word_definition = translator.translate(word_definition_en, dest='ru').text

        print(f"Значение слова: {word_definition}")
        user = input("Ваш ответ: ")
        if user == word:
            print("Правильно")
        else:
            print("Неправильно")
            print(f"Правильное значение: {word}")
        play_again = input("Играем еще? (д/н)")
        if play_again != 'д':
            print("Спасибо за игру!")
            break

word_game()






# page = requests.get(url)
# html = page.text
# soup = BeautifulSoup(html, 'html.parser')
#
# links = soup.find_all('a')
#
# for link in links:
#     print(link.get('href'))

