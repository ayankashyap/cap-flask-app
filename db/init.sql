CREATE DATABASE userdata;
use userdata

CREATE TABLE users (
    id int(11) NOT NULL AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    email varchar(100) NOT NULL,
    PRIMARY KEY(`id`)
)

INSERT INTO users
  (username, email)
VALUES
  ('ayank', 'ayankashyap8@gmail.com'),
  ('akshits', 'akshit.sarin@st.niituniversity.in');