-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 01, 2020 at 04:55 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.1.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bugbox_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `agriculture_data`
--

CREATE TABLE `agriculture_data` (
  `id` int(11) NOT NULL,
  `time` varchar(30) NOT NULL,
  `greenhouse_id` int(11) NOT NULL,
  `humidity` float NOT NULL,
  `temperature` float NOT NULL,
  `moisture` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `agriculture_data`
--

INSERT INTO `agriculture_data` (`id`, `time`, `greenhouse_id`, `humidity`, `temperature`, `moisture`) VALUES
(1, 'asd', 12, 123, 123, 123);

-- --------------------------------------------------------

--
-- Table structure for table `air_quality_data`
--

CREATE TABLE `air_quality_data` (
  `id` int(11) NOT NULL,
  `time` text NOT NULL,
  `city` varchar(25) NOT NULL,
  `suburb` varchar(25) NOT NULL,
  `SO2` float NOT NULL,
  `NO2` float NOT NULL,
  `O3` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `password`) VALUES
('webmaster@python.org', 'very-secret'),
('webmaster@python.org', 'very-secret');

-- --------------------------------------------------------

--
-- Table structure for table `weather_data`
--

CREATE TABLE `weather_data` (
  `id` int(11) NOT NULL,
  `time` varchar(25) NOT NULL,
  `city` varchar(25) NOT NULL,
  `suburb` varchar(25) NOT NULL,
  `humidity` float NOT NULL,
  `temperature` float NOT NULL,
  `pressure` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agriculture_data`
--
ALTER TABLE `agriculture_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `air_quality_data`
--
ALTER TABLE `air_quality_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `weather_data`
--
ALTER TABLE `weather_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agriculture_data`
--
ALTER TABLE `agriculture_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `air_quality_data`
--
ALTER TABLE `air_quality_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `weather_data`
--
ALTER TABLE `weather_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
