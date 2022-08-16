## Описание

#### В данном проекте реализован веб-сервис с помощью Django, который предоставляет RESTful API, позволяющий формировать ленту статей для пользователей. 
 - Авторизация/регистрация пользователей. В качестве логина используется email. Создана пользовательская модель User.
 - Добавлен валидатор пароля, проверяющий, что пароль состоит и букв и цифр.
 - Создание/редактировние/удаление статей для пользователей с ролью Author.
 - Private статьи, которые могут просматривать только пользователи с ролью Aythor и Subscriber.


#### В момент регистрации нового пользователя можно выбрать несколько ролей:

1. Subscraber - зарегестрированый пользователь с возможностью просмотра private статей.
2. Author - зарегестрированый пользователь с возможностью просмотра private статей, создания/редактирования/удаления статей, которые были написаны этим пользователем.

### [Ссылка на захосченный проект в интернете.](http://firslist.pythonanywhere.com/)
