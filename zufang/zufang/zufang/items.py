# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


# 房屋基本信息
class HousebasicItem(scrapy.Item):
    # 核验码
    verification_code = scrapy.Field()

    # 维护时间
    maintain_time = scrapy.Field()
    # 房源标题
    title = scrapy.Field()
    # 所在区
    district = scrapy.Field()
    # 所在路
    street = scrapy.Field()
    # 小区名
    community_name = scrapy.Field()
    # 出租类型
    lease_type = scrapy.Field()
    # 户型
    house_type = scrapy.Field()


# 房屋详情信息
class HousedetailItem(scrapy.Item):
    # 核验码
    verification_code = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 朝向
    orientation = scrapy.Field()
    # 入住
    check_in = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 电梯
    elevator = scrapy.Field()
    # 车位
    car_park = scrapy.Field()
    # 用水
    water = scrapy.Field()
    # 用电
    electric = scrapy.Field()
    # 燃气
    gas = scrapy.Field()
    # 采暖
    heating = scrapy.Field()


# 费用ITEM
class CostItem(scrapy.Item):
    # 核验码
    verification_code = scrapy.Field()
    # 房租
    rent = scrapy.Field()
    # 付款方式
    payment_type = scrapy.Field()
    # 押金
    deposit = scrapy.Field()
    # 服务费
    service_charge = scrapy.Field()
    # 中介费
    agency_fee = scrapy.Field()


# 中介信息ITEM
class IntermediaryItem(scrapy.Item):
    # 核验码
    verification_code = scrapy.Field()
    # 中介名
    intermediary_name = scrapy.Field()
    # 中介编号
    intermediary_number = scrapy.Field()
    # 机构备案编号
    mechanism_number = scrapy.Field()
