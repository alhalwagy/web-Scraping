from bs4 import BeautifulSoup
import requests
url = "https://www.google.com/search?q=cryptocurrency+prices+table&sxsrf=ALiCzsZYkKBDN06eHbB0yDIbNykMRcGHYA%3A1672195327026&ei=_6yrY8yLAdibkdUPsLe8gAI&oq=Cryptocurrency+Prices+&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgBMgQIIxAnMgQIIxAnMggIABCABBDLATIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLATIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLATIICAAQgAQQywE6BwgjELADECc6CggAEEcQ1gQQsAM6BwgAELADEEM6DQgAEOQCENYEELADGAE6EgguEMcBENEDEMgDELADEEMYAkoECEEYAEoECEYYAVCmBlimBmDlFGgBcAF4AIABngKIAZ4CkgEDMi0xmAEAoAEByAERwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz-serp"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
tbody = doc.tbody
trs = tbody.contents
# print(trs)
prices = {}
for tr in trs[2:4]:
	name, price = tr.contents[1:3]
	fixed_name = name.string
	fixed_price = price.string
	prices[fixed_name] = fixed_price
print(prices)