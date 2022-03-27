Тестовое задание.  

git clone -b SberTech_Test1 <remote-repo-url> https://github.com/Bmax77/Test.git  

Для запуска сервера локально введите команду: python3 server/server_flask.py [-p PORT] в директории проекта, если не указан ключ -p и номер порта, то сервер запустится на порту 8080.

Приложение ожидает от пользователя ввода номера карты и производит проверку его корректности, допустимы цифры и пробел или тире в качестве разделителя.  
После чего передает запрос на сервер.


Для запуска тестов требуется установленный minikube.

Тест запускается командой python3 test_server.py

Произойдет сборка Docker образа и его деплой в minikube в default namespace.

После чего тест дождется запуска сервера.  
Протестирует корректность ответа readiness пробы.  
Протестирует загрузку главной страницы.  
Протестирует запрос существующего в базе номера карты.  
Протестирует запрос несуществующего в базе номера карты.  
Протестирует запрос не валидного номера карты.  
После проведения тестов удалит деплой сервиса из minikube.  

Если что то пошло не так:  
Выполнить команды:  

    $ kubectl apply -f bin_server_k8s.yml  
    $ kubektl get po -A  
    Вывод команды должен быть такм:  
        NAMESPACE     NAME                               READY   STATUS    RESTARTS       AGE  
        default       bin-server-6dc878d955-bw5kg        1/1     Running   0              24s  

    $ minikube service bin-server --url  
    http://192.168.49.2:30689 - IP и порт могут быть другими  
    Открыть полученную ссылку в браузере.  
    Если под в статусе Running но ссылка не открылась, то устранить причину сетевой недоступности  
    между локальным хостом и приложением в minikube.

