# @Author: PT
# @CreateTime: 2024-06-05
# @Description: 主程序
# @Version:1.0

# 需导入的包
from flask import Flask, request, redirect, render_template, url_for, jsonify, send_file
from kg import*
from mysql_con import Mysql
import time
from werkzeug.utils import secure_filename
import os
from search_prompt import*

# 配置 限定上传文件格式
ALLOWED_EXTENSIONS = set(['csv'])

app=Flask(__name__)
app.secret_key = "secret from"
# 防止中文乱码
app.config['JSON_AS_ASCII'] = False

# 用config设置全局变量，用户名
app.config['username'] = ''
# 设置文件上传保存路径
app.config['UPLOAD_FOLDER'] = 'static/upload_files/'

# 登录注册
@app.route("/", methods=["GET", "POST"])
def get_index():
    if request.method == 'GET':
          username = request.values.get('User', type=str, default=None)
          # 修改全局变量
          app.config['username'] = username
          pwd = request.args.get('Password')
          email = request.args.get('Email')
          # 登录 跳转到图谱展示界面
          if username != None and pwd != None and email == None:
               db = Mysql()
               count = db.get_one_data(username, pwd)
               if count > 0:
                    time.sleep(1.5)
                    return redirect(url_for('display'))
          # 注册
          elif username != None and pwd != None and email != None:
               db = Mysql()
               db.insertdata(username, email, pwd)
    return render_template("login.html")

# 登录注册界面 忘记密码重置密码
@app.route('/getresetdata', methods=["GET", "POST"])
def getresetdata():
     if request.method == 'GET':
          # 接收前端获取输入框内容
          user_input = request.args.get('user_input')
          email_input = request.args.get('email_input')
          new_pwd_input = request.args.get('new_pwd_input')
          confirm_pwd_input = request.args.get('confirm_pwd_input')
          if user_input != None and email_input != None and new_pwd_input != None and confirm_pwd_input != None:
               db = Mysql()
               flag_reset = db.resetpwd(user_input, email_input, new_pwd_input, confirm_pwd_input)
     # 传给前端的数据 flag标志各种情况
     reset_data = {
          'flag_reset': flag_reset
     }
     return jsonify(reset_data)

# 图谱展示
@app.route("/display", methods=["GET", "POST"])
def display(): 
     if request.method == 'GET':
          # 获取搜索框内容
          search = request.values.get('search')
          if(search == None or search == ''):
               neo4j_data = search_all()
          elif(search != None):
               neo4j_data = search_one(search)
     return render_template("display.html", neo4j_data = neo4j_data)

# 中医诊疗
@app.route("/diagnosis", methods=["GET", "POST"])
def diagnosis(): 
     if request.method == 'GET':
          # 为所有图表设置初始值
          # 诊断结果：症状-证素-证的节点、关系
          neo4j_data = {'data_zheng': {'name': '寒淫卫表证', 'category': 0}, 'data_zs': [{'name': '表', 'category': 1}, {'name': '肺', 'category': 1}, {'name': '（外）风', 'category': 1}, {'name': '寒', 'category': 1}, {'name': '痰', 'category': 1}], 'data_zz': [{'name': '鼻塞流清涕', 'category': 2}, {'name': '咳嗽', 'category': 2}, {'name': '头痛', 'category': 2}], 'data_link': [{'source': '鼻塞流清涕', 'value': 11.4, 'target': '表'}, {'source': '咳嗽', 'value': 7.9, 'target': '表'}, {'source': '头痛', 'value': 7.1, 'target': '表'}, {'source': '鼻塞流清涕', 'value': 7.1, 'target': '肺'}, {'source': '咳嗽', 'value': 12.9, 'target': '肺'}, {'source': '鼻塞流清涕', 'value': 10.0, 'target': '（外）风'}, {'source': '头痛', 'value': 7.1, 'target': '（外）风'}, {'source': '鼻塞流清涕', 'value': 9.3, 'target': '寒'}, {'source': '头痛', 'value': 6.4, 'target': '寒'}, {'source': '咳嗽', 'value': 7.1, 'target': '痰'}, {'source': '头痛', 'value': 7.1, 'target': '痰'}, {'source': '寒淫卫表证', 'value': 26.4, 'target': '表'}, {'source': '寒淫卫表证', 'value': 20.0, 'target': '肺'}, {'source': '寒淫卫表证', 'value': 17.1, 'target': '（外）风'}, {'source': '寒淫卫表证', 'value': 15.7, 'target': '寒'}]}        
          neo4j_data = json.dumps(neo4j_data)
          # 症状别名
          zzbm = ['鼻塞流清涕', '咳嗽', '头痛']
          zzbm = json.dumps(zzbm)
          # 证素
          new_zs = ['表', '（外）风', '寒', '肺', '痰', '饮', '阴虚', '心神[脑][心][神]', '肝', '阳亢', '血虚', '火[热]']
          new_zs = json.dumps(new_zs)
          # 症状-证素得分
          l = [[11.4, 7.9, 7.1], [10.0, 0, 7.1], [9.3, 0, 6.4], [7.1, 12.9, 0], [0, 7.1, 7.1], [0, 6.4, 0], [0, 0, 7.1], [0, 0, 7.9], [0, 0, 7.1], [0, 0, 7.1], [0, 0, 6.4], [0, 0, 6.4]]
          l = json.dumps(l)
          # 得分前五证素及得分
          score_sort = {'zs': ['表', '肺', '（外）风', '寒', '痰'], 'score': [26.4, 20.0, 17.1, 15.7, 14.2]}
          score_sort = json.dumps(score_sort)
          # 证-证素-得分
          zh_dict = {'zheng': ['痰火扰心证', '痰热雍肺证', '痰邪阻肺证', '风热犯肺证', '风淫卫表证', '风寒束肺证', '湿淫卫表证', '寒淫卫表证'], 'zs': ['表', '肺', '（外）风', '寒', '痰'], 'score': [[0, 0, 0, 26.4, 26.4, 26.4, 26.4, 26.4], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0, 0, 0, 17.1, 17.1, 17.1, 17.1, 17.1], [0, 0, 15.7, 0, 0, 15.7, 15.7, 15.7], [14.2, 14.2, 14.2, 0, 0, 0, 0, 0]]}
          zh_dict = json.dumps(zh_dict)
          # 诊断结果：证
          zheng_final = '寒淫卫表证'
          # 证-代表方-中药及对应剂量
          zh_dbf_cm = {'dbf': ['黄连温胆汤', '清金化痰汤', '三子养亲汤', '银翘散', '麻黄汤', '金沸草散', '羌活胜湿汤', '桂枝汤'], 'cm_jl': [{'茯苓': 9.0, '生姜': 9.0, '甘草': 3.0, '陈皮': 6.0, '半夏': 9.0, '枳实': 9.0, '竹茹': 9.0, '黄连': 6.0}, {'甘草': 1.2, '瓜蒌仁': 3.0, '知母': 3.0, '桑白皮': 3.0, '茯苓': 9.0, '橘红': 9.0, '贝母': 9.0, '麦门冬': 9.0, '桔梗': 6.0, '栀子': 45.0, '黄芩': 45.0}, {'莱菔子': 9.0, '苏子': 9.0, '白芥子': 6.0}, {'牛蒡子': 18.0, '香豉': 15.0, '荆芥': 12.0, '甘草': 15.0, '竹叶': 12.0, '薄荷': 18.0, '桔梗': 18.0, '银花': 30.0, '连翘': 30.0}, {'甘草': 3.0, '杏仁': 9.0, '桂枝': 4.0, '麻黄': 6.0}, {'旋覆花': 90.0, '甘草': 30.0, '细辛': 30.0, '赤芍': 60.0, '半夏': 30.0, '荆芥': 120.0, '前胡': 90.0}, {'蔓荆子': 2.0, '川芎': 3.0, '甘草': 3.0, '防风': 3.0, '藁本': 3.0, '独活': 6.0, '羌活': 6.0}, {'大枣': 12.0, '生姜': 9.0, '甘草': 6.0, '白芍': 9.0, '桂枝': 9.0}]}
          zh_dbf_cm = json.dumps(zh_dbf_cm)
     return render_template("diagnosis.html", neo4j_data = neo4j_data, zzbm = zzbm, new_zs = new_zs, l = l, score_sort = score_sort, zh_dict = zh_dict, zheng_final = zheng_final, zh_dbf_cm = zh_dbf_cm)

# 症状-症状别名字典
word_list = []
data = pd.read_csv('D:/flask_project/bysj/MMKG/static/symptom_nickname.csv', encoding='UTF-8') 
for i in range(0, len(data)):
     value = data.iloc[i, 0]
     word_list.append(value)
# 构造字典树
sug, data = build_all_trie(word_list)

# 诊疗界面 搜索提示
@app.route("/getkeyword", methods=["GET", "POST"])
def getkeyword():
     if request.method == 'GET':
          # 搜索词
          keyword = request.args.get('keyword')
          # 搜索词
          keyword_result = get_tips_word(sug, data, keyword)
          # 传给前端的数据
          keyword_data = {
               'keyword_result': keyword_result
          }
     return jsonify(keyword_data)

# 诊疗界面 获取数据 传给前端 利用ajax实现异步
@app.route("/getdata", methods=["GET", "POST"])
def getdata():
     if request.method == 'GET':
          # 设置标志，接收前端数据为1则说明已点击
          flag_diagnosis = int(request.args.get('flag', '0'))
          # 接收前端获取的症状搜索框内容
          search = request.args.get('values')
          # 判断是否点击了按钮，且搜索框不为空
          if flag_diagnosis == 1 and search != '':
               neo4j_data, zzbm, new_zs, l, score_sort, zh_dict, zheng_final, zh_dbf_cm= diagnosis_score(search)
          else:
               # 为所有图表设置初始值
               neo4j_data = {'data_zheng': {'name': '寒淫卫表证', 'category': 0}, 'data_zs': [{'name': '表', 'category': 1}, {'name': '肺', 'category': 1}, {'name': '（外）风', 'category': 1}, {'name': '寒', 'category': 1}, {'name': '痰', 'category': 1}], 'data_zz': [{'name': '鼻塞流清涕', 'category': 2}, {'name': '咳嗽', 'category': 2}, {'name': '头痛', 'category': 2}], 'data_link': [{'source': '鼻塞流清涕', 'value': 11.4, 'target': '表'}, {'source': '咳嗽', 'value': 7.9, 'target': '表'}, {'source': '头痛', 'value': 7.1, 'target': '表'}, {'source': '鼻塞流清涕', 'value': 7.1, 'target': '肺'}, {'source': '咳嗽', 'value': 12.9, 'target': '肺'}, {'source': '鼻塞流清涕', 'value': 10.0, 'target': '（外）风'}, {'source': '头痛', 'value': 7.1, 'target': '（外）风'}, {'source': '鼻塞流清涕', 'value': 9.3, 'target': '寒'}, {'source': '头痛', 'value': 6.4, 'target': '寒'}, {'source': '咳嗽', 'value': 7.1, 'target': '痰'}, {'source': '头痛', 'value': 7.1, 'target': '痰'}, {'source': '寒淫卫表证', 'value': 26.4, 'target': '表'}, {'source': '寒淫卫表证', 'value': 20.0, 'target': '肺'}, {'source': '寒淫卫表证', 'value': 17.1, 'target': '（外）风'}, {'source': '寒淫卫表证', 'value': 15.7, 'target': '寒'}]}        
               zzbm = ['鼻塞流清涕', '咳嗽', '头痛']
               new_zs = ['表', '（外）风', '寒', '肺', '痰', '饮', '阴虚', '心神[脑][心][神]', '肝', '阳亢', '血虚', '火[热]']
               l = [[11.4, 7.9, 7.1], [10.0, 0, 7.1], [9.3, 0, 6.4], [7.1, 12.9, 0], [0, 7.1, 7.1], [0, 6.4, 0], [0, 0, 7.1], [0, 0, 7.9], [0, 0, 7.1], [0, 0, 7.1], [0, 0, 6.4], [0, 0, 6.4]]
               score_sort = {'zs': ['表', '肺', '（外）风', '寒', '痰'], 'score': [26.4, 20.0, 17.1, 15.7, 14.2]}
               zh_dict = {'zheng': ['痰火扰心证', '痰热雍肺证', '痰邪阻肺证', '风热犯肺证', '风淫卫表证', '风寒束肺证', '湿淫卫表证', '寒淫卫表证'], 'zs': ['表', '肺', '（外）风', '寒', '痰'], 'score': [[0, 0, 0, 26.4, 26.4, 26.4, 26.4, 26.4], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0, 0, 0, 17.1, 17.1, 17.1, 17.1, 17.1], [0, 0, 15.7, 0, 0, 15.7, 15.7, 15.7], [14.2, 14.2, 14.2, 0, 0, 0, 0, 0]]}
               zheng_final = '寒淫卫表证'
               zh_dbf_cm = {'dbf': ['黄连温胆汤', '清金化痰汤', '三子养亲汤', '银翘散', '麻黄汤', '金沸草散', '羌活胜湿汤', '桂枝汤'], 'cm_jl': [{'茯苓': 9.0, '生姜': 9.0, '甘草': 3.0, '陈皮': 6.0, '半夏': 9.0, '枳实': 9.0, '竹茹': 9.0, '黄连': 6.0}, {'甘草': 1.2, '瓜蒌仁': 3.0, '知母': 3.0, '桑白皮': 3.0, '茯苓': 9.0, '橘红': 9.0, '贝母': 9.0, '麦门冬': 9.0, '桔梗': 6.0, '栀子': 45.0, '黄芩': 45.0}, {'莱菔子': 9.0, '苏子': 9.0, '白芥子': 6.0}, {'牛蒡子': 18.0, '香豉': 15.0, '荆芥': 12.0, '甘草': 15.0, '竹叶': 12.0, '薄荷': 18.0, '桔梗': 18.0, '银花': 30.0, '连翘': 30.0}, {'甘草': 3.0, '杏仁': 9.0, '桂枝': 4.0, '麻黄': 6.0}, {'旋覆花': 90.0, '甘草': 30.0, '细辛': 30.0, '赤芍': 60.0, '半夏': 30.0, '荆芥': 120.0, '前胡': 90.0}, {'蔓荆子': 2.0, '川芎': 3.0, '甘草': 3.0, '防风': 3.0, '藁本': 3.0, '独活': 6.0, '羌活': 6.0}, {'大枣': 12.0, '生姜': 9.0, '甘草': 6.0, '白芍': 9.0, '桂枝': 9.0}]}
           # 设置一个字典，存所有数据，便于前端获取
          content = {
               'neo4j_data': neo4j_data,
               'zzbm': zzbm,
               'new_zs': new_zs,
               'l': l,
               'score_sort': score_sort,
               'zh_dict': zh_dict,
               'zheng_final': zheng_final,
               'zh_dbf_cm': zh_dbf_cm
          }
          # 转成json格式
          return jsonify(content)

# 管理界面 批量增加部分
# 检查函数：使用在上面配置的扩展名来检查文件类型
def allowed_file(filename):
     return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 图谱管理
@app.route("/manage", methods=["GET", "POST"])
def manage():
     if request.method == 'POST':
          # 批量增加部分，上传文件
          file = request.files['file']
          if file and allowed_file(file.filename):
               filename = secure_filename(file.filename)
               file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
     return render_template("manage.html")

# 管理界面 获取数据
@app.route("/getmanage", methods=["GET", "POST"])
def getmanage():
     if request.method == 'GET':
          # 接收前端数据
          flag = int(request.args.get('flag'))
          # eval去掉字符串端点处引号
          select = eval(request.args.get('select'))
          input_content = request.args.get('input_content')
          str = request.args.get('str')
          # flag == 1 即 查节点
          if flag == 1 and input_content != None:
               node_exist = search_node(select, input_content)
               manage_result = node_exist
          # flag == 2 即 改节点
          elif flag == 2 and input_content != None:
               # 由于获取过来的是字符串，先将其转为字典(即去首尾的双引号)
               modify_dict = eval(str)
               # 先判断节点是否存在
               node_exist = search_node(select, input_content)
               if node_exist: 
                    modify_node(select, modify_dict)
                    manage_result = True
               else:
                    manage_result = False
          # flag == 3 即 删节点
          elif flag == 3 and input_content != None:
               # 先判断节点是否存在
               node_exist = search_node(select, input_content)
               if node_exist: 
                    del_node(select, input_content)
                    manage_result = True
               else:
                    manage_result = False
          # flag == 4 即 增单个节点
          elif flag == 4:
               # 将字符串转为字典
               add_dict = eval(str)
               manage_result = add_node(select, add_dict)
          else:
               manage_result = False
          # 传给前端的数据
          manage_data = {
               'manage_result': manage_result
          }
     return jsonify(manage_data)

# 管理界面 修改功能 获取数据传预设值
@app.route("/getmodifydata", methods=["GET", "POST"])
def getmodifydata():
     if request.method == 'GET':
          select = request.args.get('select')
          search_input = request.args.get('search_input')
          if search_input != None and select != '代表方':
               modify_data = search_modify(select, search_input)
          else:
               modify_data = {'flag_modify': 0}
     return jsonify(modify_data)

# 管理界面 下载模板部分
@app.route('/download')
def download():
     # 文件路径和文件名
     file_path = './static/download_templates/templates_csv.zip'
     return send_file(file_path, as_attachment=True)

# 管理界面 上传按钮部分
@app.route('/getbtn', methods=["GET"])
def getbtn():
     # 按钮标志，接收前端数据
     upload_flag = request.args.get('upload_flag')
     if upload_flag == 'cm':
          # 中药表
          adds_cm()
          upload_result = True
     elif upload_flag == 'pcm':
          # 代表方-中药表
          adds_pcm()
          upload_result = True
     elif upload_flag == 'sz':
          # 证表
          adds_zheng()
          upload_result = True
     elif upload_flag == 'sz_zs':
          # 证-证素表
          adds_sz_zs()
          upload_result = True
     elif upload_flag == 'symptom':
          # 症状表
          adds_symptom()
          upload_result = True
     elif upload_flag == 'snn':
          # 症状别名表
          adds_snn()
          upload_result = True
     elif upload_flag == 'zs_s':
          # 证素-症状表
          adds_zs_s()
          upload_result = True
     else:
          upload_result = False
     # 传给前端的数据
     upload_data = {
          'upload_result': upload_result
     }
     return jsonify(upload_data)

# 用户信息修改
@app.route("/user", methods=["GET", "POST"])
def user():   
     return render_template("user.html")

# 用户界面 获取数据
@app.route("/getpwd", methods=["GET", "POST"])
def getpwd():
     if request.method == 'GET':
          # 获取全局变量的值
          username = app.config['username']
          # 设置标志，接收前端数据为1则说明已点击
          flag_pwd = int(request.args.get('flag', '0'))
          # 接收前端获取的输入框内容
          old_pwd = request.args.get('old_pwd')
          new_pwd = request.args.get('new_pwd')
          # 判断旧密码是否输入正确
          if flag_pwd == 1 and old_pwd != None and new_pwd != None:
               db = Mysql()
               count = db.get_one_data(username, old_pwd)
               # 输入正确，且新密码不等于旧密码，则更新，并将标志设为1
               if count > 0:
                    if old_pwd != new_pwd:
                         db.updatedata(username, new_pwd)
                         flag_to_html = '1'
                    else:
                         # 新密码等于旧密码，将标志设为2
                         flag_to_html = '2'
               else:
                    # 输入旧密码错误，将标志设为3
                    flag_to_html = '3'
     return jsonify(flag_to_html)

if __name__=="__main__":
    app.run(debug = True)
