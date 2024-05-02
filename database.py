from sqlalchemy import create_engine, text
import os



# PyMySQL
engine = create_engine("mysql+pymysql://root:12345678@mysql@localhost:3306/waterworks_db?charset=utf8mb4")



with engine.connect() as conn:
  result = conn.execute(text("select * from courses"))
  print(result.all())