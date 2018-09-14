import random
import pdb
import os

KEY = '150ef53973624108ba1cc46042ea3f85'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : '16209'
    }
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')

@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def tuling_reply(msg):
    reply_list=['四碗粉','智障关爱群']
    if msg.User.NickName in reply_list:
        if msg.isAt:
            if '菜单' in msg['Text']:
                return '生活百科,,,,,数字计算,,,,问答百科,,,,知识库,,,,中英互译,,,,聊天对话,,,休闲娱乐,,,笑话大全,,,,故事大全,,,,成语接龙,,,,新闻资讯,,,,星座运势,,,,脑筋急转弯,,,,歇后语,,,,绕口令,,,,顺口溜,,,,藏头诗,,,,斗图,,,生活服务,,,天气查询,,,,菜谱大全,,,,快递查询,,,,列车查询,,,,日期查询,,,,附近餐厅,,,,附近酒店,,,,实时路况,,,,果蔬报价,,,,汽油报价,,,,股票查询,,,,城市邮编'
            else:
                defaultReply = '我收到了: ' + msg['Text']
                reply = get_response(msg['Text']) #+random.choice(robots)
                print(msg['User']['NickName']+':'+msg['Text']+'==>'+reply)
                return reply
#   robots=['——By王健的zz机器人','——By 66得小麻瓜','——By反正不是本人']

if __name__ == '__main__':
    itchat.auto_login(hotReload=True,enableCmdQR=2)
    itchat.run()
