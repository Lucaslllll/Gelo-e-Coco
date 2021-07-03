from app import db


class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	email = db.Column(db.String, unique=True)
	password = db.Column(db.String)


	def __init__(self, username, first_name, last_name, email, password):

		self.username = username
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password

	def __repr__(self):
		return "<User : %r> " % self.username


class Endereco_User(db.Model):
	__tablename__ = "enderecos_user"

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	user = db.relationship('User', foreign_keys=user_id)

	def __init__(self, nome, user_id):

		self.nome = nome
		self.user_id = user_id


	def __repr__(self):
		return "<Endereco_User : %r> " % self.nome



class Informacao(db.Model):
	__tablename__ = "informacoes"

	id = db.Column(db.Integer, primary_key=True)
	telefone = db.Column(db.String)
	email = db.Column(db.String, null=True)
	endereco = db.Column(db.String, null=True)

	def __init__(self, telefone, email, endereco):
		self.telefone = telefone
		self.email = email
		self.endereco = endereco

	def __repr__(self):
		return "<Informacão : %r> " % self.endereco

class Oferecemos(db.Model):
	__tablename__ = 'oferecemos'

	id = db.Column(db.Integer, primary_key=True)
	produto = db.Column(db.String)
	detalhes = db.Column(db.Text)

	def __init__(self, produto, detalhes):

		self.produto = produto
		self.detalhes = detalhes

	def __repr__(self):
		return "<Oferecemos : %r> " % self.produto

