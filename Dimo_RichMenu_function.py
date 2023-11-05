# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:54:33 2023

@author: harry
"""
from linebot import  LineBotApi, WebhookHandler
from linebot.models import MessageEvent,FlexSendMessage, TextMessage, PostbackEvent, TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
import json

def SearchFunction(event,user_id,line_bot_api,liffid_food):
    message = TemplateSendMessage(
           alt_text='查詢功能按鈕樣板',
           template=ButtonsTemplate(
               title='查詢功能',  #主標題
               text='請選擇要使用的功能：',  #副標題
               actions=[
                   {
                      "type": "postback",
                      "label": "關鍵字查詢",
                      "data":'richMenu^txtSearch',
                      "text": "使用關鍵字查詢",
                      'inputOption':'openKeyboard'
                    },              
                   {
                        "type": "uri",
                        "label": "手動輸入資訊",
                        "uri": "https://liff.line.me/"+liffid_food
                    },
                   {
                      "type": "camera",
                      "label": "拍攝營養標籤"
                    },
                   {
                      "type": "cameraRoll",
                      "label": "選擇營養標籤照片"
                    }
               ]
           )
       )
    line_bot_api.reply_message(event.reply_token, message)
    
def item_create(index,block):
    item={
            block: {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "text",
                    "text": f"第{index+1}個食物",
                    "weight": "bold",
                    "size": "md",
                    "wrap": True
                    }
                ],
                "height": "20px",
                "flex": 2
                },
                {
                "type": "separator",
                "margin": "sm"
                },
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "text",
                        "text": "熱量",
                        "size": "xs"
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "filler"
                            }
                        ],
                        "height": "6px",
                        "width": "70%",
                        "backgroundColor": "#000000"
                        }
                    ],
                    "height": "22px"
                    },
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "text",
                        "text": "蛋白質",
                        "size": "xs"
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "filler"
                            }
                        ],
                        "height": "6px",
                        "width": "70%",
                        "backgroundColor": "#000000"
                        }
                    ],
                    "height": "22px"
                    },
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "text",
                        "text": "脂肪",
                        "size": "xs"
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "filler"
                            }
                        ],
                        "height": "6px",
                        "width": "70%",
                        "backgroundColor": "#000000"
                        }
                    ],
                    "height": "22px"
                    },
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "text",
                        "text": "碳水化合物",
                        "size": "xs"
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "filler"
                            }
                        ],
                        "height": "6px",
                        "width": "70%",
                        "backgroundColor": "#000000"
                        }
                    ],
                    "height": "22px"
                    }
                ],
                "margin": "sm",
                "spacing": "xs",
                "flex": 6
                },
                {
                "type": "separator",
                "margin": "md"
                },
                {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "修改",
                        "data": "hello"
                    },
                    "flex": 5,
                    "height": "sm"
                    },
                    {
                    "type": "separator"
                    },
                    {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "刪除",
                        "data": "hello"
                    },
                    "flex": 5,
                    "height": "sm"
                    }
                ],
                "spacing": "xs",
                "flex": 2
                },
                {
                "type": "separator",
                }
            ],
            "height": "180px",
            "paddingAll": "8px"
                      }
            }
    return item

def bubble_creat(num):
    index=0
    circle_time=3
    
    block=["header","hero","body"]
    quotient, remainder= divmod(num, 3)
    flex_content={
          "type": "carousel",
          "contents": [
          ]
        }
    #for quotient
    if remainder==0:
        for i in range(0,quotient):
            bubble_content={}
            for j in range(circle_time):
                if j==0:
                    bubble_content.update({"type": "bubble"})
                    bubble_content.update({"size": "micro"})
                bubble_content.update(item_create(index,block[j]))
                index+=1
            flex_content["contents"].append(bubble_content)
        
        return flex_content
    else:
        for i in range(0,quotient+1):
            bubble_content={}
            if i == (quotient):               
                circle_time=remainder
            print(circle_time)
            for j in range(circle_time):
                if j==0:
                    bubble_content.update({"type": "bubble"})
                    bubble_content.update({"size": "micro"})
                bubble_content.update(item_create(index,block[j]))
                index+=1
            flex_content["contents"].append(bubble_content)
        
        return flex_content
        
    
def How2Use(event,user_id,line_bot_api):
    message = TextSendMessage(
                text = '''您好~歡迎使用DIMO飲食資訊系統/n
請利用圖文選單執行相關操作，/n
系統操作：
1. 想查食物營養資訊？
 請點擊「查詢/紀錄」，你可以選擇查詢、拍照或手動輸入，並可以選擇是否添加到紀錄當中。
2. 想看飲食紀錄？
 請點擊「紀錄維護」，你可以查看今天或指定日期的飲食紀錄。

常見問題：
1. 想修改個人資料？
 請點擊「個人資料維護」，可以觀看填寫過的個人資料，並且進行修改。
2. 有飲食或健康的問題？
 請點擊「常見問題」，你可以找到相關問題選單，點擊想問的問題內容，將會取得客製化的智能回覆。
3. 需要操作指引或聯絡我們？
 請點擊「聯絡我們」，點及相關的選項，可以回覆和系統操作上的相關問題，若您對於本系統有優化或是技術上的建議，歡迎利用聯絡方式與我們進行聯繫。'''
        )
    line_bot_api.reply_message(event.reply_token,message)


def RecordFunction(event,user_id,line_bot_api):
    message = TemplateSendMessage(
           alt_text='紀錄功能按鈕樣板',
           template=ButtonsTemplate(
               title='紀錄功能',  #主標題
               text='請選擇要使用的功能：',  #副標題
               actions=[
                   {
                      "type": "postback",
                      "label": "觀看今天紀錄",
                      "data":"viewRecord^today",
                      "text": "觀看今天紀錄"
                    },              
                   {
                        "type": "postback",
                        "label": "選擇日期觀看紀錄",
                        "data":"viewRecord^chooseDate",
                        "text": "觀看特定日期紀錄"
                    },
               ]
           )
       )
    line_bot_api.reply_message(event.reply_token, message)
