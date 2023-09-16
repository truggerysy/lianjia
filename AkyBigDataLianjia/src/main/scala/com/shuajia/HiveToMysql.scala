package com.shuajia

import java.util.Properties

import org.apache.spark.SparkConf
import org.apache.spark.sql.{DataFrame, SparkSession}

object HiveToMysql {
  def main(args: Array[String]): Unit = {
    val conf: SparkConf = new SparkConf().setMaster("local[*]")
    val spark: SparkSession = SparkSession.builder().config(conf).enableHiveSupport().getOrCreate()

    val JDBCURL = "jdbc:mysql://master:3306/houserent?useUnicode=true&characterEncoding=UTF-8"
    val properties = new Properties()
    properties.put("user","root")
    properties.put("password","123456")
    properties.put("driver","com.mysql.jdbc.Driver")

    val df1: DataFrame = spark.sql(
      """
        |select * from ads.housenum_and_avgrent_of_community order by avgrent desc limit 10
        |""".stripMargin)

    val df2: DataFrame = spark.sql(
      """
        |select * from ads.housenum_and_avgrent_of_community order by avgrent limit 10
        |""".stripMargin)

    val df3: DataFrame = spark.sql(
      """
        |select * from ads.housenum_and_avgrent_of_district
        |""".stripMargin)

    val df4: DataFrame = spark.sql(
      """
        |select * from ads.housenum_and_avgrent_of_district_and_lease
        |""".stripMargin)

    val df5: DataFrame = spark.sql(
      """
        |select * from ads.housenum_and_avgrent_of_housetype
        |""".stripMargin)

    val df6: DataFrame = spark.sql(
      """
        |select * from ads.housenumber_of_intermediary order by housenumber desc limit 10
        |""".stripMargin)

    df1.write.mode("overwrite").jdbc(JDBCURL,"housenum_and_avgrent_of_community_desctop10",properties)

    df2.write.mode("overwrite").jdbc(JDBCURL,"housenum_and_avgrent_of_community_top10",properties)

    df3.write.mode("overwrite").jdbc(JDBCURL,"housenum_and_avgrent_of_district",properties)

    df4.write.mode("overwrite").jdbc(JDBCURL,"housenum_and_avgrent_of_district_and_lease",properties)

    df5.write.mode("overwrite").jdbc(JDBCURL,"housenum_and_avgrent_of_housetype",properties)

    df6.write.mode("overwrite").jdbc(JDBCURL,"housenumber_of_intermediary_top10",properties)

  }
}
