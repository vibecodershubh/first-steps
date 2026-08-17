CREATE DATABASE IF NOT EXISTS HotelDB;
USE HOTELDB;
CREATE TABLE IF NOT EXISTS Rooms (
    room_number INT AUTO_INCREMENT PRIMARY KEY,
    room_type INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    available BOOLEAN DEFAULT 1, 
    FOREIGN KEY (room_type) REFERENCES RoomTypes(room_type)
);
CREATE TABLE IF NOT EXISTS RoomTypes (
    room_type INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);
CREATE TABLE IF NOT EXISTS Booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phno VARCHAR(15) NOT NULL,
    address TEXT NOT NULL,
    checkin DATE NOT NULL,
    checkout DATE NOT NULL,
    room_type INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    room_number INT NOT NULL,
    custid VARCHAR(50) NOT NULL,
    days INT NOT NULL,
    FOREIGN KEY (room_type) REFERENCES RoomTypes(room_type),
    FOREIGN KEY (room_number) REFERENCES Rooms(room_number)
);
CREATE TABLE IF NOT EXISTS Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES Booking(id)
);
INSERT INTO RoomTypes (type_name) VALUES ('Single');
INSERT INTO RoomTypes (type_name) VALUES ('Double');
INSERT INTO RoomTypes (type_name) VALUES ('Suite');
INSERT INTO Rooms (room_type, price, available) VALUES (1, 1000, 1); -- Single Room
INSERT INTO Rooms (room_type, price, available) VALUES (2, 1500, 1); -- Double Room
INSERT INTO Rooms (room_type, price, available) VALUES (3, 3000, 1); -- Suite
