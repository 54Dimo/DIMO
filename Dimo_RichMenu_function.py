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

def askingStandardQuestion(event,user_id,line_bot_api):
    message = FlexSendMessage(
           alt_text='問題類別選單',
           contents={
                  "type": "bubble",
                  "size": "hecto",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "weight": "bold",
                        "size": "xl",
                        "text": "問題類別列表"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                              {
                                "type": "text",
                                "text": "請選擇要問的問題類別",
                                "wrap": True,
                                "size": "md"
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                          "type": "postback",
                          "label": "食品營養資訊",
                          "data":'stdQuestion^foodInfo',
                          'inputOption':'closeRichMenu'
                        }
                      },
                      {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                          "type": "postback",
                          "label": "飲食方法或準則",
                          "data":'stdQuestion^eatingMethod',
                          'inputOption':'closeRichMenu'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "食譜推薦或料理方式",
                          "data":'stdQuestion^resipeOffering',
                          'inputOption':'closeRichMenu'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "運動及健康飲食",
                          "data":'stdQuestion^exerciseAndMeal',
                          'inputOption':'closeRichMenu'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "飲食建議或料理推薦",
                          "data":'stdQuestion^mealSuggest',
                          'inputOption':'closeRichMenu'
                        }
                      }
                    ],
                    "spacing": "md"
                  }
                }
           )
    line_bot_api.reply_message(event.reply_token, message)
    
def contect2Us(event,user_id,line_bot_api):
    message = TemplateSendMessage(
           alt_text='常見問題選單',
           template=ButtonsTemplate(
               title='常見問題',  #主標題
               text='請選擇要使用的功能：',  #副標題
               actions=[
                   {
                      "type": "message",
                      "label": "如何修改紀錄內容?",
                      "text": "想要查看或修改紀錄，\n請先點擊「系統操作」選單頁籤\n接著在右下角，點擊「紀錄維護」\n\n隨後會出現兩個功能選單:\n「觀看今天紀錄」、「選擇日期觀看紀錄」點擊後即會顯示該日期的紀錄資料，即可點選「修改」進行份量更改。"
                    },              
                   {
                        "type": "message",
                        "label": "身高、體重該從哪裡變更?",
                        "text": "想要查看或修改個人資料，\n請先點擊「常見問題」選單頁籤\n接著在右上角，點擊「個人資料維護」\n隨後會出現一個功能選單:\n點擊「個人資料」按鈕後，即會開啟網頁，可以在此網頁表單上看到先前填寫的資料，也可以直接進行更正。\n更正完後不要忘了點即確認送出，送出後即會完成修改。"
                    },
                   {
                      "type": "message",
                      "label": "系統所顯示的食物份量單位基準?",
                      "text": "您好，本系統在查詢後所顯示的營養素及熱量單位，都是以每種食物的「每100公克」為份量單位顯示。"
                    },
                   {
                      "type": "postback",
                      "label": "聯絡我們",
                      "data":'contect2Us'
                    }
               ]
           )
       )
    line_bot_api.reply_message(event.reply_token, message)
    
def How2Use(event,user_id,line_bot_api):
    message = TextSendMessage(
                text = '''您好~歡迎使用DIMO飲食資訊系統
請利用圖文選單執行相關操作，
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
