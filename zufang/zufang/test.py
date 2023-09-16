import requests
from bs4 import BeautifulSoup

# 请求拉勾网大数据岗位招聘信息
url = 'https://www.lagou.com/wn/jobs?labelWords=&fromSearch=true&suginput=&kd=%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

response = requests.get(url, headers=headers)

# 解析网页
soup = BeautifulSoup(response.text, 'lxml')

# 提取招聘信息
jobs = soup.find_all('li', class_='con_list_item')

# 输出招聘信息
print('# 拉勾网大数据岗位招聘信息')
for job in jobs:
    job_name = job.find('div', class_='position').find('div', class_='p_top').find('a').get_text()
    job_salary = job.find('div', class_='position').find('span', class_='money').get_text()
    job_city = job.find('div', class_='position').find('div', class_='p_top').find('em').get_text()
    job_experience = job.find('div', class_='position').find('div', class_='li_b_l').get_text()
    job_company = job.find('div', class_='company').find('div', class_='company_name').find('a').get_text()
    job_industry = job.find('div', class_='company').find('div', class_='industry').get_text()
    print('## {}\n- 薪资：{}\n- 城市：{}\n- 经验：{}\n- 公司：{}\n- 行业：{}\n'.format(job_name, job_salary, job_city, job_experience,
                                                                        job_company, job_industry))
