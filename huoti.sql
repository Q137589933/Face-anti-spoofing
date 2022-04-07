/*
 Navicat Premium Data Transfer

 Source Server         : me
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : huoti

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 15/08/2021 01:20:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

drop database if exists huoti;
create database huoti;
use huoti;

-- ----------------------------
-- Table structure for viewer
-- ----------------------------
DROP TABLE IF EXISTS `viewer`;
CREATE TABLE `viewer`  (
  `UId` int(0) NOT NULL AUTO_INCREMENT,
  `Uname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` char(11) CHAR SET utf8,
  `email` varchar(255) CHAR SET utf8,
  PRIMARY KEY (`UId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for editor
-- ----------------------------
DROP TABLE IF EXISTS `editor`;
CREATE TABLE `editor`  (
  `EId` int(0) NOT NULL AUTO_INCREMENT,
  `Ename` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` char(11) CHAR SET utf8,
  `email` varchar(255) CHAR SET utf8,
  PRIMARY KEY (`EId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for photo
-- ----------------------------
DROP TABLE IF EXISTS `photo`;
CREATE TABLE `photo`  (
  `PId` int(0) NOT NULL AUTO_INCREMENT,
  `path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `upTime` datetime NOT NULL,
  `label` int(0) NOT NULL,
  `user` int(0) NOT NULL,
  PRIMARY KEY (`PId`) USING BTREE,
  Foreign Key(`user`) References viewer(`UId`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for video
-- ----------------------------
CREATE TABLE `video`  (
  `VId` int(0) NOT NULL AUTO_INCREMENT,
  `path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `upTime` datetime NOT NULL,
  `label` int(0) NOT NULL,
  `user` int(0) NOT NULL,
  PRIMARY KEY (`VId`) USING BTREE,
  Foreign Key(`user`) References viewer(`UId`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
