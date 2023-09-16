import scrapy
import time
from ..items import CostItem, HousedetailItem, HousebasicItem, IntermediaryItem


class HfzufangSpider(scrapy.Spider):
    name = 'hfzufang'
    # allowed_domains = ['www.xxx.com']
    # 起始URL
    start_urls = ['https://hf.lianjia.com/zufang/pg1/']

    pg = 2

    def parse(self, response):
        div_list = response.xpath('//div[@class = "content__list"]/div')
        for div in div_list:
            # 拼接详情url
            detail_url = 'https://hf.lianjia.com' + div.xpath(
                './/div[@class="content__list--item--main"]/p[1]/a/@href').get()
            time.sleep(1)
            # 返回给parse_detailhouse方法处理详情页数据
            yield scrapy.Request(url=detail_url, callback=self.parse_detailhouse)
            # 爬取下一页数据
        if self.pg <= 100:
            next_url = f'https://hf.lianjia.com/zufang/pg{self.pg}'
            print(next_url)
            self.pg += 1
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)

    # 解析详情页方法
    def parse_detailhouse(self, response):

        try:
            # 房源标题
            title = response.xpath('/html/body/div[3]/div[1]/div[3]/p/text()').get().strip().replace("\n", "")
            # 维护时间

            maintain_time = \
                response.xpath('//div[@class="content__subtitle"]/text()').get().strip().replace("\n", "").split("：")[1]
            # 核验码
            verification_code = response.xpath('//i[@class="gov_title"]//text()').getall()[1].strip().replace("\n", "")
            if verification_code.startswith("合肥"):
                verification_code = verification_code.split("核验码")[1]
            else:
                verification_code = verification_code.split("：")[1]
            # 所在区
            district = response.xpath('/html/body/div[3]/div[1]/div[10]/p[1]/a[2]/text()').get().split("租")[0]
            # 所在路
            street = response.xpath('/html/body/div[3]/div[1]/div[10]/p[1]/a[3]/text()').get().split("租")[0]
            # 小区名
            community_name = response.xpath('/html/body/div[3]/div[1]/div[10]/h1/a/text()').get().split("租")[0]
            # 出租类型
            lease_type = response.xpath('//*[@id="aside"]/ul/li[1]/text()').get()
            # 户型
            house_type = response.xpath('//*[@id="aside"]/ul/li[2]/text()').get()

            # 中介信息
            # 中介名
            intermediary_name = response.xpath('//*[@id="aside"]/div[2]/div[2]/div[1]/span[2]/text()').get()
            # 中介编号
            intermediary_number = response.xpath('//*[@id="aside"]/div[2]/div[2]/div[3]/a/text()').get()
            # 机构备案编号
            mechanism_number = response.xpath('//*[@id="aside"]/div[2]/div[2]/div[4]/a/text()').get()
            if intermediary_number != None:
                intermediary_number = intermediary_number.split("详情")[0].strip()
                if mechanism_number != None:
                    mechanism_number = mechanism_number.split("详情")[0].strip()
            else:
                pass

            # 房屋详情信息
            # 面积
            area = response.xpath('//*[@id="info"]/ul[1]/li[2]/text()').get().split("：")[1].replace("㎡", "")
            # 朝向
            orientation = response.xpath('//*[@id="info"]/ul[1]/li[3]/text()').get().split("：")[1]
            # 入住
            check_in = response.xpath('//*[@id="info"]/ul[1]/li[6]/text()').get().split("：")[1]
            # 楼层
            floor = response.xpath('//*[@id="info"]/ul[1]/li[8]/text()').get().split("：")[1]
            # 电梯
            elevator = response.xpath('//*[@id="info"]/ul[1]/li[9]/text()').get().split("：")[1]
            # 车位
            car_park = response.xpath('//*[@id="info"]/ul[1]/li[11]/text()').get().split("：")[1]
            # 用水
            water = response.xpath('//*[@id="info"]/ul[1]/li[12]/text()').get().split("：")[1]
            # 用电
            electric = response.xpath('//*[@id="info"]/ul[1]/li[14]/text()').get().split("：")[1]
            # 燃气
            gas = response.xpath('//*[@id="info"]/ul[1]/li[15]/text()').get().split("：")[1]
            # 采暖
            heating = response.xpath('//*[@id="info"]/ul[1]/li[17]/text()').get().split("：")[1]

            # 费用详情
            # 房租
            rent = response.xpath(
                '//div[@class="content__core"]//div[@class="content__aside--title"]/span/text()').get().strip().replace(
                "\n", "").replace("㎡", "")
            # 付款方式
            payment_type = response.xpath('//*[@id="cost"]/div/div[2]/div/ul/li[1]/text()').get()
            # 押金
            deposit = response.xpath('//*[@id="cost"]/div/div[2]/div/ul/li[3]/text()').get()
            # 服务费
            service_charge = response.xpath('//*[@id="cost"]/div/div[2]/div/ul/li[4]/text()').get()
            # 中介费
            agency_fee = response.xpath('//*[@id="cost"]/div/div[2]/div/ul/li[5]/text()').get()
        except Exception as e:
            print(e)
        else:
            housebasicItem = HousebasicItem(verification_code=verification_code, maintain_time=maintain_time,
                                            title=title,
                                            district=district,
                                            street=street, community_name=community_name
                                            , lease_type=lease_type, house_type=house_type)
            print(housebasicItem)
            yield housebasicItem
            intermediaryItem = IntermediaryItem(verification_code=verification_code,
                                                intermediary_name=intermediary_name,
                                                intermediary_number=intermediary_number,
                                                mechanism_number=mechanism_number)
            yield intermediaryItem
            housedetailItem = HousedetailItem(verification_code=verification_code, area=area, orientation=orientation,
                                              check_in=check_in, floor=floor, elevator=elevator,
                                              car_park=car_park, water=water, electric=electric, gas=gas,
                                              heating=heating)
            yield housedetailItem
            costItem = CostItem(verification_code=verification_code, rent=rent, payment_type=payment_type,
                                deposit=deposit,
                                service_charge=service_charge,
                                agency_fee=agency_fee)
            yield costItem
