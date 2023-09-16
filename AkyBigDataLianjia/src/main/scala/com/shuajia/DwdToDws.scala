package com.shuajia

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object DwdToDws {
  def main(args: Array[String]): Unit = {
    val conf: SparkConf = new SparkConf().setMaster("local[*]")
    val spark: SparkSession = SparkSession.builder().config(conf).enableHiveSupport().getOrCreate()

    spark.sql("set hive.exec.dynamic.partition=true;")
    spark.sql("set hive.exec.dynamic.partition.mode=nonstrict;")
    spark.sql("set hive.exec.max.dynamic.partitions.pernode=1000;")

    //dwd=>dws维度退化 join

    //dws.dws_houserent
    spark.sql(
      """
        |insert overwrite table dws.dws_houserent
        |select
        |A.verification_code,A.title,A.district,A.street,A.community_name,A.lease_type,A.house_type,
        |B.rent,B.payment_type,B.deposit,B.service_charge,B.agency_fee
        |from dwd.dwd_housebasic A
        |left join dwd.dwd_cost B
        |on A.verification_code = B.verification_code
        |""".stripMargin)

    //dws.dws_houseinfo
    spark.sql(
      """
        |insert overwrite table dws.dws_houseinfo
        |select
        |A.verification_code,A.title,A.district,A.street,A.community_name,A.lease_type,A.house_type,
        |B.area,B.orientation,B.check_in,B.floor,B.elevator,B.car_park,B.water,B.electric,B.gas,B.heating
        |from dwd.dwd_housebasic A
        |left join dwd.dwd_housedetail B
        |on A.verification_code = B.verification_code
        |""".stripMargin)

    //dws.dws_houseintermediary
    spark.sql(
      """
        |insert overwrite table dws.dws_houseintermediary
        |select
        |A.verification_code,A.title,A.district,A.street,A.community_name,A.lease_type,A.house_type,
        |B.intermediary_name,B.intermediary_number,B.mechanism_number
        |from dwd.dwd_housebasic A
        |left join dwd.dwd_intermediary B
        |on A.verification_code = B.verification_code
        |""".stripMargin)

    //dws.dws_house_rent_info
    spark.sql(
      """
        |insert overwrite table dws.dws_house_rent_info
        |select
        |A.verification_code,A.title,A.district,A.street,A.community_name,A.lease_type,A.house_type,
        |A.rent,A.payment_type,A.deposit,A.service_charge,A.agency_fee,
        |B.area,B.orientation,B.check_in,B.floor,B.elevator,B.car_park,B.water,B.electric,B.gas,B.heating
        |from dws.dws_houserent A
        |left join dws.dws_houseinfo B
        |on A.verification_code = B.verification_code
        |""".stripMargin)

    spark.stop()
  }
}
