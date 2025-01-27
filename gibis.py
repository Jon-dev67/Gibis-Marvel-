from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField
from wtforms.validators import Length, Email, DataRequired,EqualTo,ValidationError
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required, current_user


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///instance/app_marvel.db"
app.config["SECRET_KEY"]="41b56541272c31e0dbd695def78428b2"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view="page_login"
login_manager.login_message="por favor faça o login"
login_manager.login_message_category="warning"


#rota que gerencia o login e verifica se o usuario esta logado 
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


# Model
class Usuario(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  usuario = db.Column(db.String(length=60),nullable=False, unique=True)
  email = db.Column(db.String(length=60), nullable=False, unique=True)
  senha = db.Column(db.String(),nullable=False, unique=True)
  
  #criptografando senha com flask_bcrypt  
  @property
  def senhacrip(self):
      return self.senhacrip

  @senhacrip.setter
  def senhacrip(self, password_text):
      self.senha = bcrypt.generate_password_hash(password_text).decode('utf-8')
#convertendo senha para "texto claro" para checar senha para ver se ja esta no banco de dados        
  def converte_senha(self,senha_texto_claro):
      return bcrypt.check_password_hash(self.senha,senha_texto_claro)
  
# formularios
class Usuario_Form(FlaskForm):
  
  def validate_usu(self, check_usu):
        usu = Usuario.query.filter_by(usuario=check_usu.data).first()
        if usu:
          raise ValidationError("nome de usuário já existe, tente outro nome de usuário")
            
  def validate_email(self, check_email):
      email = Usuario.query.filter_by(email=check_email.data).first()
      if email:
        raise ValidationError("Email já existe, tente outro email por favor.")
  def validate_senha(self, check_senha):
      Senha = Usuario.query.filter_by(senha=check_senha.data).first()
      if Senha:
        raise ValidationError("Senha já existe, tente outra senha por favor.")
  usuarios = StringField(label="user-name", validators=[DataRequired()])
  email = StringField(label="E-mail:",validators=[DataRequired(), Email()])
  senha1 = PasswordField(label="password:", validators=[DataRequired()])
  senha2 = PasswordField(label="repeat password", validators=[DataRequired(), EqualTo('senha1', message='as senhas devem ser iguais.')])
  submit = SubmitField(label="cadastrar")
  
  
class Login_Form(FlaskForm):
  usuario_login = StringField(label="user-name", validators=[DataRequired(), Length(min=2)])
  senha_login = StringField(label="password:",validators=[DataRequired()])
  submit_login = SubmitField(label="Entrar")
  


@app.route("/", methods=["POST","GET"])
def home_page():
  return render_template("index.html")
  
@app.route("/gibi")
@login_required
def Gibi():
  return render_template("ler_gibis.html")
  
@app.route("/videos")
@login_required
def Video():
  return render_template("Ver_videos_herois.html")
  
@app.route("/hulk")
def hulk_page():
  return render_template("Hulk.html")
  
@app.route("/luke_cage")
def Luke_Cage():
  return render_template("Luke_cage.html")
  
@app.route("/superman")
def Superman():
  return render_template("Superman.html")
  
@app.route("/cad_usuarios", methods=["POST","GET"])
def Cad_usu():
  form = Usuario_Form()
  if form.validate_on_submit():
    usuar = Usuario(
           usuario = form.usuarios.data,
           email = form.email.data,
           senhacrip = form.senha1.data
      )
    db.session.add(usuar)
    db.session.commit()
    flash(f"parabéns {usuar.usuario} cadastro realizado com sucesso!!!", category="success")
    return redirect(url_for('home_page'))
  
  elif form.errors != {}:
    for err in form.errors.values():
      flash(f"oops {err}", category="warning")
      return redirect(url_for('Cad_usu',form=form))
  return render_template("cadastro.html",form=form)
  
@app.route("/login", methods=["GET","POST"])
def page_login():
    form = Login_Form()
    if form.validate_on_submit():
        usuario_logado = Usuario.query.filter_by(usuario=form.usuario_login.data).first()
        if usuario_logado and usuario_logado.converte_senha(senha_texto_claro=form.senha_login.data):
            login_user(usuario_logado)
            flash(f"login realizado com sucesso! Olá  {usuario_logado.usuario}",category="success")
            return redirect(url_for("home_page"))      
        else:
            flash(f"senha ou email inválido", category="danger")
    return render_template("login_page.html",form=form)
  
@app.route("/logout", methods=["GET"])
def page_logout():
    if current_user.is_authenticated:  # Verifica se o usuário está logado
        nome_usuario = current_user.usuario  # Acessa o nome do usuário logado
        logout_user()
        flash(f"Até logo, {nome_usuario}!", category="info")
    else:
        flash("Nenhum usuário está logado no momento.", category="warning")

    return redirect(url_for("home_page"))
  
if __name__=="__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)
  
  