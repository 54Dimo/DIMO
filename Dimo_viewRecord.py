# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 04:21:26 2023

@author: harry
"""
import DB_Control as db

def item_create(index,block,data):
    colory=(data[index][6]*data[index][10])/8
    protein=(data[index][7]*data[index][10])/2
    fat=(data[index][8]*data[index][10])/2
    carb=(data[index][9]*data[index][10])/2
    if (colory>=100):
        colory=100
    if(protein>=100):
        protein=100
    if(fat>=100):
        fat=100
    if(carb>=100):
        carb=100
    item={
            block: {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": f"{data[index][4]}",
                    "weight": "bold",
                    "size": "sm",
                    "wrap": True,
                    "flex": 7
                  },
                  {
                    "type": "text",
                    "text": f"{data[index][10]}份",
                    "size": "xxs",
                    "flex": 2,
                    "align": "end",
                    "gravity": "bottom",
                    "offsetTop": "xs"
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
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "熱量",
                            "size": "xs",
                            "flex": 6
                          },
                          {
                            "type": "text",
                            "text": f"{round(data[index][6]*data[index][10],1)}大卡",
                            "size": "xxs",
                            "align": "end",
                            "gravity": "bottom",
                            "offsetTop": "xs",
                            "flex": 4
                          }
                        ]
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
    					"width": f"{colory}%",
                        "backgroundColor": "#4b77a8"
                      }
                    ],
                    "height": "22px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "蛋白質",
                            "size": "xs",
                            "flex": 6
                          },
                          {
                            "type": "text",
                            "text": f"{round(data[index][7]*data[index][10],1)}公克",
                            "size": "xxs",
                            "align": "end",
                            "gravity": "bottom",
                            "offsetTop": "xs",
                            "flex": 4
                          }
                        ]
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
    					"width": f"{protein}%",
                        "backgroundColor": "#4aa04a"
                      }
                    ],
                    "height": "22px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "脂肪",
                            "size": "xs",
                            "flex": 6
                          },
                          {
                            "type": "text",
                            "text": f"{round(data[index][8]*data[index][10],1)}公克",
                            "size": "xxs",
                            "align": "end",
                            "gravity": "bottom",
                            "offsetTop": "xs",
                            "flex": 4
                          }
                        ]
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
    					"width": f"{fat}%",
                        "backgroundColor": "#cf5954"
                      }
                    ],
                    "height": "22px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "碳水化合物",
                            "size": "xs",
                            "flex": 6
                          },
                          {
                            "type": "text",
                            "text": f"{round(data[index][9]*data[index][10],1)}公克",
                            "size": "xxs",
                            "align": "end",
                            "gravity": "bottom",
                            "offsetTop": "xs",
                            "flex": 4
                          }
                        ]
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
    					"width": f"{carb}%",
                        "backgroundColor": "#e59d32"
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
                      "data": "udRecord^"+str(data[index][0])+":"+data[index][4]+":"+str(data[index][2])
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
                      "data": "dlRecord^"+str(data[index][0])+":"+data[index][4]+":"+str(data[index][2])
                    },
                    "flex": 5,
                    "height": "sm"
                  }
                ],
                "spacing": "xs",
                "flex": 2
              },
              {
                "type": "separator"
              }
            ],
            "height": "180px",
            "paddingAll": "8px"
                      }
            }
    return item

def bubble_creat(num,data):
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
                bubble_content.update(item_create(index,block[j],data))
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
                bubble_content.update(item_create(index,block[j],data))
                index+=1
            flex_content["contents"].append(bubble_content)
        
        return flex_content
