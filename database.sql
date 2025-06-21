CREATE DATABASE IF NOT EXISTS avtosalon;
USE avtosalon;

CREATE TABLE IF NOT EXISTS mashinalar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model VARCHAR(100),
    narx DECIMAL(10,2),
    yil INT
);

CREATE TABLE IF NOT EXISTS mijozlar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ism VARCHAR(100),
    telefon VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS xodimlar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ism VARCHAR(100),
    lavozim VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS savdo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mashina_id INT,
    mijoz_id INT,
    sana DATE,
    FOREIGN KEY (mashina_id) REFERENCES mashinalar(id),
    FOREIGN KEY (mijoz_id) REFERENCES mijozlar(id)
);

CREATE TABLE IF NOT EXISTS tolovlar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    savdo_id INT,
    summa DECIMAL(10,2),
    sana DATE,
    FOREIGN KEY (savdo_id) REFERENCES savdo(id)
);

CREATE TABLE IF NOT EXISTS servislar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mashina_id INT,
    xizmat_turi VARCHAR(100),
    narx DECIMAL(10,2),
    FOREIGN KEY (mashina_id) REFERENCES mashinalar(id)
);

-- Test ma'lumotlari (ixtiyoriy)
INSERT INTO mashinalar (model, narx, yil) VALUES ('Toyota Camry', 25000.00, 2020);
INSERT INTO mijozlar (ism, telefon) VALUES ('Ali Valiyev', '+998901234567');
INSERT INTO xodimlar (ism, lavozim) VALUES ('Bobur Mirzayev', 'Sotuv menejeri');