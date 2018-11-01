CREATE DATABASE tracedb;
USE tracedb;
CREATE TABLE trace_data(
    id INT NOT NULL AUTO_INCREMENT,
    model VARCHAR(10) NOT NULL,
    country VARCHAR(40) NOT NULL,
    data_time DATETIME NOT NULL,
    lat DOUBLE NOT NULL,
    lon DOUBLE NOT NULL,
    speed DOUBLE NOT NULL,
    altitude DOUBLE NOT NULL,
    PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

GRANT ALL PRIVILEGES ON tracedb.* TO 'lilith'@'localhost';
