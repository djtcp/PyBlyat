def process_link(link):
    # Убираем пробелы в начале и конце строки
    link = link.strip()

    # Заслайсим для получения только 'www'
    www = link[:3]
    print(www)

    # Заслайсим для получения только 'google'
    google = link[4:10]
    print(google)

    # Заслайсим для получения только '.com'
    dot_com = link[-4:16]
    print(dot_com)

    # Убираем все пробелы
    link = link.replace(' ', '')
    print(link)


link = 'www google.com '
process_link(link)