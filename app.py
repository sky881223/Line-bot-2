# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
按鈕樣板TemplateSendMessage
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)



# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('17tIzTTiii6f0/Q64rZZjkT1JMOsOEJslRrtI5IFXqKQ7Y+Y9f+At1VcksSVBMHgqlBpOxEbV34t7M+kccu8j6jrQts+K26HHQRQHq7+10ZQsnFcKFN+1HQsnFcKybFcKFNycFcKFNycFcW1000000000000000')
# 必須放上自己的Channel Secret
handler = WebhookHandler('00c82492ca8937d46ce41ec1db9be34f')

line_bot_api.push_message('U994c9805d94ea22ffd8c30be66e64b0a', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('輸出性別圖',message):
        image_message = ImageSendMessage(
            original_content_url='https://drive.google.com/uc?export=view&id=11-bhcI25JtX4pv3Mn83uMcBko3xwi26O',
            preview_image_url='https://drive.google.com/uc?export=view&id=11-bhcI25JtX4pv3Mn83uMcBko3xwi26O'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif re.match('輸出年齡圖',message):
        image_message = ImageSendMessage(
            original_content_url='https://drive.google.com/uc?export=view&id=11MigttrIPY0WjIhLA4dPdGxeFhJEccUo',
            preview_image_url='https://drive.google.com/uc?export=view&id=11MigttrIPY0WjIhLA4dPdGxeFhJEccUo'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif re.match('輸出臉部配件圖',message):
        image_message = ImageSendMessage(
            original_content_url='https://drive.google.com/uc?export=view&id=11OZvpIaV26YcCjzWeU4BROzKfsMfecOk',
            preview_image_url='https://drive.google.com/uc?export=view&id=11OZvpIaV26YcCjzWeU4BROzKfsMfecOk'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif re.match('輸出頭髮圖',message):
        image_message = ImageSendMessage(
            original_content_url='https://drive.google.com/uc?export=view&id=11O88AFRZ_TLOb4kUijLWIS31PASezswQ',
            preview_image_url='https://drive.google.com/uc?export=view&id=11O88AFRZ_TLOb4kUijLWIS31PASezswQ'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    else:
        buttons_template_message = TemplateSendMessage(
        alt_text='這個看不到',
        template=ButtonsTemplate(
            thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Pie_Chart.PNG/220px-Pie_Chart.PNG',
            title='輸出圖表',
            text='請點選欲輸出圖表',
            actions=[
                MessageAction(
                    label='輸出年齡圖',
                    text='輸出年齡圖'
                ),
                MessageAction(
                    label='輸出性別圖',
                    text='輸出性別圖'
                ),
                MessageAction(
                    label='輸出臉部配件圖',
                    text='輸出臉部配件圖'
                ),
                MessageAction(
                    label='輸出頭髮圖',
                    text='輸出頭髮圖'
                )
            ]
            actions=[
                MessageAction(
                    label='輸出鬍子圖',
                    text='輸出鬍子圖'
                ),
                MessageAction(
                    label='輸出性別圖',
                    text='輸出性別圖'
                ),
                MessageAction(
                    label='輸出臉部配件圖',
                    text='輸出臉部配件圖'
                ),
                MessageAction(
                    label='輸出頭髮圖',
                    text='輸出頭髮圖'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
