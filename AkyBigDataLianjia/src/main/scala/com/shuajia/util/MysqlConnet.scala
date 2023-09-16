package com.shuajia.util

import java.util.Properties

import org.apache.spark.SparkConf
import org.apache.spark.sql.{DataFrame, SparkSession}

object MysqlConnet {
  val conf: SparkConf = new SparkConf().setMaster("local[*]")
  val spark: SparkSession = SparkSession.builder().config(conf).enableHiveSupport().getOrCreate()
  final val JDBCURL = "jdbc:mysql://master:3306/zufang?useUnicode=true&characterEncoding=UTF-8"

  def getDF(tablename : String) ={
    val properties = new Properties()
    properties.put("user","root")
    properties.put("password","123456")
    properties.put("driver","com.mysql.jdbc.Driver")
    val df: DataFrame = spark.read.jdbc(JDBCURL, tablename, properties)
    df
  }
}
