print("Hello world")
from flask import Flask
app = Flask(__name__)
#декоратор для вывода страницы по умолчанию
@app.route("/")
def hello():
  return " <html><head></head> <body> Hello World! </body></html>"
if __name__ == "__main__":
  app.run(host='127.0.0.1',port=5000)
from flask import render_template
#наша новая функция сайта
@app.route("/data_to")
def data_to():
  #создаем переменные с данными для передачи в шаблон
  some_pars = {'user':'Ivan','color':'red'}
  some_str = 'Hello my dear friends!'
some_value = 10
#передаем данные в шаблон и вызываем его
return render_template('simple.html',some_str = some_str,
some_value = some_value,some_pars=some_pars)
# модули работы с формами и полями в формах
from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
# модули валидации полей формы
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
# используем csrf токен, можете генерировать его сами
SECRET_KEY = 'secret'
app.config['SECRET_KEY'] = SECRET_KEY
# используем капчу и полученные секретные ключи с сайта Google
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = 'сюда поместить ключ из google'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'сюда поместить секретный ключ из google'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}
# обязательно добавить для работы со стандартными шаблонами
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
# создаем форму для загрузки файла
class NetForm(FlaskForm):
# поле для введения строки, валидируется наличием данных
# валидатор проверяет введение данных после нажатия кнопки submit
# и указывает пользователю ввести данные, если они не введены
# или неверны
openid = StringField('openid', validators = [DataRequired()])
# поле загрузки файла
# здесь валидатор укажет ввести правильные файлы
upload = FileField('Load image', validators=[
FileRequired(),
FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
# поле формы с capture
recaptcha = RecaptchaField()
#кнопка submit, для пользователя отображена как send
submit = SubmitField('send')
# функция обработки запросов на адрес 127.0.0.1:5000/net
# модуль проверки и преобразование имени файла
# для устранения в имени символов типа / и т.д.
from werkzeug.utils import secure_filename
import os
