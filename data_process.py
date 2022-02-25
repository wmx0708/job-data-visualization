import numpy as np
import pandas as pd

# 读出数据
job = pd.read_excel("job.xlsx")
company = pd.read_excel("company.xlsx")

# 清洗数据
# 筛掉城市地区，只保留城市名称
for i in range(job.shape[0]):
    if len(job["地区"][i]) > 2:
        job["地区"][i] = job["地区"][i][0:2]
    if "·" in job["薪酬"][i]:
        job["薪酬"][i] = job["薪酬"][i].split("·")[0]
job.to_excel("job_clean1.xlsx")
for i in range(job.shape[0]):
    if "-" in job["薪酬"][i]:
        job["薪酬"][i] = job["薪酬"][i].split("-")[0]
job.to_excel("job_clean2.xlsx")
# for i in range(len(job["薪酬"])):
#     if "-" in job["薪酬"][i]:
#         if int(job["薪酬"][i].split("-")[0]) <= 10:
#             job["薪酬"][i] = "<=10k"
#         elif int(job["薪酬"][i].split("-")[0]) <= 15:
#             job["薪酬"][i] = "10k-15k"
#         elif int(job["薪酬"][i].split("-")[0]) <= 20:
#             job["薪酬"][i] = "15k-20k"
#         elif int(job["薪酬"][i].split("-")[0]) <= 25:
#             job["薪酬"][i] = "20k-25k"
#         elif int(job["薪酬"][i].split("-")[0]) <= 30:
#             job["薪酬"][i] = "25k-30k"
#         elif int(job["薪酬"][i].split("-")[0]) <= 40:
#             job["薪酬"][i] = "30k-40k"
#         elif int(job["薪酬"][i].split("-")[0]) > 40:
#             job["薪酬"][i] = ">40k"
#
# job.to_excel("job_clean.xlsx")
#
# print(company.shape[0])
# company.dropna(inplace = True)
# company.to_excel("company_clean.xlsx")
# company1=pd.read_excel("company_clean.xlsx")
#
# for i in range(company1.shape[0]):
#     if len(company1["地区"][i]) > 2:
#         company1["地区"][i] = company1["地区"][i][0:2]
#     if "·" in company1["薪酬"][i]:
#         company1["薪酬"][i] = company1["薪酬"][i].split("·")[0]
#
# for i in range(len(company1["薪酬"])):
#     if "-" in company1["薪酬"][i]:
#         company1["薪酬"][i]=int(company1["薪酬"][i].split("-")[0])
#
# company1.to_excel("company_clean.xlsx")