CREATE DATABASE tracedb;
USE tracedb;
CREATE TABLE trace_data(
    id INT NOT NULL AUTO_INCREMENT,
    model VARCHAR(10) NOT NULL,
    country VARCHAR(40) NOT NULL,
    data_time DATETIME NOT NULL,
    lat FLOAT NOT NULL,
    lon FLOAT NOT NULL,
    speed FLOAT NOT NULL,
    altitude FLOAT NOT NULL,
    PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

GRANT ALL PRIVILEGES ON tracedb.* TO 'lilith'@'localhost';

