# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 00:54:17 2023

@author: harry
"""
from linebot import  LineBotApi, WebhookHandler
from linebot.models import MessageEvent,FlexSendMessage, TextMessage, PostbackEvent, TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn

def respond_exerciseAndMeal(event,user_id,line_bot_api):
    message=FlexSendMessage(
            alt_text='運動及健康飲食問題選單',
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
                        "text": "運動及健康飲食"
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
                                "text": "請選擇要問的問題",
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
                          "type": "message",
                          "label": "運動跟飲食怎麼搭配?",
                          "text":'請問健康的身體狀況，該如何搭配運動以及飲食呢?'
                        }
                      },
                      {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                          "type": "message",
                          "label": "我該從事什麼樣的運動?",
                          "text":'請根據我要達成的目標，提供我一些可以從事的運動項目。'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "運動前後的飲食?",
                          "text":'當我在運動前後，可以搭配什麼樣的飲食呢?'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "我今天吃的健康嗎?",
                          "text":'根據我今天的飲食狀況，請幫我分析我的飲食是否符合健康標準?'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "我今天應該運動嗎?",
                          "text":'根據我今天的飲食狀況，需要搭配運動來提升消耗嗎?'
                        }
                      }
                    ],
                    "spacing": "md"
                  }
                }
            )

    
def respond_resipeOffering(event,user_id,line_bot_api):
    message = FlexSendMessage(
           alt_text='食譜推薦或料理方式問題選單',
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
                        "text": "食譜推薦及料理方式"
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
                                "text": "請選擇要問的問題",
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
                          "type": "message",
                          "label": "低卡餐點食譜?",
                          "text":'請給我一份低熱量的健康料理食譜?'
                        }
                      },
                      {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                          "type": "message",
                          "label": "素食料理?",
                          "text":'請推薦我素食料理的相關食譜。'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "低碳飲食吃什麼?",
                          "text":'請給我一些關於低碳的料理食譜。'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "高纖蔬食料理方式?",
                          "text":'請提供我一些高纖蔬食的料理食譜。'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "健康的早餐?",
                          "text":'請教我怎麼做一份健康又活力的早餐。'
                        }
                      }
                    ],
                    "spacing": "md"
                  }
                }
           )
    line_bot_api.reply_message(event.reply_token, message)
    
    
def respond_mealSuggest(event,user_id,line_bot_api):
    message = FlexSendMessage(
           alt_text='飲食建議或料理推薦問題選單',
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
                        "text": "飲食建議或料理推薦"
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
                                "text": "請選擇要問的問題",
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
                          "type": "message",
                          "label": "吃什麼來達成目標?",
                          "text":'若我想達成我的目標，可以吃些什麼?'
                        }
                      },
                      {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                          "type": "message",
                          "label": "改善皮膚狀況?",
                          "text":'吃些什麼食物可以改善皮膚健康呢?'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "運動前後的飲食?",
                          "text":'當我在運動前後，可以吃些什麼?'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "我還能吃些什麼?",
                          "text":'根據我今天的飲食狀況，給我一些推薦的餐食?'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "高蛋白的食物選擇?",
                          "text":'若我想要補充蛋白質，可以吃什麼?'
                        }
                      }
                    ],
                    "spacing": "md"
                  }
                }
           )
    line_bot_api.reply_message(event.reply_token, message)
    
def respond_eatingMethod(event,user_id,line_bot_api):
    message = FlexSendMessage(
           alt_text='飲食方法或準則問題選單',
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
                        "text": "飲食方法或準則"
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
                                "text": "請選擇要問的問題",
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
                          "type": "message",
                          "label": "我每天應該吃多少?",
                          "text":'請根據我的身體狀況，我每天應該攝取多少呢?'
                        }
                      },
                      {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                          "type": "message",
                          "label": "怎麼吃來達成目標?",
                          "text":'請根據我要達成的目標，建議我一些飲食方法。'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "素食者怎麼吃?",
                          "text":'我是素食者，請問該怎麼吃來達成目標呢?'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "斷食方法?",
                          "text":'請問常見的斷食方法，是否適合我?'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "怎樣才能吃得健康?",
                          "text":'我想要活得健康，可以怎麼吃?'
                        }
                      }
                    ],
                    "spacing": "md"
                  }
                }
           )
    line_bot_api.reply_message(event.reply_token, message)
    
def respond_foodInfo(event,user_id,line_bot_api):
    message = FlexSendMessage(
           alt_text='食品營養資訊問題選單',
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
                        "text": "食品營養資訊"
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
                                "text": "請選擇要問的問題",
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
                          "type": "message",
                          "label": "營養素攝取?",
                          "text":'請問我一天該攝取多少營養素呢?'
                        }
                      },
                      {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                          "type": "message",
                          "label": "分析今日飲食?",
                          "text":'請根據我今天的飲食狀況，幫我整理我吃了多少營養素。'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "珍珠奶茶的熱量是多少?",
                          "text":'請問一杯珍珠奶茶的營養資訊是多少?'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "補充蛋白質?",
                          "text":'請列舉一些含有豐富蛋白質影養素的食物。'
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "營養資訊的重要性?",
                          "text":'請問健康飲食，一定要計算營養素嗎?'
                        }
                      }
                    ],
                    "spacing": "md"
                  }
                }
           )
    line_bot_api.reply_message(event.reply_token, message)
    