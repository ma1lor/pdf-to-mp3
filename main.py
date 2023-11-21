from pathlib import Path
import pdfplumber
from gtts import gTTS


def pdftomp3(file_path='tet.pdf', language = 'en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'File exists'
        print(f'[+] proccesing')
        with pdfplumber.PDF(open(Path(file_path), mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)

        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        with open('text.txt', 'w') as file:
            file.write(text)
        return f'[+] {file_name}.mp3 saved successfully! \n ---Have a good day!'

    else:
        return 'File does not exist'
    






def main():
    print(1)
    print(pdftomp3(file_path='files\Robert_Louis_Stevenson_-_Treasure_Island.pdf'))











if __name__ == "__main__":
    main()

