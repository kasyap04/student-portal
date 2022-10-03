-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 05, 2022 at 04:59 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `students_portal`
--

-- --------------------------------------------------------

--
-- Table structure for table `academic_fee`
--

CREATE TABLE `academic_fee` (
  `fee_id` int(11) NOT NULL,
  `dep_id` int(11) NOT NULL,
  `sem` varchar(5) NOT NULL,
  `fee` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `attendence`
--

CREATE TABLE `attendence` (
  `attend_id` int(11) NOT NULL,
  `stu_id` int(11) NOT NULL,
  `dep_id` int(11) NOT NULL,
  `sem` varchar(5) NOT NULL,
  `date` date NOT NULL,
  `attend` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendence`
--

INSERT INTO `attendence` (`attend_id`, `stu_id`, `dep_id`, `sem`, `date`, `attend`) VALUES
(11, 1, 1, '1', '2022-02-11', 'h'),
(12, 2, 1, '1', '2022-02-11', 'a'),
(13, 3, 1, '1', '2022-02-11', 'h'),
(14, 4, 1, '1', '2022-02-11', 'p'),
(15, 4, 1, '1', '2022-02-13', 'a'),
(16, 2, 1, '1', '2022-02-13', 'a'),
(17, 3, 1, '1', '2022-02-13', 'a'),
(18, 1, 1, '1', '2022-02-13', 'a'),
(19, 1, 1, '1', '2022-03-05', 'p'),
(20, 2, 1, '1', '2022-03-05', 'a'),
(21, 3, 1, '1', '2022-03-05', 'p'),
(22, 4, 1, '1', '2022-03-05', 'p'),
(23, 1, 1, '1', '2022-04-04', 'p'),
(24, 2, 1, '1', '2022-04-04', 'p'),
(25, 3, 1, '1', '2022-04-04', 'p'),
(26, 4, 1, '1', '2022-04-04', 'p'),
(27, 12, 1, '1', '2022-04-04', 'p'),
(28, 13, 1, '1', '2022-04-04', 'p'),
(29, 14, 1, '1', '2022-04-04', 'p'),
(30, 15, 1, '1', '2022-04-04', 'p'),
(31, 16, 1, '1', '2022-04-04', 'p'),
(32, 1, 1, '1', '2022-04-05', 'p'),
(33, 2, 1, '1', '2022-04-05', 'p'),
(34, 3, 1, '1', '2022-04-05', 'a'),
(35, 4, 1, '1', '2022-04-05', 'a'),
(36, 12, 1, '1', '2022-04-05', 'p'),
(37, 13, 1, '1', '2022-04-05', 'p'),
(38, 14, 1, '1', '2022-04-05', 'p'),
(39, 15, 1, '1', '2022-04-05', 'p'),
(40, 16, 1, '1', '2022-04-05', 'a');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `classroom`
--

CREATE TABLE `classroom` (
  `classroom_id` int(11) NOT NULL,
  `sub_id` int(11) NOT NULL,
  `context` varchar(10) NOT NULL,
  `context_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `classroom`
--

INSERT INTO `classroom` (`classroom_id`, `sub_id`, `context`, `context_id`) VALUES
(1, 1, 'classwork', 3),
(6, 1, 'usershare', 9),
(7, 1, 'classwork', 4),
(8, 1, 'usershare', 10),
(11, 7, 'usershare', 12);

-- --------------------------------------------------------

--
-- Table structure for table `classwork`
--

CREATE TABLE `classwork` (
  `work_id` int(11) NOT NULL,
  `title` varchar(25) NOT NULL,
  `body` longtext NOT NULL,
  `date` date NOT NULL,
  `due_date` date DEFAULT NULL,
  `due_time` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `classwork`
--

INSERT INTO `classwork` (`work_id`, `title`, `body`, `date`, `due_date`, `due_time`) VALUES
(3, 'Seminar', 'Prepare a seminar about foundation of mathematics', '2022-02-24', '2022-02-18', '13:59'),
(4, 'Assignment', 'Submit an assigment about SQLite', '2022-03-01', '2022-03-01', '23:59');

-- --------------------------------------------------------

--
-- Table structure for table `class_media`
--

CREATE TABLE `class_media` (
  `media_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `context` varchar(10) NOT NULL,
  `context_id` int(11) NOT NULL,
  `shareby` varchar(10) NOT NULL,
  `shareby_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class_media`
--

INSERT INTO `class_media` (`media_id`, `name`, `context`, `context_id`, `shareby`, `shareby_id`) VALUES
(28, 'uploads/Screenshot(1)_67cn8gO.png', 'usershare', 7, 'student', 1),
(29, 'uploads/Screenshot(3)_XggbPPN.png', 'usershare', 7, 'student', 1),
(36, 'uploads/STUDYABOUTLED.docx', 'usershare', 10, 'teacher', 1),
(37, 'uploads/ASTUDYABOUTFLOWTRANSDUCERS.docx', 'classwork', 3, 'student', 1),
(38, 'uploads/ASTUDYABOUTDOUBLYLINKEDLIST.docx', 'classwork', 3, 'student', 1),
(39, 'uploads/Chapter3.pdf', 'classwork', 4, 'student', 4),
(40, 'uploads/HYPOTHESIS.pptx', 'classwork', 3, 'student', 4),
(41, 'uploads/projectfinal-1.docx', 'usershare', 13, 'principal', 2);

-- --------------------------------------------------------

--
-- Table structure for table `class_teacher`
--

CREATE TABLE `class_teacher` (
  `ct_id` int(11) NOT NULL,
  `dep_id` int(11) NOT NULL,
  `sem` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class_teacher`
--

INSERT INTO `class_teacher` (`ct_id`, `dep_id`, `sem`, `teacher_id`) VALUES
(1, 1, 1, 1),
(2, 1, 2, 8);

-- --------------------------------------------------------

--
-- Table structure for table `complaints`
--

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL,
  `stu_id` int(11) NOT NULL,
  `to` varchar(10) NOT NULL,
  `to_id` int(11) NOT NULL,
  `body` varchar(200) NOT NULL,
  `date` datetime NOT NULL,
  `respond_date` datetime DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `complaints`
--

INSERT INTO `complaints` (`complaint_id`, `stu_id`, `to`, `to_id`, `body`, `date`, `respond_date`, `reply`) VALUES
(8, 1, 't', 1, 'classroom getting more worse', '2022-02-15 15:05:34', '2022-04-04 23:36:05', 'We will do the necessary'),
(10, 1, 'hod', 6, 'This complaint is fied to HOD od BCA department', '2022-02-20 12:18:38', NULL, NULL),
(11, 1, 'p', 2, 'exam topic not covered', '2022-02-24 11:58:35', '2022-04-02 00:00:00', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `dep_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `short_name` varchar(6) NOT NULL,
  `duration` varchar(2) NOT NULL,
  `hod` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`dep_id`, `name`, `short_name`, `duration`, `hod`) VALUES
(1, 'Bachelor of computer application', 'BCA', '3', 6),
(2, 'Bachelor of bussiness administrator', 'BBA', '3', 0),
(3, 'Bachelor Of Commerce', 'B COM', '3', 4),
(4, 'Bachelor of art - english', 'BA ENG', '3', 4),
(5, 'Master of commerce', 'MCOM', '2', 0);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-02-19 07:07:47.420539'),
(2, 'auth', '0001_initial', '2022-02-19 07:08:04.155072'),
(3, 'admin', '0001_initial', '2022-02-19 07:08:09.591725'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-02-19 07:08:09.679983'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-02-19 07:08:09.803502'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-02-19 07:08:12.389268'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-02-19 07:08:13.385224'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-02-19 07:08:13.531154'),
(9, 'auth', '0004_alter_user_username_opts', '2022-02-19 07:08:13.594434'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-02-19 07:08:14.739550'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-02-19 07:08:14.780911'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-02-19 07:08:14.873152'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-02-19 07:08:15.037138'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-02-19 07:08:15.306645'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-02-19 07:08:15.807170'),
(16, 'auth', '0011_update_proxy_permissions', '2022-02-19 07:08:16.303601'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-02-19 07:08:16.471021'),
(18, 'sessions', '0001_initial', '2022-02-19 07:08:17.230364');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ap1o1dsaob3fxphll7gaptn5nwnk73rj', 'eyJ1aWQiOjEsImxvZ2luX3VzZXIiOiIifQ:1nbRdi:oLf9dTqrw0nMH0wg6R3Vr3-_K7LUCwsfnGBI4AdtK94', '2022-04-18 18:41:22.783935'),
('ca19x2np2vv1kkhphq9tbw1zdcjny4an', 'eyJsb2dpbl91c2VyIjp7InVzZXIiOiJwcmluY2lwYWwiLCJpZCI6Miwia2V5IjoiMnByMTM3MTYifX0:1nZEhZ:_J22MSVqyqY_3HD7jdYDUVKO3_F7j9feAoM3DxDSuOo', '2022-04-12 16:28:13.421490'),
('txhms6ri7i2aq65yfthk6y4ljim0c5zg', 'eyJsb2dpbl91c2VyIjp7InVzZXIiOiJzdHVkZW50IiwiaWQiOjF9fQ:1nTIrq:gHKdHWcddj872G7tbrbYsgXQMpffSRKjEacOEhVYX2M', '2022-03-27 07:42:18.715882');

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `event_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `body` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`event_id`, `date`, `body`) VALUES
(1, '2022-01-21', 'New yearr'),
(2, '2019-06-05', 'Ramdan / world enivonment '),
(3, '2019-07-19', 'Reading day'),
(4, '2019-07-03', 'St. thomas day'),
(5, '2022-07-11', 'World population day'),
(6, '2022-08-15', 'Independence day '),
(7, '2022-03-01', 'Mannam jayanthi'),
(8, '2020-01-10', 'Arts day'),
(9, '2022-03-12', 'Test event');

-- --------------------------------------------------------

--
-- Table structure for table `fees`
--

CREATE TABLE `fees` (
  `fee_id` int(11) NOT NULL,
  `dep_id` int(11) NOT NULL,
  `sem` int(11) NOT NULL,
  `fee_name` varchar(25) NOT NULL,
  `fee_amount` varchar(5) NOT NULL,
  `due_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fees`
--

INSERT INTO `fees` (`fee_id`, `dep_id`, `sem`, `fee_name`, `fee_amount`, `due_date`) VALUES
(7, 1, 2, 'sem', '15000', NULL),
(8, 5, 1, 'exam', '560', '2022-02-16'),
(10, 1, 1, 'sem', '15751', NULL),
(12, 1, 1, 'exam', '560', '2022-02-01');

-- --------------------------------------------------------

--
-- Table structure for table `fee_paid`
--

CREATE TABLE `fee_paid` (
  `paid_id` int(11) NOT NULL,
  `stu_id` int(11) NOT NULL,
  `fee_id` int(11) NOT NULL,
  `amount` varchar(10) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fee_paid`
--

INSERT INTO `fee_paid` (`paid_id`, `stu_id`, `fee_id`, `amount`, `date`) VALUES
(4, 1, 10, '10000', '2022-02-15'),
(5, 1, 12, '550.0', '2022-03-10'),
(6, 1, 7, '10', '2022-03-10'),
(7, 2, 10, '1000', '2022-03-12'),
(8, 4, 10, '1000', '2022-03-16'),
(9, 14, 10, '15751', '2022-04-05'),
(10, 14, 12, '560', '2022-04-05');

-- --------------------------------------------------------

--
-- Table structure for table `internals`
--

CREATE TABLE `internals` (
  `int_id` int(11) NOT NULL,
  `dep_id` int(1) NOT NULL,
  `sem` varchar(5) NOT NULL,
  `sub_id` int(11) NOT NULL,
  `stu_id` int(11) NOT NULL,
  `obtained_mark` varchar(3) NOT NULL,
  `total_mark` varchar(3) NOT NULL,
  `exam_name` varchar(75) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `internals`
--

INSERT INTO `internals` (`int_id`, `dep_id`, `sem`, `sub_id`, `stu_id`, `obtained_mark`, `total_mark`, `exam_name`, `date`) VALUES
(1, 1, '1', 1, 1, '30', '60', '1st internal examination', '2022-02-01'),
(2, 1, '1', 1, 2, '45', '60', '1st internal examination', '2022-02-01'),
(3, 1, '1', 1, 3, '50', '60', '1st internal examination', '2022-02-01'),
(4, 1, '1', 1, 4, '3', '60', '1st internal examination', '2022-02-01'),
(5, 1, '1', 2, 1, '50', '60', '1st internal examination', '2022-02-02'),
(6, 1, '1', 2, 2, '52', '60', '1st internal examination', '2022-02-02'),
(7, 1, '1', 2, 3, '57', '60', '1st internal examination', '2022-02-02'),
(8, 1, '1', 2, 4, '55', '60', '1st internal examination', '2022-02-02'),
(9, 1, '1', 1, 1, '10', '60', '2nd internal examination', '2022-03-15'),
(10, 1, '1', 1, 2, '47', '60', '2nd internal examination', '2022-03-15'),
(11, 1, '1', 1, 3, '32', '60', '2nd  internal examination', '2022-03-15'),
(12, 1, '1', 1, 4, '38', '60', '2nd  internal examination', '2022-03-15'),
(17, 1, '1', 7, 1, '20', '60', '1st internal examination', '2022-02-10'),
(18, 1, '1', 7, 2, '40', '60', '1st internal examination', '2022-02-10'),
(19, 1, '1', 7, 3, '30', '60', '1st internal examination', '2022-02-10'),
(20, 1, '1', 7, 4, '50', '60', '1st internal examination', '2022-02-10'),
(29, 1, '1', 1, 4, '25', '30', 'Class test', '2022-03-05'),
(30, 1, '1', 1, 2, '24', '30', 'Class test', '2022-03-05'),
(31, 1, '1', 1, 3, '21', '30', 'Class test', '2022-03-05'),
(32, 1, '1', 1, 1, '20', '30', 'Class test', '2022-03-05');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(50) NOT NULL,
  `login_key` varchar(10) DEFAULT NULL,
  `type` varchar(10) NOT NULL,
  `u_id` int(11) NOT NULL,
  `last_login` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`login_id`, `username`, `password`, `login_key`, `type`, `u_id`, `last_login`) VALUES
(1, 'BOATBCA024', '1234567', NULL, 'student', 1, '2022-04-04 15:07:46'),
(2, 'BOATBCA018', '1234567', NULL, 'student', 2, '2022-03-24 22:44:27'),
(3, 'BOATBCA020', 'boatbca020', NULL, 'student', 3, NULL),
(4, 'BOATBCA016', 'thomman', NULL, 'student', 4, '2022-03-16 12:44:13'),
(5, '1111111111', '1234567', '1te48154', 'teacher', 1, '2022-04-04 23:46:40'),
(6, '2222222222', 'anu@donbosco', '4te90989', 'teacher', 4, '2022-04-04 23:27:30'),
(7, '3333333333', 'geenavargeese@donbosco', NULL, 'teacher', 6, '2022-04-04 23:26:41'),
(9, '4444444444', 'ms.prejishachandran@donbosco', NULL, 'teacher', 7, NULL),
(10, '5555555555', 'ms.swathimohan@donbosco', NULL, 'teacher', 8, '2022-03-16 15:04:42'),
(11, '6666666666', 'ms.anumolritto@donbosco', NULL, 'teacher', 9, NULL),
(12, '7777777777', 'asd@donbosco', NULL, 'teacher', 10, NULL),
(13, '7777777777', 'asd@donbosco', NULL, 'teacher', 11, NULL),
(14, '1234567890', '0000000', '1ad40879', 'admin', 1, '2022-04-05 00:08:23'),
(15, '9876543210', '1234567', '2pr53164', 'principal', 2, '2022-04-05 00:09:21'),
(20, 'BOATBCA023', 'boatbca023', NULL, 'student', 12, NULL),
(21, 'BOATBCA022', 'boatbca022', NULL, 'student', 13, NULL),
(22, 'BOATBCA007', 'boatbca007', NULL, 'student', 14, NULL),
(23, 'BOATBCA013', 'boatbca013', NULL, 'student', 15, NULL),
(24, 'BOATBCA011', 'boatbca011', NULL, 'student', 16, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `master`
--

CREATE TABLE `master` (
  `master_id` int(11) NOT NULL,
  `name` varchar(35) NOT NULL,
  `number` int(10) NOT NULL,
  `post` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `master`
--

INSERT INTO `master` (`master_id`, `name`, `number`, `post`) VALUES
(1, 'Sandosh', 1234567890, 'admin'),
(2, 'Fr Name Name', 2147483647, 'principal');

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `notif_id` int(11) NOT NULL,
  `body` varchar(100) NOT NULL,
  `send_by` varchar(10) NOT NULL,
  `send_id` int(11) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`notif_id`, `body`, `send_by`, `send_id`, `date_time`) VALUES
(3, 'There will be class test in this week', 'teacher', 1, '2022-02-21 12:39:40'),
(6, 'You changed your password at Feb 28 2022, 10:23 PM', 'System', 1, '2022-02-28 22:23:35'),
(11, 'You changed your password at Mar 08 2022, 10:19 AM', 'System', 1, '2022-03-08 10:19:20'),
(12, 'Admin changed your password at Mar 12 2022, 09:31 AM', 'System', 1, '2022-03-12 09:31:25'),
(13, 'Please bring your passport size photo tommorrow', 'Admin', 1, '2022-03-12 18:39:49'),
(15, 'You changed your password at Mar 16 2022, 12:45 PM', 'System', 1, '2022-03-16 12:45:25'),
(19, 'Your admission number is changed to BOATBCA018 by Admin', 'System', 1, '2022-03-24 22:54:19');

-- --------------------------------------------------------

--
-- Table structure for table `notif_connect`
--

CREATE TABLE `notif_connect` (
  `connnect_id` int(11) NOT NULL,
  `notif_id` int(11) NOT NULL,
  `stu_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `notif_connect`
--

INSERT INTO `notif_connect` (`connnect_id`, `notif_id`, `stu_id`) VALUES
(3, 3, 1),
(4, 3, 2),
(5, 3, 3),
(6, 3, 4),
(9, 6, 1),
(26, 11, 2),
(27, 12, 1),
(28, 13, 1),
(29, 13, 2),
(30, 13, 3),
(31, 13, 4),
(32, 13, 10),
(33, 13, 11),
(38, 15, 4),
(45, 19, 2);

-- --------------------------------------------------------

--
-- Table structure for table `principal`
--

CREATE TABLE `principal` (
  `p_id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `report_files`
--

CREATE TABLE `report_files` (
  `rep_id` int(11) NOT NULL,
  `stu_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `body` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `semester`
--

CREATE TABLE `semester` (
  `sem_id` int(11) NOT NULL,
  `sem` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `stu_id` int(10) NOT NULL,
  `adm_no` varchar(12) NOT NULL,
  `name` varchar(25) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(6) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `join_year` date NOT NULL,
  `dep_id` int(11) NOT NULL,
  `current_sem` varchar(5) NOT NULL,
  `email` varchar(30) NOT NULL,
  `image` varchar(100) NOT NULL,
  `passout` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`stu_id`, `adm_no`, `name`, `dob`, `gender`, `phone`, `join_year`, `dep_id`, `current_sem`, `email`, `image`, `passout`) VALUES
(1, 'BOATBCA024', 'Vishnu P', '1999-05-10', 'male', '8089398832', '2019-02-13', 1, '1', 'vishnusree252@gmail.com', 'uploads/me_nFBeeaI.jpg', 0),
(2, 'BOATBCA018', 'Adarsh Pm', '2002-01-04', 'male', '2222222222', '2022-02-09', 1, '1', 'adarshpm@gmail.com', 'uploads/adarsh.jpeg', 0),
(3, 'BOATBCA020', 'Nikhil Pr', '2000-01-18', 'male', '3333333333', '2022-02-09', 1, '1', 'nikhilpr@gmail.com', 'uploads/nikil.jpeg', 0),
(4, 'BOATBCA016', 'Augustine Tom', '2001-10-08', 'male', '+919072918215', '2019-06-05', 1, '1', 'tom@gmail.com', 'uploads/tom.jpeg', 0),
(7, 'BOATBCA019', 'Asd', '2022-02-02', 'male', '2222222222', '2022-02-13', 3, '1', 'abcd@gmail.com', '', 0),
(12, 'BOATBCA023', 'Steve Augustine', '2001-04-24', 'male', '+919048176842', '2019-06-01', 1, '1', 'steve.augustine24@gmail.com', 'uploads/steve.jpeg', 0),
(13, 'BOATBCA022', 'Sharon Shaju', '2000-01-01', 'male', '+919562484274', '2019-01-06', 1, '1', 'sharon@gmail.com', 'uploads/SHARON-pp.jpg', 0),
(14, 'BOATBCA007', 'Bhakya K Ajayan', '2001-01-01', 'female', '+918281255654', '2019-01-06', 1, '1', 'bhagya@gmail.com', 'uploads/bhagya.jpeg', 0),
(15, 'BOATBCA013', 'Adarsh S Babu', '2000-01-01', 'male', '+919072409099', '2019-01-06', 1, '1', 'adarshsbabu@gmail.com', 'uploads/adarshs.jpeg', 0),
(16, 'BOATBCA011', 'Ridhu K Biju', '2000-01-01', 'female', '+918943923788', '2019-01-06', 1, '1', 'ridhu@gmail.com', 'uploads/ridhu.jpeg', 0);

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `sub_id` int(10) NOT NULL,
  `dep_id` int(11) NOT NULL,
  `sem` varchar(5) NOT NULL,
  `type` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `code` varchar(25) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `adm_year` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`sub_id`, `dep_id`, `sem`, `type`, `name`, `code`, `teacher_id`, `adm_year`) VALUES
(1, 1, '1', 'compli', 'Mathematical Foundation For Computer Application', 'BCA1C01', 1, '2019'),
(2, 1, '1', 'common', 'Transactional: Essential Language Skills', 'A01', 4, '2019'),
(4, 4, '1', 'common', 'Transactional: Essential Language Skills', 'ENG1A01', 4, '2019'),
(7, 1, '1', 'compliment', 'Operation Research', 'BCA2C03', 7, '2019'),
(8, 1, '2', 'common', 'Writing For Academic And Professional Success', 'A04', 9, '2019'),
(9, 1, '1', 'core', 'Computer Fundamentals And Html', 'BCA1V01', 6, '2019');

-- --------------------------------------------------------

--
-- Table structure for table `submited`
--

CREATE TABLE `submited` (
  `submit_id` int(11) NOT NULL,
  `work_id` int(11) NOT NULL,
  `stu_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `submited`
--

INSERT INTO `submited` (`submit_id`, `work_id`, `stu_id`, `date`, `time`) VALUES
(24, 3, 1, '2022-03-08', '10:07:05'),
(25, 4, 4, '2022-03-16', '12:33:33'),
(26, 3, 4, '2022-03-16', '12:34:19');

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE `teachers` (
  `teacher_id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(6) NOT NULL,
  `qualification` varchar(25) NOT NULL,
  `experiance` varchar(25) NOT NULL,
  `dep_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`teacher_id`, `name`, `mobile`, `email`, `dob`, `gender`, `qualification`, `experiance`, `dep_id`) VALUES
(1, 'Anuprabha V', '+9111111111112', 'anuprabha@gmail.com', '1991-01-01', 'female', 'MCA', '3', 1),
(4, 'Abhila', '2222222222', 'abhila@gmail.com', '1992-02-02', '', 'MA ENG', '1', 4),
(6, 'Geena Vargeese', '3333333333', 'geena', '1989-01-03', '', 'MCA', '6', 1),
(7, 'Ms. Prejisha Chandran', '1111111111', '123@gmail.com', '2022-02-01', '', 'B. Tech', '2', 1),
(8, 'Ms. Swathi Mohan', '1111111111', '123@gmail.com', '2022-02-01', '', 'M. Tech', '3', 1),
(9, 'Ms. Anumol Ritto', '1111111111', '123@gmail.com', '2022-02-16', '', 'MA', '0', 4);

-- --------------------------------------------------------

--
-- Table structure for table `user_share`
--

CREATE TABLE `user_share` (
  `share_id` int(11) NOT NULL,
  `body` longtext NOT NULL,
  `date` date NOT NULL,
  `send_user` varchar(10) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_share`
--

INSERT INTO `user_share` (`share_id`, `body`, `date`, `send_user`, `user_id`) VALUES
(9, 'Last year question papers', '2022-02-25', 'student', 1),
(10, 'Web programming classnotestali[\"https://try.com\"]endli', '2022-03-02', 'teacher', 1),
(12, 'HELLO', '2022-03-16', 'student', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `academic_fee`
--
ALTER TABLE `academic_fee`
  ADD PRIMARY KEY (`fee_id`);

--
-- Indexes for table `attendence`
--
ALTER TABLE `attendence`
  ADD PRIMARY KEY (`attend_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `classroom`
--
ALTER TABLE `classroom`
  ADD PRIMARY KEY (`classroom_id`);

--
-- Indexes for table `classwork`
--
ALTER TABLE `classwork`
  ADD PRIMARY KEY (`work_id`);

--
-- Indexes for table `class_media`
--
ALTER TABLE `class_media`
  ADD PRIMARY KEY (`media_id`);

--
-- Indexes for table `class_teacher`
--
ALTER TABLE `class_teacher`
  ADD PRIMARY KEY (`ct_id`);

--
-- Indexes for table `complaints`
--
ALTER TABLE `complaints`
  ADD PRIMARY KEY (`complaint_id`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`dep_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`event_id`);

--
-- Indexes for table `fees`
--
ALTER TABLE `fees`
  ADD PRIMARY KEY (`fee_id`);

--
-- Indexes for table `fee_paid`
--
ALTER TABLE `fee_paid`
  ADD PRIMARY KEY (`paid_id`);

--
-- Indexes for table `internals`
--
ALTER TABLE `internals`
  ADD PRIMARY KEY (`int_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `master`
--
ALTER TABLE `master`
  ADD PRIMARY KEY (`master_id`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`notif_id`);

--
-- Indexes for table `notif_connect`
--
ALTER TABLE `notif_connect`
  ADD PRIMARY KEY (`connnect_id`);

--
-- Indexes for table `principal`
--
ALTER TABLE `principal`
  ADD PRIMARY KEY (`p_id`);

--
-- Indexes for table `semester`
--
ALTER TABLE `semester`
  ADD PRIMARY KEY (`sem_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`stu_id`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`sub_id`);

--
-- Indexes for table `submited`
--
ALTER TABLE `submited`
  ADD PRIMARY KEY (`submit_id`);

--
-- Indexes for table `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`teacher_id`);

--
-- Indexes for table `user_share`
--
ALTER TABLE `user_share`
  ADD PRIMARY KEY (`share_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `academic_fee`
--
ALTER TABLE `academic_fee`
  MODIFY `fee_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `attendence`
--
ALTER TABLE `attendence`
  MODIFY `attend_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `classroom`
--
ALTER TABLE `classroom`
  MODIFY `classroom_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `classwork`
--
ALTER TABLE `classwork`
  MODIFY `work_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `class_media`
--
ALTER TABLE `class_media`
  MODIFY `media_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `class_teacher`
--
ALTER TABLE `class_teacher`
  MODIFY `ct_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `complaints`
--
ALTER TABLE `complaints`
  MODIFY `complaint_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `dep_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `event_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `fees`
--
ALTER TABLE `fees`
  MODIFY `fee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `fee_paid`
--
ALTER TABLE `fee_paid`
  MODIFY `paid_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `internals`
--
ALTER TABLE `internals`
  MODIFY `int_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `master`
--
ALTER TABLE `master`
  MODIFY `master_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `notif_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `notif_connect`
--
ALTER TABLE `notif_connect`
  MODIFY `connnect_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `principal`
--
ALTER TABLE `principal`
  MODIFY `p_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `semester`
--
ALTER TABLE `semester`
  MODIFY `sem_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `stu_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `sub_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `submited`
--
ALTER TABLE `submited`
  MODIFY `submit_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `teachers`
--
ALTER TABLE `teachers`
  MODIFY `teacher_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `user_share`
--
ALTER TABLE `user_share`
  MODIFY `share_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
