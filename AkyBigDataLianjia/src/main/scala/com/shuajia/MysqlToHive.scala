package com.shuajia

import  com.shuajia.util.MysqlConnet
import org.apache.spark.SparkConf
import org.apache.spark.sql.{DataFrame, SparkSession}

object  MysqlToHive {
  def main(args: Array[String]): Unit = {
    val conf: SparkConf = new SparkConf().setMaster("local[*]")
    val spark: SparkSession = SparkSession.builder().config(conf).enableHiveSupport().getOrCreate()

    //调用Mysql的驱动器接口
    val housebasicdf: DataFrame = MysqlConnet.getDF("housebasic_table")
    val costdf: DataFrame = MysqlConnet.getDF("cost_table")
    val housedetaildf: DataFrame = MysqlConnet.getDF("housedetail_table")
    val intermediarydf: DataFrame = MysqlConnet.getDF("intermediary_table")

    housebasicdf.createOrReplaceTempView("t_housebasic")
    costdf.createOrReplaceTempView("t_cost")
    housedetaildf.createOrReplaceTempView("t_housedetail")
    intermediarydf.createOrReplaceTempView("t_intermediary")

    //支持Hive动态分区
    spark.sql("set hive.exec.dynamic.partition=true;")
    spark.sql("set hive.exec.dynamic.partition.mode=nonstrict;")
    spark.sql("set hive.exec.max.dynamic.partitions.pernode=1000;")

    //t_housebasic
    spark.sql(
      """
        |insert overwrite table ods.ods_housebasic
        |select verification_code,title,district,street,community_name,
        |lease_type,house_type,maintain_time from t_housebasic
        |""".stripMargin)

    //t_cost
    spark.sql(
      """
        |insert overwrite table ods.ods_cost
        |select verification_code,rent,payment_type,deposit,service_charge,agency_fee
        |from t_cost
        |""".stripMargin)

    //t_housedetail
    spark.sql(
      """
        |insert overwrite table ods.ods_housedetail
        |select verification_code,area,orientation,check_in,floor,
        |elevator,car_park,water,electric,gas,heating
        |from t_housedetail
        |""".stripMargin)

    //t_intermediary
    spark.sql(
      """
        |insert overwrite table ods.ods_intermediary
        |select verification_code,intermediary_name,intermediary_number,mechanism_number
        |from t_intermediary
        |""".stripMargin)

    spark.stop()
  }
}
