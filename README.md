# Тестовое задание.

    git clone -b SberTech_Test1 https://github.com/Bmax77/Test.git

Для запуска сервера локально введите команду:

    python3 server/server_flask.py [-p PORT]

если не указан ключ -p и номер порта, то сервер запустится на порту 8080.

Приложение ожидает от пользователя ввода номера карты и производит проверку его корректности, допустимы цифры и пробел или тире в качестве разделителя.
После чего передает запрос на сервер.

### Для запуска тестов требуется запуск minikube c драйвером hyperkit. minikube start --driver=hyperkit
Тест запускается командой:

    python3 test_server.py

Произойдет сборка Docker образа и его деплой в minikube в default namespace.
После чего тест дождется запуска сервера.
- Протестирует корректность ответа readiness пробы.
- Протестирует загрузку главной страницы.
- Протестирует запрос существующего в базе номера карты.
- Протестирует запрос несуществующего в базе номера карты.
- Протестирует запрос не валидного номера карты.
- После проведения тестов удалит деплой сервиса из minikube.