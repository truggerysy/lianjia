package com.shuajia

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object DwsToAds {
  def main(args: Array[String]): Unit = {
    val conf: SparkConf = new SparkConf().setMaster("local[*]")
    val spark: SparkSession = SparkSession.builder().config(conf).enableHiveSupport().getOrCreate()

    spark.sql("set hive.exec.dynamic.partition=true;")
    spark.sql("set hive.exec.dynamic.partition.mode=nonstrict;")
    spark.sql("set hive.exec.max.dynamic.partitions.pernode=1000;")

    //dws维度=>ads应用层
    //指标1：各个区域的平均房屋和房屋个数 ads.housenum_and_avgrent_of_district
    spark.sql(
      """
        |insert overwrite table ads.housenum_and_avgrent_of_district
        |select
        |district,count(verification_code) housenumofdistrict,round(avg(rent)) avgrent
        |from dws.dws_houserent where lease_type !="未知" group by district
        |""".stripMargin)

    //指标2：各个区域的不同出租类型的平均房租和平均个数
    spark.sql(
      """
        |insert overwrite table ads.housenum_and_avgrent_of_district_and_lease
        |select
        |district,lease_type,count(verification_code) housenumofdistrict,round(avg(rent)) avgrent
        |from dws.dws_houserent where lease_type !="未知" group by district,lease_type
        |""".stripMargin)

    //指标3：各个小区的平均房屋和房屋个数
    spark.sql(
      """
        |insert overwrite table ads.housenum_and_avgrent_of_community
        |select
        |community_name,count(verification_code) housenumofdistrict,round(avg(rent)) avgrent
        |from dws.dws_houserent group by community_name
        |""".stripMargin)

    spark.sql(
      """
        |select district,rent,
        |CASE WHEN area>0 AND area <=20 THEN "0-20㎡"
        |WHEN area>20 AND area <=40 THEN "20-40㎡"
        |WHEN area>20 AND area <=60 THEN "40-60㎡"
        |WHEN area>20 AND area <=80 THEN "60-80㎡"
        |WHEN area>20 AND area <=100 THEN "80-100㎡"
        |WHEN area>20 AND area <=120 THEN "100-120㎡"
        |WHEN area>20 AND area <=140 THEN "120-140㎡"
        |WHEN area>20 AND area <=160 THEN "140-160㎡"
        |WHEN area>20 AND area <=180 THEN "160-180㎡"
        |WHEN area>20 AND area <=200 THEN "180-200㎡"
        |ELSE "200-~㎡" END as type
        |from dws.dws_house_rent_info
        |""".stripMargin).createOrReplaceTempView("t_1")

    //指标4：不同房屋面积的平均房租和房屋个数
    spark.sql(
      """
        |insert overwrite table ads.housenum_and_avgrent_of_housetype
        |select type,count(1) numoftype,round(avg(rent)) avgrent from t_1
        |group by type
        |""".stripMargin)
    //指标5：房源信息最多中介的中介
    spark.sql(
      """
        |insert overwrite table ads.housenumber_of_intermediary
        |select intermediary_name,intermediary_number,count(1) housenumberofintermediary
        |from dws.dws_houseintermediary where intermediary_name is not NULL
        |group by intermediary_name,intermediary_number
        |""".stripMargin)
  }
}
