CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(1,2) NOT NULL,
    `price` INTEGER NOT NULL
);
CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` INTEGER NOT NULL
);
CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `timestamp` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);



INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES (null, "14K Gold", 736.60);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1258.90);
INSERT INTO `Metals` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metals` VALUES (null, "Palladium", 1241.00);


INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 782);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638);


INSERT INTO `Styles` VALUES (null, "Classic", 500);
INSERT INTO `Styles` VALUES (null, "Modern", 710);
INSERT INTO `Styles` VALUES (null, "Vintage", 965);


INSERT INTO `Orders` VALUES (null, 3, 2, 3, 1614659931693);
INSERT INTO `Orders` VALUES (null, 2, 3, 2, 1654656951656);
INSERT INTO `Orders` VALUES (null, 5, 4, 1, 4444656957656);



SELECT
    a.id,
    a.metal_id,
    a.style_id,
    a.size_id,
    a.timestamp
FROM orders a;