import os  # استيراد المكتبة الخاصة بإدارة نظام التشغيل
import telebot  # استيراد المكتبة الخاصة بـ TeleBot
from API_KEY import get_gpt_reply  # استيراد وظيفة get_gpt_reply من ملف API_KEY

from dotenv import load_dotenv  # استيراد المكتبة الخاصة بـ dotenv
load_dotenv()

BOT_TOKEN = os.environ['BOT_TOKEN']  # استرجاع رمز الوصول للروبوت من المتغيرات البيئية
bot = telebot.TeleBot(BOT_TOKEN)  # إنشاء كائن للروبوت باستخدام رمز الوصول

@bot.message_handler(commands=['start'])  # تعيين معالج لرسائل البدء
def on_start(message):
    chat_id = message.chat.id
    text = 'مرحبا انا خدمة رد آلي لخدمة العملاء \n   كيف يمكنني مساعدتك؟'  # رسالة البدء
    bot.send_message(chat_id, text)  # إرسال الرسالة
    return

@bot.message_handler()  # تعيين معالج لرسائل غير محددة الأوامر
def on_message(message):
    chat_id = message.chat.id
    prompt = message.text[:250]  # استخراج جزء من النص المستلم كـ prompt
    bot.send_chat_action(chat_id, action='typing')  # إرسال إشعار بكتابة
    text = get_gpt_reply(prompt, 1000)  # الحصول على الرد من وظيفة get_gpt_reply
    bot.send_message(chat_id, text)  # إرسال الرسالة
    return

bot.infinity_polling()  # تشغيل الروبوت بشكل مستمر
































# import os
# import telebot
# from API_KEY import get_gpt_reply 

# from dotenv import load_dotenv
# load_dotenv()

# BOT_TOKEN = os.environ['BOT_TOKEN']
# bot = telebot.TeleBot(BOT_TOKEN)

# @bot.message_handler(commands=['start'])
# def on_start(message):
#     chat_id = message.chat.id
#     text = 'مرحبا انا خدمة رد آلي لخدمة العملاء \n   كيف يمكنني مساعدتك؟'
#     bot.send_message(chat_id, text)
#     return
# @bot.message_handler()
# def on_message(message):
#     chat_id = message.chat.id
#     prompt = message.text[:250]
#     bot.send_chat_action(chat_id ,action='typing')
#     text =  get_gpt_reply(prompt , 1000)
#     bot.send_message(chat_id, text)
#     return

# bot.infinity_polling() 


# bot.polling()
