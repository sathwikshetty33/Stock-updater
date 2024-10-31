import requests
from pyexpat.errors import messages
from twilio.rest import Client


api_key=''
stock_endpoint='https://www.alphavantage.co/query'
news_endpoint='https://newsapi.org/v2/everything'
newsapikey=''
stockname='TSLA'
company_name='Tesla Inc'
parameters={
'function':'TIME_SERIES_DAILY',
'symbol':stockname,
'apikey':api_key,
}
sid=''
authtoken=''
client = Client(sid,authtoken)
com=requests.get(url=stock_endpoint,params=parameters)
data=com.json()['Time Series (Daily)']
pricelist=[value for (key,value) in data.items()]
yesterday_list=pricelist[0]
yesterday_closing_price=yesterday_list['4. close']
daybefore_yesterday_list=pricelist[1]
daybefore_yesterday_price=daybefore_yesterday_list['4. close']
diff=(float(yesterday_closing_price)-float(daybefore_yesterday_price))
diff_per=round(diff/float(yesterday_closing_price))*100
updown=None
if diff_per>0:
    updown='🔺'
else:
    updown='🔻'
if abs(diff_per) >0:
    news_parameters={
        'apiKey':newsapikey,
        'q': company_name,

    }
    con1=requests.get(url=news_endpoint,params=news_parameters)
    articles=con1.json()['articles'][:3]
    articles_list=[f"{stockname} \n{updown} {abs(diff_per)} % \n Headlines: {article['title']}. \nBrief: {article['description']}" for article in articles]
    for article in articles_list:
        message=client.messages.create(
            body=article,
            from_='+17063506765',
            to='+919620146061'
        )
        print('succes')