import gtts
from gtts import gTTS
from art import tprint  # украшательство (шрифты)
import pdfplumber
from pathlib import Path  # для проверки что по указанному пути есть файл


def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'Формат файла PDF'
        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Processing...')

        # читаем pdf файл в обычную строку. В параментрах открываем файл на чтение в двоичном режиме флагом rb
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:

            # пробегаемя по всем страницам и извлекаем текст из каждой
            pages = [page.extract_text() for page in pdf.pages]

        # склеиваем все страницы воедино
        text = ''.join(pages)

        #
        # with open('text1.txt', 'w') as file:
        #     file.write(text)

        # сохраним текст и заменим все реплейсы на пустоту
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)

        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!\n'

        # with open('text2.txt', 'w') as file:
        #     file.write(text)
    else:
        return 'Файл не PDF формата'


def main():
    tprint('PDF>>TO>>MP3', font='block')
    file_path = input("\n Enter a file's path:")
    language = input("Choose the language of your PDF. For example 'ru' or 'en': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
