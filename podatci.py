from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

# spajanje na bazu
konekcija = create_engine("sqlite:///baza.db", echo=True)
Model = declarative_base()

#dodavanje u bazu
Session = db.orm.sessionmaker()
Session.configure(bind=konekcija)

session = Session()

class Korisnik(Model):
    __tablename__="korisnik"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ime = db.Column(db.String(50))
    prezime = db.Column(db.String(50))
    email = db.Column(db.String(50))
    JMBG = db.Column(db.String(50))
    adresa_id = db.Column(db.Integer, db.ForeignKey('adresa.id'))
    adresa = db.orm.relationship("Adresa", back_populates="korisnici")

class Adresa(Model):
    __tablename__="adresa"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    naziv = db.Column(db.String(50))
    mjesto = db.Column(db.String(50))

    korisnici = db.orm.relationship('Korisnik')

#izgradnja svih tablica
Model.metadata.create_all(konekcija)

#adresa = Adresa()
#adresa.mjesto = "Mostar"
#adresa.naziv = "Kralja Tomislava"

#session.add(adresa)
#session.commit()

korisnik = Korisnik()
korisnik.adresa_id = 1
korisnik.ime= "Pero"
korisnik.prezime = "Peric"
korisnik.email = "pero.peric@fpmoz.sum.ba"
korisnik.JMBG = "11222121324113"

session.add(korisnik)
session.commit()

korisnici = session.query(Korisnik).filter_by(prezime="Daniel").all()
for korisnik in korisnici:
    print(korisnik.ime, korisnik.prezime, korisnik.adresa.naziv, korisnik.adresa.mjesto)