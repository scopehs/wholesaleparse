CREATE TABLE `invoices` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `accountId` int NOT NULL,
  `accountName` varchar(200) NOT NULL,
  `invoiceNumber` varchar(200) NOT NULL,
  `invoiceDate` varchar(200) NOT NULL,
  `orderNumber` varchar(200) NOT NULL,
  `productNumber` varchar(200) NOT NULL,
  `description` text NOT NULL,
  `quantity` int NOT NULL,
  `netPrice` FLOAT NOT NULL,
  `per` int NOT NULL,
  `goods` FLOAT NOT NULL,
  `vat` FLOAT NOT NULL,
  `total` FLOAT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci