# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
from .items import *

class ZufangPipeline:
    Housebasic_list = []
    Housedetail_list = []
    Cost_list = []
    Intermediary_list = []

    def open_spider(self, spider):


        # 如果连接数据库失败会自动重新链接
        try:
            host = '192.168.153.120'
            user = 'root'
            password = '123456'
            database = 'zufang'
            charset = 'utf8'
            self.conn = pymysql.Connect(host=host, user=user, password=password, database=database, charset=charset)
            self.cur = self.conn.cursor()
        except:
            self.open_spider()
        else:
            spider.logger.info('MySQL: connected')

            self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
            spider.cur = self.cur

    def process_item(self, item, spider):

        if isinstance(item, HousebasicItem):
            if len(self.Housebasic_list) == 30:
                # 这里是判断你一次性要插入多少条数据可自行修改
                self.insert_data(self.Housebasic_list)
                self.Housebasic_list = []
            else:
                self.Housebasic_list.append((item['verification_code'], item['maintain_time'], item['title'],
                                             item['district'], item['street'], item['community_name'],
                                             item['lease_type'], item['house_type']))


        elif isinstance(item, HousedetailItem):
            if len(self.Housedetail_list) == 30:
                # 这里是判断你一次性要插入多少条数据可自行修改
                self.insert_data(self.Housedetail_list)
                self.Housedetail_list = []
            else:
                self.Housedetail_list.append(
                    (item['verification_code'], item['area'], item['orientation'], item['check_in'],
                     item['floor'], item['elevator'], item['car_park'], item['water'], item['electric'], item['gas'],
                     item['heating']))


        elif isinstance(item, CostItem):
            if len(self.Cost_list) == 30:
                # 这里是判断你一次性要插入多少条数据可自行修改
                self.insert_data(self.Cost_list)
                self.Cost_list = []
            else:
                self.Cost_list.append((item['verification_code'], item['rent'], item['payment_type'], item['deposit'],
                                       item['service_charge'], item['agency_fee']))


        elif isinstance(item, IntermediaryItem):
            if len(self.Intermediary_list) == 30:
                # 这里是判断你一次性要插入多少条数据可自行修改
                self.insert_data(self.Intermediary_list)
                self.Intermediary_list = []
            else:
                self.Intermediary_list.append((item['verification_code'], item['intermediary_name'],
                                               item['intermediary_number'], item['mechanism_number']))

        return item

    def insert_data(self, data):
        # 这个函数是用来往数据库中写入数据的。传过来的data是一个元祖，经尝试字典是不可以的，也就是说我们不可以直接把item传给这个函数。
        print('begin insert data')
        print(data)
        print(len(data[0]))
        if len(data[0]) == 8:
            try:
                sql = 'INSERT INTO housebasic_table(verification_code,maintain_time,title,district,street,community_name,lease_type,house_type) ' \
                      'VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE maintain_time = values(maintain_time),title = values(title) ,' \
                      'district = values(district),street = values(street),community_name = values(community_name),lease_type = values(lease_type),' \
                      'house_type = values(house_type)'
                self.cur.executemany(sql, data)
                self.conn.commit()
                print("success insert 300 data")
            except Exception as e:
                print(e)
                self.conn.rollback()
                print('insert warnning')

        elif len(data[0]) == 4:
            try:
                sql = 'INSERT INTO intermediary_table(verification_code,intermediary_name,intermediary_number,mechanism_number) VALUES (%s,%s,%s,%s)' \
                      'ON DUPLICATE KEY UPDATE intermediary_name = values(intermediary_name),intermediary_number = values(intermediary_number) ,' \
                      'mechanism_number = values(mechanism_number)'
                self.cur.executemany(sql, data)
                self.conn.commit()
                print("success insert 300 data")
            except Exception as e:
                print(e)
                self.conn.rollback()
                print('insert warnning')

        elif len(data[0]) == 6:
            try:
                sql = 'INSERT INTO cost_table(verification_code,rent,payment_type,deposit,service_charge,agency_fee) VALUES (%s,%s,%s,%s,%s,%s)' \
                      'ON DUPLICATE KEY UPDATE rent = values(rent),payment_type = values(payment_type),' \
                      'deposit = values(deposit),service_charge = values(service_charge),agency_fee = values(agency_fee)'
                self.cur.executemany(sql, data)
                self.conn.commit()
                print("success insert 300 data")
            except Exception as e:
                print(e)
                self.conn.rollback()
                print('insert warnning')

        elif len(data[0]) == 11:
            try:
                sql = 'INSERT INTO housedetail_table(verification_code,area,orientation' \
                      ',check_in,floor,elevator,car_park,water,electric,gas,heating) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' \
                      'ON DUPLICATE KEY UPDATE area = values(area),orientation = values(orientation),' \
                      'check_in = values(check_in),floor = values(floor),elevator = values(elevator),car_park = values(car_park),' \
                      'car_park = values(car_park),water = values(water),electric = values(electric),gas = values(gas),heating = values(heating)'
                self.cur.executemany(sql, data)
                self.conn.commit()
                print("success insert 300 data")
            except Exception as e:
                print(e)
                self.conn.rollback()
                print('insert warnning')

    def close_spider(self, spider):
        self.insert_data(self.Housebasic_list)
        self.insert_data(self.Housedetail_list)
        self.insert_data(self.Cost_list)
        self.insert_data(self.Intermediary_list)
        self.conn.commit()
        self.cur.close()
        self.conn.close()
