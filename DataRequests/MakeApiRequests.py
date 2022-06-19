import requests
import json
import pandas as pd
import datetime
import dateutil.parser
from datetime import date
from datetime import datetime
from datetime import timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('mongodb://admin:F5tMazRj47cYqm33e@35.88.43.45:27017/')
db=client.compass


class Api:
    def __init__(self):
        pass
    


    
    

    client = MongoClient('mongodb://admin:F5tMazRj47cYqm33e@35.88.43.45:27017/')
    db=client.compass
    
    


    def makeApiRequestForsignup(self, country_name):
        # import pymongo
        import dateutil
        dateStr = '2021-08-01T00:00:00.000Z'
        myDatetime = dateutil.parser.parse(dateStr)
        collection2=db.user_master
        data=[{"$match":{
         '$and':[{ 'USER_NAME':{"$not":{"$regex":"test",'$options':'i'}}},
                   {'EMAIL_ID':{"$not":{"$regex":"test",'$options':'i'}}},
                     {'EMAIL_ID':{"$not":{"$regex":"1gen",'$options':'i'}}},
          {'INCOMPLETE_SIGNUP':{"$ne":'Y'}},
          {'IS_DISABLED':{"$ne":'Y'}},
          {'IS_BLOCKED':{"$ne":'Y'}},
                  {'schoolId.NAME':{'$not':{"$regex":'Blocked','$options':'i'}}},
          {'schoolId.BLOCKED_BY_CAP':{'$exists':0}},{"CREATED_DATE":{'$gte':myDatetime
            }}]}}]
        total_user_count=len(list(collection2.aggregate(data)))
        # total_user_count=len(df_average1)
        print(total_user_count)

        #family_count

        data1=[{"$match":{
                '$and':[{ 'USER_NAME':{"$not":{"$regex":"test",'$options':'i'}}},
                        {'EMAIL_ID':{"$not":{"$regex":"test",'$options':'i'}}},
                            {'EMAIL_ID':{"$not":{"$regex":"1gen",'$options':'i'}}},
                {'INCOMPLETE_SIGNUP':{"$ne":'Y'}},{'ROLE_ID._id':{'$eq':ObjectId("5f155b8a3b6800007900da2b")}},
                {'IS_DISABLED':{"$ne":'Y'}},
                {'IS_BLOCKED':{"$ne":'Y'}},
                        {'schoolId.NAME':{'$not':{"$regex":'Blocked','$options':'i'}}},
                {'schoolId.BLOCKED_BY_CAP':{'$exists':0}},{"CREATED_DATE":{'$gte':myDatetime
            }}]}}]
        total_family_count=len(list(collection2.aggregate(data1)))
        # total_family_count=len(df_average2)
        print(total_family_count)

        # #active users

        # data=[{"$match":{
        #         '$and':[{ 'USER_NAME':{"$not":{"$regex":"test",'$options':'i'}}},
        #                 {'EMAIL_ID':{"$not":{"$regex":"test",'$options':'i'}}},
        #                     {'EMAIL_ID':{"$not":{"$regex":"1gen",'$options':'i'}}},
        #         {'INCOMPLETE_SIGNUP':{"$ne":'Y'}},
        #         {'IS_DISABLED':{"$ne":'Y'}},
        #         {'IS_BLOCKED':{"$ne":'Y'}},
        #                 {'schoolId.NAME':{'$not':{"$regex":'Blocked','$options':'i'}}},
        #         {'schoolId.BLOCKED_BY_CAP':{'$exists':0}},{"CREATED_DATE":{'$gte':myDatetime
        #     }}]}},{'$project':{'_id':0,'ID':'$_id'}}]
        # df_average3=pd.DataFrame(list(collection2.aggregate(data)))
        # user_list=df_average3['ID'].to_list()

        # collection3=db.audio_track_master
        # data_audio=[{"$match":{
        #         '$and':[{ 'USER_ID.USER_NAME':{"$not":{"$regex":"test",'$options':'i'}}},
        #                 {'USER_ID.EMAIL_ID':{"$not":{"$regex":"test",'$options':'i'}}},
        #                     {'USER_ID.EMAIL_ID':{"$not":{"$regex":"1gen",'$options':'i'}}},
        #         {'USER_ID.INCOMPLETE_SIGNUP':{"$ne":'Y'}},
        #         {'USER_ID.IS_DISABLED':{"$ne":'Y'}},
        #         {'USER_ID.IS_BLOCKED':{"$ne":'Y'}},
        #                     {'USER_ID.schoolId.NAME':{'$not':{"$regex":'Blocked','$options':'i'}}},
        #         {'USER_ID.schoolId.BLOCKED_BY_CAP':{'$exists':0}},{'USER_ID._id':{'$in':user_list}},{"MODIFIED_DATE" :{'$gte':"2021-08-01 00:00:00"
        #     }}]}},
        # {'$project':{'_id':0,
        #             'USER_ID':'$USER_ID._id',
                    
        #             }
        #             }]
        # df_average4=pd.DataFrame(list(collection3.aggregate(data_audio)))
        # print("================")
        # print(df_average4)
        # total_active=len(set(df_average4["USER_ID"]))




        # url = "https://covid-193.p.rapidapi.com/statistics"
        # querystring = {"country": "india"}
        # headers = {
        #     'x-rapidapi-host': "covid-193.p.rapidapi.com",
        #     'x-rapidapi-key': "482a8f8516msh16204eb9d1f4f68p1a9146jsnf33914c7300e"
        # }
        # response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response.text)
        # js = json.loads(response.text)
        # print("******", js)
        # result = js.get('response')[0]
        # print(result.get('cases'))
        # print("*helloooooooo" * 20)
        # return result.get('cases') , result.get('deaths'),result.get('tests')
        return {"all":total_user_count},{"family":total_family_count}

    def csy_first_date():
        date_today =datetime.date.today()
    #     print(date_today)
    #     date_today='2024-07-01'
    #     day_end=datetime.datetime.strptime(date_today, '%Y-%m-%d').date()
        initial_date='2020-08-01'
        day1=datetime.datetime.strptime(initial_date, '%Y-%m-%d').date()
        # Check if leap year in the calculation
        if ((day1.year+1) % 4) == 0:
            if ((day1.year+1) % 100) == 0:
                if ((day1.year+1) % 400) == 0:
                    days_diff=1
                else:
                    days_diff=1
            else:
                days_diff=1
        else:
            days_diff=0
        if ((date_today-day1).days<(365+days_diff)):
            day_1=day1
        else:
            day1=day1+timedelta(days=(365+days_diff))
            day_1=day1
        csy_date=datetime.datetime.strptime((day_1.strftime('%Y-%m-%d')), '%Y-%m-%d')
        return csy_date

    def makeApiRequestForCounrty(self, country_name):
        url = "https://covid-193.p.rapidapi.com/statistics"
        querystring = {"country": country_name}
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "482a8f8516msh16204eb9d1f4f68p1a9146jsnf33914c7300e"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('response')[0]
        print(result.get('cases'))
        print("*" * 20)
        return result.get('cases') , result.get('deaths'),result.get('tests')


    def makeApiRequestForIndianStates(self):
        url = "https://covid19-data.p.rapidapi.com/india"
        headers = {
            'x-rapidapi-host': "covid19-data.p.rapidapi.com",
            'x-rapidapi-key': "482a8f8516msh16204eb9d1f4f68p1a9146jsnf33914c7300e"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        #result = js.get('list')
        return js


    def makeApiWorldwide(self):
        url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
        headers = {
            "x-rapidapi-host": "covid-19-statistics.p.rapidapi.com",
            "x-rapidapi-key": "482a8f8516msh16204eb9d1f4f68p1a9146jsnf33914c7300e"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('data')

        return result

