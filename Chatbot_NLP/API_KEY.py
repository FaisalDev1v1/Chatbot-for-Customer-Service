import os  # استيراد المكتبة الخاصة بإدارة نظام التشغيل
import openai  # استيراد المكتبة الخاصة ب OpenAI
from dotenv import load_dotenv  # استيراد المكتبة الخاصة بـ dotenv
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']  # استرجاع مفتاح API من المتغيرات البيئية

def get_gpt_reply(prompt,max_tokens=250):  # تعريف الوظيفة التي تحصل على رد من OpenAI GPT-3
    response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',  # تحديد النموذج المستخدم للرد
    messages = [{"role":"user","content":prompt}],  # تحديد النص الذي يتم إرساله كـ prompt
    max_tokens=max_tokens ,  # تحديد الحد الأقصى لعدد الرموز المسموح بها في الرد
  )
    response_message = response.to_dict()['choices'][0]['message']['content']  # استخراج الرسالة الرد من الاستجابة
    return response_message

print(get_gpt_reply("Hello"))  # استدعاء الوظيفة للحصول على رد







































# import os
# import openai
# from dotenv import load_dotenv
# load_dotenv()

# openai.api_key = os.environ['OPENAI_API_KEY'] 



# def get_gpt_reply(prompt,max_tokens=250):
#     response = openai.ChatCompletion.create(
#     model = 'gpt-3.5-turbo',
#     messages = [{"role":"user","content":prompt}],
#     max_tokens=250 , 
#   )
#     response_message = response.to_dict()['choices'][0]['message']['content']
#     return response_message
# print(get_gpt_reply("Hello"))
  



# print(response)



# print(response_message)
