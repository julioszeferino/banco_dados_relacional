from email.policy import default
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


import sqlalchemy as sa
from datetime import datetime, time


# Tabela tipos_ocorrencias
class TipoOcorrencia(Base):

    __tablename__: str = 'tipos_ocorrencias'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    tipo_ocorrencia: str = sa.Column(sa.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Tipo Ocorrencia: {self.tipo_ocorrencia}>'


# Tabela carros
class Carro(Base):

    __tablename__: str = 'carros'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    placa: str = sa.Column(sa.String(7), unique=True, nullable=False)
    modelo: str = sa.Column(sa.String(50), nullable=False)
    ano: int = sa.Column(sa.Integer, nullable=False)
    chassi: str = sa.Column(sa.String(50), nullable=False)
    cor: str = sa.Column(sa.String(50), nullable=False)

    def __repr__(self):
        return f'<Carro: {self.placa}>'


# Tabela condutores
class Condutor(Base):

    __tablename__: str = 'condutores'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    nome: str = sa.Column(sa.String(50), nullable=False)
    cpf: str = sa.Column(sa.String(11), unique=True, nullable=False)

    def __repr__(self):
        return f'<Condutor: {self.nome}>'


# Tabela telefones
class Telefone(Base):

    __tablename__: str = 'telefones'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    numero: str = sa.Column(sa.String(11), unique=True, nullable=False)
    tipo: str = sa.Column(sa.String(50), nullable=False)

    def __repr__(self):
        return f'<Telefone: {self.numero}>'


# Tabela clientes
class Cliente(Base):

    __tablename__: str = 'clientes'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    cpf: str = sa.Column(sa.String(14), unique=True, nullable=False)
    nome: str = sa.Column(sa.String(50), nullable=False)
    sexo: str = sa.Column(sa.String(1), nullable=False)
    uf: str = sa.Column(sa.String(2), nullable=False)
    cidade: str = sa.Column(sa.String(50), nullable=False)
    bairro: str = sa.Column(sa.String(50), nullable=False)
    logradouro: str = sa.Column(sa.String(50), nullable=False)

    telefones_id: int = sa.Column(sa.BigInteger, sa.ForeignKey('telefones.id'), nullable=False)
    telefones: Telefone = sa.orm.relationship('Telefone', lazy='joined')
   
    def __repr__(self):
        return f'<Cliente: {self.nome}>'


# Tabela apolices
class Apolice(Base):

    __tablename__: str = 'apolices'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_inicio: datetime = sa.Column(sa.DateTime, nullable=False)
    data_fim: datetime = sa.Column(sa.DateTime, nullable=False)
    valor_total: float = sa.Column(sa.DECIMAL(15, 2), nullable=False, default=0.00)
    valor_franquia: float = sa.Column(sa.DECIMAL(15, 2), nullable=False, default=0.00)

    clientes_id: int = sa.Column(sa.BigInteger, sa.ForeignKey('clientes.id'), nullable=False)   
    clientes: Cliente = sa.orm.relationship('Cliente', lazy='joined')

    carros_id: int = sa.Column(sa.BigInteger, sa.ForeignKey('carros.id'), nullable=False)
    carros: Carro = sa.orm.relationship('Carro', lazy='joined')

    def __repr__(self):
        return f'<Apolice: {self.id}>'


# Tabela sinistros
class Sinistro(Base):

    __tablename__: str = 'sinistros'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_ocorrencia: datetime = sa.Column(sa.DateTime, nullable=False)
    hora_ocorrencia: time = sa.Column(sa.Time, nullable=False)
    uf: str = sa.Column(sa.String(2), nullable=False)
    cidade: str = sa.Column(sa.String(50), nullable=False)
    bairro: str = sa.Column(sa.String(50), nullable=False)
    logradouro: str = sa.Column(sa.String(50), nullable=False)

    carros_id: int = sa.Column(sa.BigInteger, sa.ForeignKey('carros.id'), nullable=False)
    carros: Carro = sa.orm.relationship('Carro', lazy='joined')

    condutores_id: int = sa.Column(sa.BigInteger, sa.ForeignKey('condutores.id'), nullable=False)
    condutores: Condutor = sa.orm.relationship('Condutor', lazy='joined')

    tipos_ocorrencias_id: int = sa.Column(sa.BigInteger, sa.ForeignKey('tipos_ocorrencias.id'), nullable=False)
    tipos_ocorrencias: TipoOcorrencia = sa.orm.relationship('TipoOcorrencia', lazy='joined')

    apolices_id: int = sa.Column(sa.BigInteger, sa.ForeignKey('apolices.id'), nullable=False)
    apolices: Apolice = sa.orm.relationship('Apolice', lazy='joined')

    def __repr__(self):
        return f'<Sinistro: {self.id}>'


# Tabela apolices_condutores
class ApoliceCondutor(Base):

    __tablename__: str = 'apolices_condutores'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    
    apolices_id: int = sa.Column(sa.BigInteger, sa.ForeignKey('apolices.id'), nullable=False)
    apolices: Apolice = sa.orm.relationship('Apolice', lazy='joined')

    condutores_id: int = sa.Column(sa.BigInteger, sa.ForeignKey('condutores.id'), nullable=False)
    condutores: Condutor = sa.orm.relationship('Condutor', lazy='joined')

    def __repr__(self):
        return f'<Apolice: {self.apolices_id}, Condutor: {self.condutores_id}>'

