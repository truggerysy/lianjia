package com.shuajia

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object OdsToDwd {
  def main(args: Array[String]): Unit = {
    val conf: SparkConf = new SparkConf().setMaster("local[*]")
    val spark: SparkSession = SparkSession.builder().config(conf).enableHiveSupport().getOrCreate()

    spark.sql("set hive.exec.dynamic.partition=true;")
    spark.sql("set hive.exec.dynamic.partition.mode=nonstrict;")
    spark.sql("set hive.exec.max.dynamic.partitions.pernode=1000;")
    //dwd_housebasic
    spark.sql(
      """
        |insert overwrite table dwd.dwd_housebasic
        |select ltrim(rtrim(verification_code)) verification_code,title,
        |case when district="政务" THEN "蜀山"
        |when district="高新" THEN "蜀山"
        |when district="经开" THEN "蜀山"
        |when district="新站" THEN "长丰"
        |when district="滨湖新区" THEN "包河" else district END as district,
        |street,community_name,lease_type,house_type
        |from ods.ods_housebasic where district not in ("空港经济示范区","庐江县")
        |""".stripMargin)

    //dwd_cost
    spark.sql(
      """
        |insert overwrite table dwd.dwd_cost
        |select ltrim(rtrim(verification_code)) verification_code,rent,
        |payment_type,deposit,service_charge,agency_fee
        |from ods.ods_cost
        |""".stripMargin)

    //dwd_housedetail
    spark.sql(
      """
        |insert overwrite table dwd.dwd_housedetail
        |select ltrim(rtrim(verification_code)) verification_code,area,
        |orientation,check_in,floor,elevator,car_park,water,electric,gas,heating
        |from ods.ods_housedetail
        |""".stripMargin)

    //dwd_intermediary
    spark.sql(
      """
        |insert overwrite table dwd.dwd_intermediary
        |select ltrim(rtrim(verification_code)) verification_code,intermediary_name,
        |intermediary_number,mechanism_number
        |from ods.ods_intermediary where intermediary_name is not NULL
        |or intermediary_number is not NULL or mechanism_number is not NULL
        |""".stripMargin)

    spark.stop()
  }
}
