import speech_recognition
from datetime import datetime
import webbrowser

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands': {
        'greeting': ['привет', 'дарова'],
        'create_task': ['открой файл', 'открой блокнот', 'файл', 'блокнот'],
        'time': ['время', 'сколько время', 'часы', 'сколько часов', 'часов'],
        'open_bloomberg': ['открой браузер', 'браузер', 'американское телевидение', 'открой американское телевидение'],
        'open_wdr': ['открой немецкое телевидение', 'немецкое телевидение'],
        'open_youtube': ['открой ютуб', 'ютуб', 'ютубчик']
    }
}
def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

        return query

    except speech_recognition.UnknownValueError:
        return 'Damnn... Не понял что ты сказал'

def greeting():
    return 'Привет братуха'


def open_bloomberg():
    return webbrowser.open('https://www.bloomberg.com/live/europe')


def open_wdr():
    return webbrowser.open('https://www1.wdr.de/fernsehen/livestream/index.html')


def open_youtube():
    return webbrowser.open('https://www.youtube.com')


def time():
    current_datetime = datetime.now()
    return f"Сеачас: {current_datetime}"


def create_task():
    print('Что запишим в файл')

    query = listen_command()

    with open('Task', 'a') as file:
        file.write(f"{query}\n")
    return f"Данные записаны в файл"


def main():
    query = listen_command()
    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())


if __name__ == '__main__':
    main()