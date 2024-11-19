import os

class Config:
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://usuario:senha@ip:porta/nome_do_banco')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres.ybckbvogxccgupsxgbsr:Ev3nt0hub123v3nt0@aws-0-us-west-1.pooler.supabase.com:6543/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = True