import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class TranscriptionAudio(APIView):
    def trascript(self):
        transcrib_body = {
            'part1': 'Сейчас мы поговорим об инструментах локального администрирования. В рамках данного урока мы познакомимся с шаблонами безопасности и научимся работать с ними. Создадим свой шаблон безопасности, научимся его экспортировать, импортировать и анализировать. Также познакомимся со средством командной строки редактора безопасности и вкратце рассмотрим параметры локальной групповой политики. Анализ и настройка безопасности – это оснастка консоли управления Microsoft, позволяющая анализировать и настраивать параметры безопасности на компьютерах с операционной системой Windows с помощью файлов шаблонов безопасности.',
            'part2': 'Состояние операционной системы и приложений на устройстве является динамическим. Например, может временно потребоваться изменить уровни безопасности, чтобы можно было немедленно устранить проблему, связанную с администрированием или сетью. Тем не менее, это изменение часто может отменять обратный переход. Это означает, что компьютер больше не будет отвечать требованиям для корпоративной безопасности. Регулярный анализ позволяет отслеживать и обеспечивать адекватный уровень безопасности на каждом компьютере по рамках программы управления рисками предприятия. Вы можете настроить уровни безопасности, и, что важнее, выявить изъяны системы безопасности, которые могут возникать в системе в течение определенных промежутков времени. С помощью средства анализа и настройки безопасности можете быстро просматривать результаты анализов. Они предоставляют рекомендации вместе с текущими системами параметрами и используют визуальные флаги или замечания для выбора тех областей, в которых текущие параметры не соответствуют предлагаемому уровню безопасности.',
            'part3': 'Средства анализа и настройки безопасности также предоставляют возможность устранения несоответствия, выявленного в ходе проверки. Кроме того, с помощью средств анализа и настройки безопасности можно прямо настраивать безопасность локальной системы. С помощью личных баз данных вы можете импортировать шаблоны безопасности, созданные с помощью оснасток безопасности, и применять эти шаблоны на локальном компьютере. Это немедленно настраивать безопасность системы на уровнях, заданных в шаблоне. Шаблоны безопасности — это оснастка консоли управления Microsoft, позволяющая изменять файлы шаблонов безопасности. С ее помощью вы можете создать политику безопасности для вашего устройства или для вашей сети. Это единая точка входа, с помощью которой можете просматривать весь диапазон безопасности системы. С помощью оснастки шаблона безопасности не появятся новые параметры безопасности, она просто организует все существующие атрибуты безопасности в одном месте, для того чтобы упростить администрирование. Импорт шаблона безопасности в объект групповой политики упрощает администрирование домена. Таким образом, можно настроить безопасность для домена или подразделение единовременно, чтобы применить шаблон безопасности к локальному устройству.',
            'part4': 'Вы можете использовать оснастку, анализ и настройка безопасности или средства командной строки SecEdit, о котором мы поговорим позже. Шаблоны безопасности можно использовать для определения следующих параметров. Политика учетных записей, политика паролей, политика блокировки учетных записей, политика керберас, локальные политики, политика аудита, назначение прав пользователя, параметры безопасности, а также журналы событий, группы с ограниченным доступом, членства в группах, учитывающих безопасность, системные службы, запуск и разрешение для системной службы. Реестер, разрешение для различных разделов реестра, а также файловая система, разрешение для каталогов и файлов. Каждый шаблон безопасности сохраняется в виде текстового файла с расширением инф. Это позволяет скопировать, вставить, импортировать, экспортировать некоторые или вообще все атрибуты шаблона. За исключением претика безопасности IP и политика открытого ключа, все атрибуты безопасности могут содержаться в шаблоне. Для того, чтобы работать со снастками анализ настройки безопасности и шаблона безопасности, нужно вызвать консоль управления Microsoft. Это можно сделать с помощью окна «Выполнить». Давайте посмотрим, как это сделать. Итак, запустим консоль управления Microsoft. Это можно сделать следующим образом. ввести команду и нажать OK. Появляется окошко контроля учетных записей. Соглашаемся с изменениями, так как это административное приложение.',
            'part5': 'Для того, чтобы добавить в консуль оснастку «Анализ настройка безопасности», мы выбираем файл «Добавить или удалить оснастку». Здесь в списке выбираем анализ настройки безопасности, а затем шаблон безопасности. Если вы будете часто работать с данными шаблонами, с данными оснастками, их можно сохранить в виде вашей собственной оснастки безопасности. Это можно сделать следующим образом. Файл, сохранить как. И в разделе средства администрирования Windows как раз вы можете сохранить, например, их под названием анализ. после чего они будут доступны в меню пуск. Итак, создадим новый шаблон безопасности. Как видите, уже есть каталог, за которым наблюдается система Windows. Тут есть созданный мне заранее тестовый шаблон. Мы создадим новый. Итак, у нас есть шаблон Test1. Открываем его и видим, что здесь повторяется часть параметров локальной политики безопасности. Давайте настроим несколько параметров в шаблоне. Например, в политике учетных записей, в политике паролей потребуем максимальный срок действия пароля. ',
            'part6': 'Установим его на 45 дней. предлагаемое значение нам предлагает 30, но мы соглашаемся все равно 45. И минимально 40 действий пароля мы поставим не 30, а мы поставим 15 дней. Итак, мы настроили несколько параметров. Для нашего примера этого достаточно. Можно также настроить доступ к локвальным политикам, аудит, параметры безопасности. Можно выбрать режим доступа к различным файлам. Файловые системы, добавить файл можно. Что делаем далее? Итак, мы должны сохранить этот шаблон. Мы внесли изменения, но их еще не сохранили. Выбираем «сохранить». Итак, мы сохранили параметры в шаблоне безопасности. Теперь мы проанализируем нашу систему на соответствие параметрам данного шаблона. Для этого мы переходим в раздел «Анализ настройки безопасности». Здесь немного нелогичный момент, но тем не менее у нас нет базы данных, поэтому мы должны её создать. Для того, чтобы её создать, мы выбираем вариант «Открыть». Мы создаём новую базу данных, назовём её «тест1» по названию нашего шаблона. И нам предлагают импортировать шаблон. Выбираем наш шаблон, тест 1. Итак, мы готовы проанализировать состояние нашей системы. Выбираем правой кнопкой «Анализ компьютера». ',
            'part7': 'Выбираем вариант, где будут сохраняться журналы. В принципе, можно здесь согласиться с параметрами по умолчанию. И проверяем политики учетных записей, политика паролей. Как видите, есть пункты, отмеченные красным. Эти параметры отличаются... параметра компьютера. Параметра базы данных 45, параметра компьютера 41, минимальное срок действия пароля 15, параметра компьютера 0. То есть не заданное. Давайте применим этот шаблон безопасности к нашему компьютеру. Опять же, правой кнопкой настроить компьютер. Она предлагает создать журнал. Соглашаемся. Мы провели изменения. Кстати, чтобы проверить, применились изменения или нет, или повторно проанализировать компьютер, что мы можем сделать сейчас. и посмотреть, что у нас параметры не отличаются. Вот, встают зеленые значки. Или второй вариант. Можно посмотреть прямо в локальной политике безопасности. политики учетных записей, политика паролей, и мы видим, что вот они параметры, те, которые мы задавали для нашего шаблона. Итак, мы увидели параметры безопасности, которые подходят для нашего шаблона. Поговорим про средство командной строки редактора безопасности. Оно настраивает и анализирует безопасность системы, сравнивает текущую конфигурацию с определенными шаблонами безопасности. Средство командной строки работает с шаблоном безопасности и имеет шесть основных функций. Фактически... Они дублируют функции оснасток, с которыми познакомились только что, и позволяют более эффективно настраивать сервера без использования графического интерфейса. Чтобы вызвать средства командной строки редактора безопасности, можно использовать несколько различных способов. ',
            'part8': 'Я продемонстрирую вам все, а вы выберите тот, который для вас подходит больше всего. Для работы со средством командной строки редактора безопасности потребуется командная строка с повышенными привилегиями. Поэтому сделаем следующее. Пуск, затем служебная. Итак, командная строка, нажимаем правой кнопкой, более, запуск от имени администратора. Соглашаемся с контролем учетных записей. Это первый способ. Второй способ. Можно вызвать тоже меню пуск. Точно также выбрать служебные. И не нажимая правой кнопкой, зажать CTRL и SHIFT и нажать на командную строку. Это равносильно запуску от имени администратора. Это второй способ. И пожалуй самый быстрый способ, два самых быстрых способа. Первый это через WinKR. Далее пишем CMD. Зажимаем CTRL SHIFT, нажимаем OK. И еще один способ – это нажать клавишу Win, далее X, выбрать Windows PowerShell администратор, согласиться, и, пожалуйста, вот у нас готовое окошко. ',
            'part9': 'Попробуем провести нашу работу с помощью PowerShell. Пишем команду. И нам сообщают, что в синтаксе с командой предполагают шесть различных вариантов. Продемонстрируем, как можно работать с шаблоном. Первое, что мы должны сделать, это провести валидацию шаблона. Убираемся к Edit, Validate, Test Inf. Появляется сообщение о том, что шаблон валидирован. Теперь мы должны проанализировать. нашу систему на соответствие. Выбираем Analyze, выбираем файл шаблона и выбираем файл базы данных, даже если не существует, он будет ссордан. Итак, задача выполнена успешно, был создан автоматический лог в системной директории, а мы видим, что у нас появился файл тест.sdb в каталоге с шаблонами. Теперь давайте применим эту конфигурацию с компьютером. Посмотрим, например. Итак, для того чтобы применить конфигурацию мы выбираем стек-эдит, конфигур. Выбираем базу данных. Набираем конфиг файл. Файл журнала и требование перезаписи можно в принципе не указывать. Давайте укажем сейчас файл журнала, чтобы нам было удобнее работать. Итак, сдача выполнена успешно. Если мы сейчас посмотрим на примененные нами параметры, мы это сможем сделать при помощи локальной политики безопасности. Итак, политики учетных записей, политика паролей. Итак, мы видим, что у нас применились параметры, которые были указаны в шаблоне. Давайте посмотрим еще раз сам шаблон. Итак, вот у нас шаблон тест, политика паролей. Итак, максимальная срок действия 41 дней, минимальная срок действия 0 дней. ',
            'part10': 'И можем провести еще раз анализ, чтобы наверняка убедиться, В базе данных. мы это сделаем в этой базе данных В предыдущем анализ. Итак, в базе данных у нас 45 дней, это предыдущий шаблон, который мы использовали. Сейчас на компьютере 41, и минимальный срок действия в базе данных, который мы предоставили, использовали 15, на компьютере сейчас 0. То есть мы конфигурацию поменяли, и конфигурация у нас применилась. Теперь кратко поговорим об основном элементе в администрировании Windows – групповой политики. Так как именно в объектах групповой политики GPO хранятся те изменения, которые мы вносим с помощью инструментов, о которых мы говорим. Однако возможности групповой политики на самом деле еще шире. Групповая политика – это мощный инструмент администрирования компьютеров, работающих под управлением операционной системы Windows. ',
            'pert11': 'С помощью этого инструмента, системные администраторы могут централизованно управлять параметрами клиентских машин в домене. Локальная групповая политика, которую мы рассмотрим сейчас, позволяет контролировать параметры устройств, не присоединенных к домену, определять поведение операционной системы для всех пользователей и вносить определенные настройки для каждой из учетных записей на компьютере. С помощью настроек локальной групповой политики можно контролировать возможности операционной системы Windows. Отличный инструмент отлично подходит для корпоративной среды. С его помощью можно ограничить функционал операционной системы до необходимого минимума. Таким образом, вы снижаете площадь возможной атаки на корпоративную инфраструктуру.',

        }
        return transcrib_body

    def gloss(self):
        #gloss_items
        return 'ok'

    def get(self, request, *args, **kwargs):
        test = 'Go Hack with back!'
        a = TranscriptionAudio()
        text_body = a.trascript()
        resp = {
            'id': 0,
            'body': text_body

        }
        return Response(json.dumps(resp))

class TestW(APIView):
    def test(self):
        #with open('textaudio2.txt.', 'r') as f:
        #    for i in f:
        #        print(i)
        text = 'Сейчас мы поговорим об инструментах локального администрирования. В рамках данного урока мы познакомимся с шаблонами безопасности и научимся работать с ними. Создадим свой шаблон безопасности, научимся его экспортировать, импортировать и анализировать. Также познакомимся со средством командной строки редактора безопасности и вкратце рассмотрим параметры локальной групповой политики. Анализ и настройка безопасности – это оснастка консоли управления Microsoft, позволяющая анализировать и настраивать параметры безопасности на компьютерах с операционной системой Windows с помощью файлов шаблонов безопасности. Состояние операционной системы и приложений на устройстве является динамическим. Например, может временно потребоваться изменить уровни безопасности, чтобы можно было немедленно устранить проблему, связанную с администрированием или сетью. Тем не менее, это изменение часто может отменять обратный переход. Это означает, что компьютер больше не будет отвечать требованиям для корпоративной безопасности. Регулярный анализ позволяет отслеживать и обеспечивать адекватный уровень безопасности на каждом компьютере по рамках программы управления рисками предприятия. Вы можете настроить уровни безопасности, и, что важнее, выявить изъяны системы безопасности, которые могут возникать в системе в течение определенных промежутков времени. С помощью средства анализа и настройки безопасности можете быстро просматривать результаты анализов. Они предоставляют рекомендации вместе с текущими системами параметрами и используют визуальные флаги или замечания для выбора тех областей, в которых текущие параметры не соответствуют предлагаемому уровню безопасности. Средства анализа и настройки безопасности также предоставляют возможность устранения несоответствия, выявленного в ходе проверки. Кроме того, с помощью средств анализа и настройки безопасности можно прямо настраивать безопасность локальной системы. С помощью личных баз данных вы можете импортировать шаблоны безопасности, созданные с помощью оснасток безопасности, и применять эти шаблоны на локальном компьютере. Это немедленно настраивать безопасность системы на уровнях, заданных в шаблоне. Шаблоны безопасности — это оснастка консоли управления Microsoft, позволяющая изменять файлы шаблонов безопасности. С ее помощью вы можете создать политику безопасности для вашего устройства или для вашей сети. Это единая точка входа, с помощью которой можете просматривать весь диапазон безопасности системы. С помощью оснастки шаблона безопасности не появятся новые параметры безопасности, она просто организует все существующие атрибуты безопасности в одном месте, для того чтобы упростить администрирование. Импорт шаблона безопасности в объект групповой политики упрощает администрирование домена. Таким образом, можно настроить безопасность для домена или подразделение единовременно, чтобы применить шаблон безопасности к локальному устройству. вы можете использовать оснастку, анализ и настройка безопасности или средства командной строки SecEdit, о котором мы поговорим позже. Шаблоны безопасности можно использовать для определения следующих параметров. Политика учетных записей, политика паролей, политика блокировки учетных записей, политика керберас, локальные политики, политика аудита, назначение прав пользователя, параметры безопасности, а также журналы событий, группы с ограниченным доступом, членства в группах, учитывающих безопасность, системные службы, запуск и разрешение для системной службы. Реестер, разрешение для различных разделов реестра, а также файловая система, разрешение для каталогов и файлов. Каждый шаблон безопасности сохраняется в виде текстового файла с расширением инф. Это позволяет скопировать, вставить, импортировать, экспортировать некоторые или вообще все атрибуты шаблона. За исключением претика безопасности IP и политика открытого ключа, все атрибуты безопасности могут содержаться в шаблоне. Для того, чтобы работать со снастками анализ настройки безопасности и шаблона безопасности, нужно вызвать консоль управления Microsoft. Это можно сделать с помощью окна «Выполнить». Давайте посмотрим, как это сделать. Итак, запустим консоль управления Microsoft. Это можно сделать следующим образом. ввести команду и нажать OK. Появляется окошко контроля учетных записей. Соглашаемся с изменениями, так как это административное приложение. Для того, чтобы добавить в консуль оснастку «Анализ настройка безопасности», мы выбираем файл «Добавить или удалить оснастку». Здесь в списке выбираем анализ настройки безопасности, а затем шаблон безопасности. Если вы будете часто работать с данными шаблонами, с данными оснастками, их можно сохранить в виде вашей собственной оснастки безопасности. Это можно сделать следующим образом. Файл, сохранить как. И в разделе средства администрирования Windows как раз вы можете сохранить, например, их под названием анализ. после чего они будут доступны в меню пуск. Итак, создадим новый шаблон безопасности. Как видите, уже есть каталог, за которым наблюдается система Windows. Тут есть созданный мне заранее тестовый шаблон. Мы создадим новый. Итак, у нас есть шаблон Test1. Открываем его и видим, что здесь повторяется часть параметров локальной политики безопасности. Давайте настроим несколько параметров в шаблоне. Например, в политике учетных записей, в политике паролей потребуем максимальный срок действия пароля. Установим его на 45 дней. предлагаемое значение нам предлагает 30, но мы соглашаемся все равно 45. И минимально 40 действий пароля мы поставим не 30, а мы поставим 15 дней. Итак, мы настроили несколько параметров. Для нашего примера этого достаточно. Можно также настроить доступ к локвальным политикам, аудит, параметры безопасности. Можно выбрать режим доступа к различным файлам. Файловые системы, добавить файл можно. Что делаем далее? Итак, мы должны сохранить этот шаблон. Мы внесли изменения, но их еще не сохранили. Выбираем «сохранить». Итак, мы сохранили параметры в шаблоне безопасности. Теперь мы проанализируем нашу систему на соответствие параметрам данного шаблона. Для этого мы переходим в раздел «Анализ настройки безопасности». Здесь немного нелогичный момент, но тем не менее у нас нет базы данных, поэтому мы должны её создать. Для того, чтобы её создать, мы выбираем вариант «Открыть». Мы создаём новую базу данных, назовём её «тест1» по названию нашего шаблона. И нам предлагают импортировать шаблон. Выбираем наш шаблон, тест 1. Итак, мы готовы проанализировать состояние нашей системы. Выбираем правой кнопкой «Анализ компьютера». Выбираем вариант, где будут сохраняться журналы. В принципе, можно здесь согласиться с параметрами по умолчанию. И проверяем политики учетных записей, политика паролей. Как видите, есть пункты, отмеченные красным. Эти параметры отличаются... параметра компьютера. Параметра базы данных 45, параметра компьютера 41, минимальное срок действия пароля 15, параметра компьютера 0. То есть не заданное. Давайте применим этот шаблон безопасности к нашему компьютеру. Опять же, правой кнопкой настроить компьютер. Она предлагает создать журнал. Соглашаемся. Мы провели изменения. Кстати, чтобы проверить, применились изменения или нет, или повторно проанализировать компьютер, что мы можем сделать сейчас. и посмотреть, что у нас параметры не отличаются. Вот, встают зеленые значки. Или второй вариант. Можно посмотреть прямо в локальной политике безопасности. политики учетных записей, политика паролей, и мы видим, что вот они параметры, те, которые мы задавали для нашего шаблона. Итак, мы увидели параметры безопасности, которые подходят для нашего шаблона. Поговорим про средство командной строки редактора безопасности. Оно настраивает и анализирует безопасность системы, сравнивает текущую конфигурацию с определенными шаблонами безопасности. Средство командной строки работает с шаблоном безопасности и имеет шесть основных функций. Фактически... Они дублируют функции оснасток, с которыми познакомились только что, и позволяют более эффективно настраивать сервера без использования графического интерфейса. Чтобы вызвать средства командной строки редактора безопасности, можно использовать несколько различных способов. Я продемонстрирую вам все, а вы выберите тот, который для вас подходит больше всего. Для работы со средством командной строки редактора безопасности потребуется командная строка с повышенными привилегиями. Поэтому сделаем следующее. Пуск, затем служебная. Итак, командная строка, нажимаем правой кнопкой, более, запуск от имени администратора. Соглашаемся с контролем учетных записей. Это первый способ. Второй способ. Можно вызвать тоже меню пуск. Точно также выбрать служебные. И не нажимая правой кнопкой, зажать CTRL и SHIFT и нажать на командную строку. Это равносильно запуску от имени администратора. Это второй способ. И пожалуй самый быстрый способ, два самых быстрых способа. Первый это через WinKR. Далее пишем CMD. Зажимаем CTRL SHIFT, нажимаем OK. И еще один способ – это нажать клавишу Win, далее X, выбрать Windows PowerShell администратор, согласиться, и, пожалуйста, вот у нас готовое окошко. Попробуем провести нашу работу с помощью PowerShell. Пишем команду. И нам сообщают, что в синтаксе с командой предполагают шесть различных вариантов. Продемонстрируем, как можно работать с шаблоном. Первое, что мы должны сделать, это провести валидацию шаблона. Убираемся к Edit, Validate, Test Inf. Появляется сообщение о том, что шаблон валидирован. Теперь мы должны проанализировать. нашу систему на соответствие. Выбираем Analyze, выбираем файл шаблона и выбираем файл базы данных, даже если не существует, он будет ссордан. Итак, задача выполнена успешно, был создан автоматический лог в системной директории, а мы видим, что у нас появился файл тест.sdb в каталоге с шаблонами. Теперь давайте применим эту конфигурацию с компьютером. Посмотрим, например. Итак, для того чтобы применить конфигурацию мы выбираем стек-эдит, конфигур. Выбираем базу данных. Набираем конфиг файл. Файл журнала и требование перезаписи можно в принципе не указывать. Давайте укажем сейчас файл журнала, чтобы нам было удобнее работать. Итак, сдача выполнена успешно. Если мы сейчас посмотрим на примененные нами параметры, мы это сможем сделать при помощи локальной политики безопасности. Итак, политики учетных записей, политика паролей. Итак, мы видим, что у нас применились параметры, которые были указаны в шаблоне. Давайте посмотрим еще раз сам шаблон. Итак, вот у нас шаблон тест, политика паролей. Итак, максимальная срок действия 41 дней, минимальная срок действия 0 дней. И можем провести еще раз анализ, чтобы наверняка убедиться, В базе данных. мы это сделаем в этой базе данных В предыдущем анализ. Итак, в базе данных у нас 45 дней, это предыдущий шаблон, который мы использовали. Сейчас на компьютере 41, и минимальный срок действия в базе данных, который мы предоставили, использовали 15, на компьютере сейчас 0. То есть мы конфигурацию поменяли, и конфигурация у нас применилась. Теперь кратко поговорим об основном элементе в администрировании Windows – групповой политики. Так как именно в объектах групповой политики GPO хранятся те изменения, которые мы вносим с помощью инструментов, о которых мы говорим. Однако возможности групповой политики на самом деле еще шире. Групповая политика – это мощный инструмент администрирования компьютеров, работающих под управлением операционной системы Windows. С помощью этого инструмента, системные администраторы могут централизованно управлять параметрами клиентских машин в домене. Локальная групповая политика, которую мы рассмотрим сейчас, позволяет контролировать параметры устройств, не присоединенных к домену, определять поведение операционной системы для всех пользователей и вносить определенные настройки для каждой из учетных записей на компьютере. С помощью настроек локальной групповой политики можно контролировать возможности операционной системы Windows. Отличный инструмент отлично подходит для корпоративной среды. С его помощью можно ограничить функционал операционной системы до необходимого минимума. Таким образом, вы снижаете площадь возможной атаки на корпоративную инфраструктуру.'
        transcrib_body = [
            'Сейчас мы поговорим об инструментах локального администрирования. В рамках данного урока мы познакомимся с шаблонами безопасности и научимся работать с ними. Создадим свой шаблон безопасности, научимся его экспортировать, импортировать и анализировать. Также познакомимся со средством командной строки редактора безопасности и вкратце рассмотрим параметры локальной групповой политики. Анализ и настройка безопасности – это оснастка консоли управления Microsoft, позволяющая анализировать и настраивать параметры безопасности на компьютерах с операционной системой Windows с помощью файлов шаблонов безопасности.',
            'Состояние операционной системы и приложений на устройстве является динамическим. Например, может временно потребоваться изменить уровни безопасности, чтобы можно было немедленно устранить проблему, связанную с администрированием или сетью. Тем не менее, это изменение часто может отменять обратный переход. Это означает, что компьютер больше не будет отвечать требованиям для корпоративной безопасности. Регулярный анализ позволяет отслеживать и обеспечивать адекватный уровень безопасности на каждом компьютере по рамках программы управления рисками предприятия. Вы можете настроить уровни безопасности, и, что важнее, выявить изъяны системы безопасности, которые могут возникать в системе в течение определенных промежутков времени. С помощью средства анализа и настройки безопасности можете быстро просматривать результаты анализов. Они предоставляют рекомендации вместе с текущими системами параметрами и используют визуальные флаги или замечания для выбора тех областей, в которых текущие параметры не соответствуют предлагаемому уровню безопасности.',
            'Средства анализа и настройки безопасности также предоставляют возможность устранения несоответствия, выявленного в ходе проверки. Кроме того, с помощью средств анализа и настройки безопасности можно прямо настраивать безопасность локальной системы. С помощью личных баз данных вы можете импортировать шаблоны безопасности, созданные с помощью оснасток безопасности, и применять эти шаблоны на локальном компьютере. Это немедленно настраивать безопасность системы на уровнях, заданных в шаблоне. Шаблоны безопасности — это оснастка консоли управления Microsoft, позволяющая изменять файлы шаблонов безопасности. С ее помощью вы можете создать политику безопасности для вашего устройства или для вашей сети. Это единая точка входа, с помощью которой можете просматривать весь диапазон безопасности системы. С помощью оснастки шаблона безопасности не появятся новые параметры безопасности, она просто организует все существующие атрибуты безопасности в одном месте, для того чтобы упростить администрирование. Импорт шаблона безопасности в объект групповой политики упрощает администрирование домена. Таким образом, можно настроить безопасность для домена или подразделение единовременно, чтобы применить шаблон безопасности к локальному устройству.',
            'Вы можете использовать оснастку, анализ и настройка безопасности или средства командной строки SecEdit, о котором мы поговорим позже. Шаблоны безопасности можно использовать для определения следующих параметров. Политика учетных записей, политика паролей, политика блокировки учетных записей, политика керберас, локальные политики, политика аудита, назначение прав пользователя, параметры безопасности, а также журналы событий, группы с ограниченным доступом, членства в группах, учитывающих безопасность, системные службы, запуск и разрешение для системной службы. Реестер, разрешение для различных разделов реестра, а также файловая система, разрешение для каталогов и файлов. Каждый шаблон безопасности сохраняется в виде текстового файла с расширением инф. Это позволяет скопировать, вставить, импортировать, экспортировать некоторые или вообще все атрибуты шаблона. За исключением претика безопасности IP и политика открытого ключа, все атрибуты безопасности могут содержаться в шаблоне. Для того, чтобы работать со снастками анализ настройки безопасности и шаблона безопасности, нужно вызвать консоль управления Microsoft. Это можно сделать с помощью окна «Выполнить». Давайте посмотрим, как это сделать. Итак, запустим консоль управления Microsoft. Это можно сделать следующим образом. ввести команду и нажать OK. Появляется окошко контроля учетных записей. Соглашаемся с изменениями, так как это административное приложение.',
            'Для того, чтобы добавить в консуль оснастку «Анализ настройка безопасности», мы выбираем файл «Добавить или удалить оснастку». Здесь в списке выбираем анализ настройки безопасности, а затем шаблон безопасности. Если вы будете часто работать с данными шаблонами, с данными оснастками, их можно сохранить в виде вашей собственной оснастки безопасности. Это можно сделать следующим образом. Файл, сохранить как. И в разделе средства администрирования Windows как раз вы можете сохранить, например, их под названием анализ. после чего они будут доступны в меню пуск. Итак, создадим новый шаблон безопасности. Как видите, уже есть каталог, за которым наблюдается система Windows. Тут есть созданный мне заранее тестовый шаблон. Мы создадим новый. Итак, у нас есть шаблон Test1. Открываем его и видим, что здесь повторяется часть параметров локальной политики безопасности. Давайте настроим несколько параметров в шаблоне. Например, в политике учетных записей, в политике паролей потребуем максимальный срок действия пароля. ',
            'Установим его на 45 дней. предлагаемое значение нам предлагает 30, но мы соглашаемся все равно 45. И минимально 40 действий пароля мы поставим не 30, а мы поставим 15 дней. Итак, мы настроили несколько параметров. Для нашего примера этого достаточно. Можно также настроить доступ к локвальным политикам, аудит, параметры безопасности. Можно выбрать режим доступа к различным файлам. Файловые системы, добавить файл можно. Что делаем далее? Итак, мы должны сохранить этот шаблон. Мы внесли изменения, но их еще не сохранили. Выбираем «сохранить». Итак, мы сохранили параметры в шаблоне безопасности. Теперь мы проанализируем нашу систему на соответствие параметрам данного шаблона. Для этого мы переходим в раздел «Анализ настройки безопасности». Здесь немного нелогичный момент, но тем не менее у нас нет базы данных, поэтому мы должны её создать. Для того, чтобы её создать, мы выбираем вариант «Открыть». Мы создаём новую базу данных, назовём её «тест1» по названию нашего шаблона. И нам предлагают импортировать шаблон. Выбираем наш шаблон, тест 1. Итак, мы готовы проанализировать состояние нашей системы. Выбираем правой кнопкой «Анализ компьютера». ',
            'Выбираем вариант, где будут сохраняться журналы. В принципе, можно здесь согласиться с параметрами по умолчанию. И проверяем политики учетных записей, политика паролей. Как видите, есть пункты, отмеченные красным. Эти параметры отличаются... параметра компьютера. Параметра базы данных 45, параметра компьютера 41, минимальное срок действия пароля 15, параметра компьютера 0. То есть не заданное. Давайте применим этот шаблон безопасности к нашему компьютеру. Опять же, правой кнопкой настроить компьютер. Она предлагает создать журнал. Соглашаемся. Мы провели изменения. Кстати, чтобы проверить, применились изменения или нет, или повторно проанализировать компьютер, что мы можем сделать сейчас. и посмотреть, что у нас параметры не отличаются. Вот, встают зеленые значки. Или второй вариант. Можно посмотреть прямо в локальной политике безопасности. политики учетных записей, политика паролей, и мы видим, что вот они параметры, те, которые мы задавали для нашего шаблона. Итак, мы увидели параметры безопасности, которые подходят для нашего шаблона. Поговорим про средство командной строки редактора безопасности. Оно настраивает и анализирует безопасность системы, сравнивает текущую конфигурацию с определенными шаблонами безопасности. Средство командной строки работает с шаблоном безопасности и имеет шесть основных функций. Фактически... Они дублируют функции оснасток, с которыми познакомились только что, и позволяют более эффективно настраивать сервера без использования графического интерфейса. Чтобы вызвать средства командной строки редактора безопасности, можно использовать несколько различных способов. ',
            'Я продемонстрирую вам все, а вы выберите тот, который для вас подходит больше всего. Для работы со средством командной строки редактора безопасности потребуется командная строка с повышенными привилегиями. Поэтому сделаем следующее. Пуск, затем служебная. Итак, командная строка, нажимаем правой кнопкой, более, запуск от имени администратора. Соглашаемся с контролем учетных записей. Это первый способ. Второй способ. Можно вызвать тоже меню пуск. Точно также выбрать служебные. И не нажимая правой кнопкой, зажать CTRL и SHIFT и нажать на командную строку. Это равносильно запуску от имени администратора. Это второй способ. И пожалуй самый быстрый способ, два самых быстрых способа. Первый это через WinKR. Далее пишем CMD. Зажимаем CTRL SHIFT, нажимаем OK. И еще один способ – это нажать клавишу Win, далее X, выбрать Windows PowerShell администратор, согласиться, и, пожалуйста, вот у нас готовое окошко. ',
            'Попробуем провести нашу работу с помощью PowerShell. Пишем команду. И нам сообщают, что в синтаксе с командой предполагают шесть различных вариантов. Продемонстрируем, как можно работать с шаблоном. Первое, что мы должны сделать, это провести валидацию шаблона. Убираемся к Edit, Validate, Test Inf. Появляется сообщение о том, что шаблон валидирован. Теперь мы должны проанализировать. нашу систему на соответствие. Выбираем Analyze, выбираем файл шаблона и выбираем файл базы данных, даже если не существует, он будет ссордан. Итак, задача выполнена успешно, был создан автоматический лог в системной директории, а мы видим, что у нас появился файл тест.sdb в каталоге с шаблонами. Теперь давайте применим эту конфигурацию с компьютером. Посмотрим, например. Итак, для того чтобы применить конфигурацию мы выбираем стек-эдит, конфигур. Выбираем базу данных. Набираем конфиг файл. Файл журнала и требование перезаписи можно в принципе не указывать. Давайте укажем сейчас файл журнала, чтобы нам было удобнее работать. Итак, сдача выполнена успешно. Если мы сейчас посмотрим на примененные нами параметры, мы это сможем сделать при помощи локальной политики безопасности. Итак, политики учетных записей, политика паролей. Итак, мы видим, что у нас применились параметры, которые были указаны в шаблоне. Давайте посмотрим еще раз сам шаблон. Итак, вот у нас шаблон тест, политика паролей. Итак, максимальная срок действия 41 дней, минимальная срок действия 0 дней. ',
            'И можем провести еще раз анализ, чтобы наверняка убедиться, В базе данных. мы это сделаем в этой базе данных В предыдущем анализ. Итак, в базе данных у нас 45 дней, это предыдущий шаблон, который мы использовали. Сейчас на компьютере 41, и минимальный срок действия в базе данных, который мы предоставили, использовали 15, на компьютере сейчас 0. То есть мы конфигурацию поменяли, и конфигурация у нас применилась. Теперь кратко поговорим об основном элементе в администрировании Windows – групповой политики. Так как именно в объектах групповой политики GPO хранятся те изменения, которые мы вносим с помощью инструментов, о которых мы говорим. Однако возможности групповой политики на самом деле еще шире. Групповая политика – это мощный инструмент администрирования компьютеров, работающих под управлением операционной системы Windows. ',
            'С помощью этого инструмента, системные администраторы могут централизованно управлять параметрами клиентских машин в домене. Локальная групповая политика, которую мы рассмотрим сейчас, позволяет контролировать параметры устройств, не присоединенных к домену, определять поведение операционной системы для всех пользователей и вносить определенные настройки для каждой из учетных записей на компьютере. С помощью настроек локальной групповой политики можно контролировать возможности операционной системы Windows. Отличный инструмент отлично подходит для корпоративной среды. С его помощью можно ограничить функционал операционной системы до необходимого минимума. Таким образом, вы снижаете площадь возможной атаки на корпоративную инфраструктуру.'
        ]
        print(text)