# @Author: PT
# @CreateTime: 2024-06-05
# @Description:知识图谱 从neo4j中提取数据的函数
# @Version:1.0

# 需导入的包
import json
import pandas as pd
from py2neo import *

# 连接neo4j
# neo4j数据库名称，数据库密码
graph = Graph('http://localhost:7474/', auth=('neo4j6', 'PT_neo4j'))


# 展示各个种类的节点与其关系
def search_all():
    # 节点
    data = [{'id': '103', 'ID': '1', 'name': '新近感受风寒', 'py': 'XJGSFH', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, 
            {'id': '737', 'ID': '1', 'bzm': '新近感受风寒', 'name': '偶感风寒', 'py': 'OGFH', 'category': '症状别名'}, {'id': '738', 'ID': '2', 'bzm': '新近感受风寒', 'name': '感受风寒', 'py': 'GSFH', 'category': '症状别名'}, 
            {'id': '104', 'ID': '2', 'name': '感受暑热火邪', 'py': 'GSSRHX', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, 
            {'id': '105', 'ID': '3', 'name': '环境潮湿', 'py': 'HJCS', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, 
            {'id': '106', 'ID': '4', 'name': '环境干燥', 'py': 'HJGZ', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, 
            {'id': '107', 'ID': '5', 'name': '淋雨下水', 'py': 'LYXS', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, 
            {'id': '739', 'ID': '3', 'bzm': '淋雨下水', 'name': '淋雨', 'py': 'LY', 'category': '症状别名'}, {'id': '740', 'ID': '4', 'bzm': '淋雨下水', 'name': '下水', 'py': 'XS', 'category': '症状别名'}, 
            {'id': '108', 'ID': '6', 'name': '饮食不慎', 'py': 'YSBS', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, 
            {'id': '741', 'ID': '5', 'bzm': '饮食不慎', 'name': '饮食不洁', 'py': 'YSBJ', 'category': '症状别名'}, {'id': '742', 'ID': '6', 'bzm': '饮食不慎', 'name': '饮食过饱', 'py': 'YSGB', 'category': '症状别名'}, 
            {'id': '109', 'ID': '7', 'name': '活动或劳累病重', 'py': 'HDHLLBZ', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, 
            {'id': '743', 'ID': '7', 'bzm': '活动或劳累病重', 'name': '活动后病情加重', 'py': 'HDHBQJZ', 'category': '症状别名'}, {'id': '744', 'ID': '8', 'bzm': '活动或劳累病重', 'name': '疲劳后病情加重', 'py': 'PLHBQJZ', 'category': '症状别名'}, 
            {'id': '745', 'ID': '9', 'bzm': '活动或劳累病重', 'name': '劳累后病情加重', 'py': 'LLHBQJZ', 'category': '症状别名'}, {'id': '110', 'ID': '8', 'name': '病情与情志有关', 'py': 'BQYQZYG', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, 
            {'id': '111', 'ID': '9', 'name': '外伤所致', 'py': 'WSSZ', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, {'id': '112', 'ID': '10', 'name': '新产、流产、手术', 'py': 'XCLCSS', 'zl': '始因等', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, 
            {'id': '746', 'ID': '10', 'bzm': '新产、流产、手术', 'name': '新产', 'py': 'XC', 'category': '症状别名'}, {'id': '747', 'ID': '11', 'bzm': '新产、流产、手术', 'name': '流产', 'py': 'LC', 'category': '症状别名'}, {'id': '748', 'ID': '12', 'bzm': '新产、流产、手术', 'name': '手术', 'py': 'SS', 'category': '症状别名'}, 
            {'id': '921', 'ID': '1', 'name': '始因等', 'py': 'SYD', 'category': '症状种类'}, {'id': '966', 'ID': '26', 'name': '火[热]', 'py': 'HR', 'bw': '否', 'category': '证素'}, {'id': '956', 'ID': '16', 'name': '表', 'py': 'B', 'bw': '是', 'category': '证素'}, 
            {'id': '949', 'ID': '9', 'name': '小肠', 'py': 'XC', 'bw': '是', 'category': '证素'}, {'id': '945', 'ID': '5', 'name': '肝', 'py': 'G', 'bw': '是', 'category': '证素'}, {'id': '973', 'ID': '33', 'name': '气滞', 'py': 'QZ', 'bw': '否', 'category': '证素'}, 
            {'id': '960', 'ID': '20', 'name': '筋骨[关节]', 'py': 'JGGJ', 'bw': '是', 'category': '证素'}, {'id': '962', 'ID': '22', 'name': '寒', 'py': 'H', 'bw': '否', 'category': '证素'}, {'id': '988', 'ID': '48', 'name': '津[液]亏', 'py': 'JYK', 'bw': '否', 'category': '证素'}, 
            {'id': '964', 'ID': '24', 'name': '湿', 'py': 'S', 'bw': '否', 'category': '证素'}, {'id': '978', 'ID': '38', 'name': '气虚', 'py': 'QX', 'bw': '否', 'category': '证素'}, {'id': '29', 'ID': '29', 'name': '饮邪停肺证', 'zl': '基础证', 'zf': '肺系', 'byzs': '肺、饮', 'hyzs': '心、肾、寒、阳虚', 'category': '证'}, 
            {'id': '94', 'ID': '94', 'name': '肝胆湿热证', 'zl': '病位兼证', 'zf': '肝系', 'byzs': '肝、胆、湿、火[热]', 'hyzs': '胃、血瘀', 'category': '证'}, {'id': '54', 'ID': '54', 'name': '脾阳虚证', 'zl': '基础证', 'zf': '脾系', 'byzs': '脾、阳虚', 'hyzs': '寒、湿、气虚', 'category': '证'}, 
            {'id': '42', 'ID': '42', 'name': '痰热雍肺证', 'zl': '病性兼证', 'zf': '肺系', 'byzs': '肺、火[热]、痰', 'hyzs': '（气）闭、脓、阴虚、动风、动血、毒', 'category': '证'}, {'id': '88', 'ID': '88', 'name': '血虚生风证', 'zl': '病性兼证', 'zf': '肝系', 'byzs': '肝、血虚、动风', 'hyzs': '', 'category': '证'}, 
            {'id': '61', 'ID': '61', 'name': '胃寒凝滞证', 'zl': '基础证', 'zf': '脾系', 'byzs': '胃、寒、气滞', 'hyzs': '', 'category': '证'}, {'id': '74', 'ID': '74', 'name': '肝郁气滞证', 'zl': '基础证', 'zf': '肝系', 'byzs': '肝、气滞', 'hyzs': '心神、胆、胞宫', 'category': '证'}, 
            {'id': '84', 'ID': '84', 'name': '肝经湿热证', 'zl': '病性兼证', 'zf': '肝系', 'byzs': '肝、火[热]、湿', 'hyzs': '气滞', 'category': '证'}, {'id': '9', 'ID': '9', 'name': '小肠实热证', 'zl': '基础证', 'zf': '心系', 'byzs': '小肠、火[热]', 'hyzs': '', 'category': '证'}, 
            {'id': '25', 'ID': '25', 'name': '湿淫卫表证', 'zl': '基础证', 'zf': '肺系', 'byzs': '肺、表、湿', 'hyzs': '（外）风、寒', 'category': '证'}, {'id': '1017', 'ID': '24', 'name': '羌活胜湿汤', 'category': '代表方'}, {'id': '1002', 'ID': '9', 'name': '小蓟饮子', 'category': '代表方'}, 
            {'id': '1071', 'ID': '78', 'name': '茵陈五苓散', 'category': '代表方'}, {'id': '1021', 'ID': '28', 'name': '苓甘五味姜辛汤', 'category': '代表方'}, {'id': '1041', 'ID': '48', 'name': '附子理中汤', 'category': '代表方'}, {'id': '1038', 'ID': '45', 'name': '柴胡疏肝散', 'category': '代表方'}, 
            {'id': '1048', 'ID': '55', 'name': '厚朴温中汤', 'category': '代表方'}, {'id': '1066', 'ID': '73', 'name': '四物汤', 'category': '代表方'}, {'id': '1058', 'ID': '65', 'name': '龙胆泻肝汤', 'category': '代表方'}, {'id': '1033', 'ID': '40', 'name': '清金化痰汤', 'category': '代表方'}, 
            {'id': '1096', 'ID': '18', 'name': '羌活', 'xw': '辛、苦、温', 'gj': '膀胱、肾', 'image': 'https://image.zhongyibaike.com/image/%E7%BE%8C%E6%B4%BB/%E7%BE%8C%E6%B4%BB.jpg', 'category': '中药'}, 
            {'id': '1124', 'ID': '46', 'name': '柴胡', 'xw': '辛、苦、微寒', 'gj': '肝、胆、肺', 'image': 'https://image.zhongyibaike.com/image/%E6%9F%B4%E8%83%A1/%E6%9F%B4%E8%83%A1.jpg', 'category': '中药'}, 
            {'id': '1223', 'ID': '145', 'name': '蔓荆子', 'xw': '辛、苦、微寒', 'gj': '膀胱、肝、胃', 'image': 'https://image.zhongyibaike.com/image/%E8%94%93%E8%8D%86%E5%AD%90/%E8%94%93%E8%8D%86%E5%AD%90.jpg', 'category': '中药'}, 
            {'id': '1202', 'ID': '124', 'name': '贝母', 'xw': '苦、甘、微寒', 'gj': '肺、心', 'image': 'https://image.zhongyibaike.com/image/%E5%B7%9D%E8%B4%9D%E6%AF%8D/%E5%B7%9D%E8%B4%9D%E6%AF%8D.jpg', 'category': '中药'}, 
            {'id': '1196', 'ID': '118', 'name': '蒲黄', 'xw': '甘、平', 'gj': '肝、心包', 'image': 'https://image.zhongyibaike.com/image/%E8%92%B2%E9%BB%84/%E7%94%9F%E8%92%B2%E9%BB%84.jpg', 'category': '中药'}, 
            {'id': '1166', 'ID': '88', 'name': '五味子', 'xw': '酸、甘、温', 'gj': '肺、心、肾', 'image': 'https://image.zhongyibaike.com/image/%E4%BA%94%E5%91%B3%E5%AD%90/%E4%BA%94%E5%91%B3%E5%AD%90.jpg', 'category': '中药'}, 
            {'id': '1221', 'ID': '143', 'name': '藕节', 'xw': '甘、涩、平', 'gj': '肝、肺、胃', 'image': 'https://image.zhongyibaike.com/image/%E8%97%95%E8%8A%82/%E8%97%95%E8%8A%82.jpg', 'category': '中药'}, 
            {'id': '1137', 'ID': '59', 'name': '防风', 'xw': '辛、甘、微温', 'gj': '膀胱、肝、脾', 'image': 'https://image.zhongyibaike.com/image/%E9%98%B2%E9%A3%8E/%E9%98%B2%E9%A3%8E1.jpg', 'category': '中药'}, 
            {'id': '1114', 'ID': '36', 'name': '麦门冬', 'xw': '甘、微苦、微寒', 'gj': '心、肺、胃', 'image': 'https://image.zhongyibaike.com/image/%E9%BA%A6%E5%86%AC/%E9%BA%A6%E5%86%AC.jpg', 'category': '中药'}, 
            {'id': '1208', 'ID': '130', 'name': '木通', 'xw': '苦、寒', 'gj': '心、小肠、膀胱', 'image': 'https://image.zhongyibaike.com/image/%E6%9C%A8%E9%80%9A/%E6%9C%A8%E9%80%9A2.jpg', 'category': '中药'}, 
            {'id': '1135', 'ID': '57', 'name': '川芎', 'xw': '辛、温', 'gj': '肝、胆、心包', 'image': 'https://image.zhongyibaike.com/image/%E5%B7%9D%E8%8A%8E/%E5%B7%9D%E8%8A%8E.jpg', 'category': '中药'}, 
            {'id': '1080', 'ID': '2', 'name': '白术', 'xw': '苦、甘、温', 'gj': '脾、胃', 'image': 'https://image.zhongyibaike.com/image/%E7%99%BD%E6%9C%AF/%E7%82%92%E7%99%BD%E6%9C%AF2.jpg', 'category': '中药'}, 
            {'id': '1130', 'ID': '52', 'name': '茵陈', 'xw': '苦、辛、微寒', 'gj': '脾、胃、肝、胆', 'image': 'https://image.zhongyibaike.com/image/%E8%8C%B5%E9%99%88/%E8%8C%B5%E9%99%88.jpg', 'category': '中药'}, 
            {'id': '1116', 'ID': '38', 'name': '厚朴', 'xw': '苦、辛、温', 'gj': '脾、肺、大肠', 'image': 'https://image.zhongyibaike.com/image/%E5%8E%9A%E6%9C%B4/%E5%8E%9A%E6%9C%B4.jpg', 'category': '中药'}, 
            {'id': '1136', 'ID': '58', 'name': '小蓟', 'xw': '甘、苦、凉', 'gj': '心、肝', 'image': 'https://image.zhongyibaike.com/image/%E5%B0%8F%E8%93%9F/%E5%B0%8F%E8%93%9F.jpg', 'category': '中药'}, 
            {'id': '1167', 'ID': '89', 'name': '知母', 'xw': '苦、甘、寒', 'gj': '肺、胃、肾', 'image': 'https://image.zhongyibaike.com/image/%E7%9F%A5%E6%AF%8D/%E7%9F%A5%E6%AF%8D.jpg', 'category': '中药'}, 
            {'id': '1107', 'ID': '29', 'name': '黄芩', 'xw': '苦、寒', 'gj': '肺、胆、脾、大肠、小肠', 'image': 'https://image.zhongyibaike.com/image/%E9%BB%84%E8%8A%A9/%E9%BB%84%E8%8A%A91.jpg', 'category': '中药'}, 
            {'id': '1191', 'ID': '113', 'name': '草豆蔻', 'xw': '辛、温', 'gj': '脾、胃', 'image': 'https://image.zhongyibaike.com/image/%E8%8D%89%E8%B1%86%E8%94%BB/%E8%8D%89%E8%B1%86%E8%94%BB2.jpg', 'category': '中药'}, 
            {'id': '1171', 'ID': '93', 'name': '干姜', 'xw': '辛、热', 'gj': '脾、胃、肾、心、肺', 'image': 'https://image.zhongyibaike.com/image/%E5%B9%B2%E5%A7%9C/%E5%B9%B2%E5%A7%9C.jpg', 'category': '中药'}, 
            {'id': '1110', 'ID': '32', 'name': '陈皮', 'xw': '苦、辛、温', 'gj': '肺、脾', 'image': 'https://image.zhongyibaike.com/image/%E9%99%88%E7%9A%AE/%E9%99%88%E7%9A%AE.jpg', 'category': '中药'}, 
            {'id': '1190', 'ID': '112', 'name': '枳壳', 'xw': '苦、辛、酸、微寒', 'gj': '脾、胃', 'image': 'https://image.zhongyibaike.com/image/%E6%9E%B3%E5%A3%B3/%E6%9E%B3%E5%A3%B31.jpg', 'category': '中药'}, 
            {'id': '1151', 'ID': '73', 'name': '橘红', 'xw': '辛、苦、温', 'gj': '肺、脾', 'image': 'https://image.zhongyibaike.com/image/%E6%A9%98%E7%BA%A2/%E6%A9%98%E7%BA%A2.jpg', 'category': '中药'}, 
            {'id': '1216', 'ID': '138', 'name': '桑白皮', 'xw': '甘、寒', 'gj': '肺', 'image': 'https://image.zhongyibaike.com/image/%E6%A1%91%E7%99%BD%E7%9A%AE/%E6%A1%91%E7%99%BD%E7%9A%AE.jpg', 'category': '中药'}, 
            {'id': '1139', 'ID': '61', 'name': '附子', 'xw': '辛、甘、大热、有毒', 'gj': '心、肾、脾', 'image': 'https://image.zhongyibaike.com/image/%E9%99%84%E5%AD%90/%E9%99%84%E7%89%872.jpg', 'category': '中药'}, 
            {'id': '1087', 'ID': '9', 'name': '生地黄', 'xw': '甘、苦、微寒', 'gj': '心、肝、肾', 'image': 'https://image.zhongyibaike.com/image/%E7%94%9F%E5%9C%B0%E9%BB%84/%E5%B9%B2%E5%9C%B0%E9%BB%84.jpg', 'category': '中药'}, 
            {'id': '1169', 'ID': '91', 'name': '藁本', 'xw': '辛、温', 'gj': '膀胱', 'image': 'https://image.zhongyibaike.com/image/%E8%97%81%E6%9C%AC/%E8%97%81%E6%9C%AC.jpg', 'category': '中药'}, 
            {'id': '1182', 'ID': '104', 'name': '肉桂', 'xw': '辛、甘、大热', 'gj': '肾、脾、辛、肝', 'image': 'https://image.zhongyibaike.com/image/%E8%82%89%E6%A1%82/%E8%82%89%E6%A1%82.jpg', 'category': '中药'}, 
            {'id': '1111', 'ID': '33', 'name': '木香', 'xw': '辛、苦、温', 'gj': '脾、胃、大肠、三焦、胆', 'image': 'https://image.zhongyibaike.com/image/%E6%9C%A8%E9%A6%99/%E6%9C%A8%E9%A6%99.jpg', 'category': '中药'}, 
            {'id': '1258', 'ID': '180', 'name': '猪苓', 'xw': '甘、平', 'gj': '脾、肾、肺、膀胱', 'image': 'https://image.zhongyibaike.com/image/%E7%8C%AA%E8%8B%93/%E7%8C%AA%E8%8B%932.jpg', 'category': '中药'}, 
            {'id': '1120', 'ID': '42', 'name': '滑石', 'xw': '甘、淡、寒', 'gj': '膀胱、肺、胃', 'image': 'https://image.zhongyibaike.com/image/%E6%BB%91%E7%9F%B3/%E6%BB%91%E7%9F%B3%E7%B2%891.jpg', 'category': '中药'}, 
            {'id': '1094', 'ID': '16', 'name': '茯苓', 'xw': '甘、淡、平', 'gj': '心、肺、脾、肾', 'image': 'https://image.zhongyibaike.com/image/%E8%8C%AF%E8%8B%93/%E8%8C%AF%E8%8B%931.jpg', 'category': '中药'}, 
            {'id': '1140', 'ID': '62', 'name': '独活', 'xw': '辛、苦、微温', 'gj': '肾、膀胱', 'image': 'https://image.zhongyibaike.com/image/%E7%8B%AC%E6%B4%BB/%E7%8B%AC%E6%B4%BB.jpg', 'category': '中药'}, 
            {'id': '1148', 'ID': '70', 'name': '栀子', 'xw': '苦、寒', 'gj': '心、肺、三焦', 'image': 'https://image.zhongyibaike.com/image/%E6%A0%80%E5%AD%90/%E7%94%9F%E6%A0%80%E5%AD%90.jpg', 'category': '中药'}, 
            {'id': '1145', 'ID': '67', 'name': '细辛', 'xw': '辛、温', 'gj': '心、肺、肾', 'image': 'https://image.zhongyibaike.com/image/%E7%BB%86%E8%BE%9B/%E7%BB%86%E8%BE%9B2.jpg', 'category': '中药'}, 
            {'id': '1165', 'ID': '87', 'name': '桔梗', 'xw': '苦、辛、平', 'gj': '肺', 'image': 'https://image.zhongyibaike.com/image/%E6%A1%94%E6%A2%97/%E6%A1%94%E6%A2%97.jpg', 'category': '中药'}, 
            {'id': '1093', 'ID': '15', 'name': '熟地黄', 'xw': '甘、微温', 'gj': '肝、肾', 'image': 'https://image.zhongyibaike.com/image/%E7%86%9F%E5%9C%B0%E9%BB%84/%E7%86%9F%E5%9C%B0%E9%BB%84.jpg', 'category': '中药'}, 
            {'id': '1195', 'ID': '117', 'name': '车前子', 'xw': '甘、寒', 'gj': '肝、肾、肺、小肠', 'image': 'https://image.zhongyibaike.com/image/%E8%BD%A6%E5%89%8D%E5%AD%90/%E8%BD%A6%E5%89%8D%E5%AD%90.jpg', 'category': '中药'}, 
            {'id': '1134', 'ID': '56', 'name': '甘草', 'xw': '甘、平', 'gj': '心、肺、脾、胃', 'image': 'https://image.zhongyibaike.com/image/%E7%94%98%E8%8D%89/%E7%94%9F%E7%94%98%E8%8D%891.jpg', 'category': '中药'}, 
            {'id': '1083', 'ID': '5', 'name': '当归', 'xw': '甘、辛、温', 'gj': '肝、心、脾', 'image': 'https://image.zhongyibaike.com/image/%E5%BD%93%E5%BD%92/%E5%BD%93%E5%BD%92.jpg', 'category': '中药'}, 
            {'id': '1158', 'ID': '80', 'name': '泽泻', 'xw': '甘、淡、寒', 'gj': '肾、膀胱', 'image': 'https://image.zhongyibaike.com/image/%E6%B3%BD%E6%B3%BB/%E6%B3%BD%E6%B3%BB2.jpg', 'category': '中药'}, 
            {'id': '1200', 'ID': '122', 'name': '竹叶', 'xw': '甘、淡、寒', 'gj': '心、肺、胆、胃', 'image': 'https://image.zhongyibaike.com/image/%E6%B7%A1%E7%AB%B9%E5%8F%B6/%E6%B7%A1%E7%AB%B9%E5%8F%B62.jpg', 'category': '中药'}, 
            {'id': '1081', 'ID': '3', 'name': '人参', 'xw': '甘、微苦、微温', 'gj': '脾、肺、心、肾', 'image': 'https://image.zhongyibaike.com/image/%E4%BA%BA%E5%8F%82/%E4%BA%BA%E5%8F%82.jpg', 'category': '中药'}, 
            {'id': '1112', 'ID': '34', 'name': '香附', 'xw': '辛、微苦、微甘、平', 'gj': '肝、脾、三焦', 'image': 'https://image.zhongyibaike.com/image/%E9%A6%99%E9%99%84/%E9%A6%99%E9%99%84.jpg', 'category': '中药'}, 
            {'id': '1122', 'ID': '44', 'name': '龙胆', 'xw': '苦、寒', 'gj': '肝、胆', 'image': 'https://image.zhongyibaike.com/image/%E9%BE%99%E8%83%86%E8%8D%89/%E9%BE%99%E8%83%86%E8%8D%891.jpg', 'category': '中药'}, 
            {'id': '1248', 'ID': '170', 'name': '瓜蒌仁', 'xw': '甘、寒', 'gj': '肺、胃、大肠', 'image': 'https://image.zhongyibaike.com/image/%E7%93%9C%E8%92%8C%E5%AD%90/%E7%93%9C%E8%92%8C%E5%AD%90.jpg', 'category': '中药'}, 
            {'id': '1179', 'ID': '101', 'name': '通草', 'xw': '甘、淡、微寒', 'gj': '肺、胃', 'image': 'https://image.zhongyibaike.com/image/%E9%80%9A%E8%8D%89/%E9%80%9A%E8%8D%892.jpg', 'category': '中药'}, 
            {'id': '1108', 'ID': '30', 'name': '白芍', 'xw': '苦、酸、微寒', 'gj': '肝、脾', 'image': 'https://image.zhongyibaike.com/image/%E7%99%BD%E8%8A%8D/%E7%94%9F-%E7%99%BD-%E8%8A%8D.jpg', 'category': '中药'},
            {'id': '667', 'ID': '583', 'name': '舌淡', 'py': 'SD', 'zl': '舌象', 'image': 'https://i.postimg.cc/jS26zqcQ/2-1.jpg', 'category': '症状'}, {'id': '938', 'ID': '18', 'name': '舌象', 'py': 'SX', 'category': '症状种类'},
            {'id': '316', 'ID': '219', 'name': '咳嗽', 'py': 'KS', 'zl': '咳痰喘', 'image': 'https://i.postimg.cc/tJHJ4kSm/image.webp', 'category': '症状'}, {'id': '928', 'ID': '8', 'name': '咳痰喘', 'py': 'KTC', 'category': '症状种类'},
            {'id': '691', 'ID': '607', 'name': '舌苔薄白', 'py': 'STBB', 'zl': '舌象', 'image': 'https://i.postimg.cc/9QP4R65t/26.jpg', 'category': '症状'}, 
            {'id': '681', 'ID': '597', 'name': '舌边齿印', 'py': 'SBCY', 'zl': '舌象', 'image': 'https://i.postimg.cc/ZKKsMSj0/16.jpg', 'category': '症状'},
            {'id': '684', 'ID': '600', 'name': '舌动异常', 'py': 'SDYC', 'zl': '舌象', 'image': 'https://i.postimg.cc/cC1h2RRP/19.jpg', 'category': '症状'}]    
    # 关系
    links = [{'source': '103', 'target': '737', 'name': '别名'}, {'source': '103', 'target': '738', 'name': '别名'}, {'source': '107', 'target': '739', 'name': '别名'}, {'source': '107', 'target': '740', 'name': '别名'}, 
             {'source': '108', 'target': '741', 'name': '别名'}, {'source': '108', 'target': '742', 'name': '别名'}, {'source': '109', 'target': '743', 'name': '别名'}, {'source': '109', 'target': '744', 'name': '别名'}, 
             {'source': '109', 'target': '745', 'name': '别名'}, {'source': '112', 'target': '746', 'name': '别名'}, {'source': '112', 'target': '747', 'name': '别名'}, {'source': '112', 'target': '748', 'name': '别名'}, 
             {'source': '103', 'target': '921', 'name': '种类'}, {'source': '104', 'target': '921', 'name': '种类'}, {'source': '105', 'target': '921', 'name': '种类'}, {'source': '106', 'target': '921', 'name': '种类'}, 
             {'source': '107', 'target': '921', 'name': '种类'}, {'source': '108', 'target': '921', 'name': '种类'}, {'source': '109', 'target': '921', 'name': '种类'}, {'source': '110', 'target': '921', 'name': '种类'}, 
             {'source': '111', 'target': '921', 'name': '种类'}, {'source': '112', 'target': '921', 'name': '种类'}, {'source': '103', 'target': '956', 'name': '辨识', 'score': '8.6'}, {'source': '103', 'target': '962', 'name': '辨识', 'score': '8.6'}, 
             {'source': '104', 'target': '966', 'name': '辨识', 'score': '8.6'}, {'source': '104', 'target': '964', 'name': '辨识', 'score': '7.9'}, {'source': '105', 'target': '956', 'name': '辨识', 'score': '7.9'}, {'source': '105', 'target': '973', 'name': '辨识', 'score': '7.1'}, 
             {'source': '105', 'target': '960', 'name': '辨识', 'score': '7.9'}, {'source': '105', 'target': '964', 'name': '辨识', 'score': '11.4'}, {'source': '106', 'target': '956', 'name': '辨识', 'score': '7.9'}, {'source': '106', 'target': '988', 'name': '辨识', 'score': '8.6'}, 
             {'source': '106', 'target': '964', 'name': '辨识', 'score': '2.9'}, {'source': '107', 'target': '956', 'name': '辨识', 'score': '8.6'}, {'source': '107', 'target': '960', 'name': '辨识', 'score': '7.9'}, {'source': '107', 'target': '962', 'name': '辨识', 'score': '8.6'}, 
             {'source': '107', 'target': '964', 'name': '辨识', 'score': '7.9'}, {'source': '108', 'target': '949', 'name': '辨识', 'score': '8.6'}, {'source': '108', 'target': '973', 'name': '辨识', 'score': '7.9'}, {'source': '109', 'target': '978', 'name': '辨识', 'score': '8.6'}, 
             {'source': '110', 'target': '945', 'name': '辨识', 'score': '11.4'}, {'source': '110', 'target': '973', 'name': '辨识', 'score': '11.4'}, {'source': '111', 'target': '973', 'name': '辨识', 'score': '7.1'}, {'source': '112', 'target': '973', 'name': '辨识', 'score': '7.1'}, 
             {'source': '112', 'target': '978', 'name': '辨识', 'score': '7.1'}, {'source': '29', 'target': '962', 'name': '或有'}, {'source': '94', 'target': '966', 'name': '必有'}, {'source': '94', 'target': '945', 'name': '必有'}, {'source': '94', 'target': '964', 'name': '必有'}, 
             {'source': '54', 'target': '962', 'name': '或有'}, {'source': '54', 'target': '964', 'name': '或有'}, {'source': '54', 'target': '978', 'name': '或有'}, {'source': '42', 'target': '966', 'name': '必有'}, {'source': '88', 'target': '945', 'name': '必有'}, 
             {'source': '61', 'target': '973', 'name': '必有'}, {'source': '61', 'target': '962', 'name': '必有'}, {'source': '74', 'target': '945', 'name': '必有'}, {'source': '74', 'target': '973', 'name': '必有'}, {'source': '84', 'target': '966', 'name': '必有'}, 
             {'source': '84', 'target': '945', 'name': '必有'}, {'source': '84', 'target': '973', 'name': '或有'}, {'source': '84', 'target': '964', 'name': '必有'}, {'source': '9', 'target': '966', 'name': '必有'}, {'source': '9', 'target': '949', 'name': '必有'}, 
             {'source': '25', 'target': '956', 'name': '必有'}, {'source': '25', 'target': '962', 'name': '或有'}, {'source': '25', 'target': '964', 'name': '必有'}, {'source': '29', 'target': '1021', 'name': '治疗方剂'}, {'source': '94', 'target': '1071', 'name': '治疗方剂'}, 
             {'source': '54', 'target': '1041', 'name': '治疗方剂'}, {'source': '42', 'target': '1033', 'name': '治疗方剂'}, {'source': '88', 'target': '1066', 'name': '治疗方剂'}, {'source': '61', 'target': '1048', 'name': '治疗方剂'}, {'source': '74', 'target': '1038', 'name': '治疗方剂'}, 
             {'source': '84', 'target': '1058', 'name': '治疗方剂'}, {'source': '9', 'target': '1002', 'name': '治疗方剂'}, {'source': '25', 'target': '1017', 'name': '治疗方剂'},  
             {'source': '1017', 'target': '1096', 'name': '药物组成', 'jl': '6'}, {'source': '1017', 'target': '1223', 'name': '药物组成', 'jl': '2'}, {'source': '1017', 'target': '1137', 'name': '药物组成', 'jl': '3'}, {'source': '1017', 'target': '1135', 'name': '药物组成', 'jl': '3'}, 
             {'source': '1017', 'target': '1169', 'name': '药物组成', 'jl': '3'}, {'source': '1017', 'target': '1140', 'name': '药物组成', 'jl': '6'}, {'source': '1017', 'target': '1134', 'name': '药物组成', 'jl': '3'}, {'source': '1002', 'target': '1196', 'name': '药物组成', 'jl': '15'}, 
             {'source': '1002', 'target': '1221', 'name': '药物组成', 'jl': '15'}, {'source': '1002', 'target': '1136', 'name': '药物组成', 'jl': '15'}, {'source': '1002', 'target': '1087', 'name': '药物组成', 'jl': '120'}, {'source': '1002', 'target': '1120', 'name': '药物组成', 'jl': '15'}, 
             {'source': '1002', 'target': '1148', 'name': '药物组成', 'jl': '15'}, {'source': '1002', 'target': '1134', 'name': '药物组成', 'jl': '15'}, {'source': '1002', 'target': '1083', 'name': '药物组成', 'jl': '15'}, {'source': '1002', 'target': '1200', 'name': '药物组成', 'jl': '15'}, 
             {'source': '1002', 'target': '1179', 'name': '药物组成', 'jl': '15'}, {'source': '1071', 'target': '1080', 'name': '药物组成', 'jl': '9'}, {'source': '1071', 'target': '1130', 'name': '药物组成', 'jl': '160'}, {'source': '1071', 'target': '1182', 'name': '药物组成', 'jl': '6'}, 
             {'source': '1071', 'target': '1258', 'name': '药物组成', 'jl': '9'}, {'source': '1071', 'target': '1094', 'name': '药物组成', 'jl': '9'}, {'source': '1071', 'target': '1158', 'name': '药物组成', 'jl': '30'}, {'source': '1021', 'target': '1166', 'name': '药物组成', 'jl': '6'}, 
             {'source': '1021', 'target': '1171', 'name': '药物组成', 'jl': '9'}, {'source': '1021', 'target': '1094', 'name': '药物组成', 'jl': '12'}, {'source': '1021', 'target': '1145', 'name': '药物组成', 'jl': '3'}, {'source': '1021', 'target': '1134', 'name': '药物组成', 'jl': '6'}, 
             {'source': '1041', 'target': '1080', 'name': '药物组成', 'jl': '6'}, {'source': '1041', 'target': '1171', 'name': '药物组成', 'jl': '6'}, {'source': '1041', 'target': '1139', 'name': '药物组成', 'jl': '6'}, {'source': '1041', 'target': '1134', 'name': '药物组成', 'jl': '3'}, 
             {'source': '1041', 'target': '1081', 'name': '药物组成', 'jl': '6'}, {'source': '1038', 'target': '1124', 'name': '药物组成', 'jl': '6'}, {'source': '1038', 'target': '1135', 'name': '药物组成', 'jl': '4.5'}, {'source': '1038', 'target': '1110', 'name': '药物组成', 'jl': '6'}, 
             {'source': '1038', 'target': '1190', 'name': '药物组成', 'jl': '4.5'}, {'source': '1038', 'target': '1134', 'name': '药物组成', 'jl': '1.5'}, {'source': '1038', 'target': '1112', 'name': '药物组成', 'jl': '4.5'}, {'source': '1038', 'target': '1108', 'name': '药物组成', 'jl': '4.5'}, 
             {'source': '1048', 'target': '1116', 'name': '药物组成', 'jl': '30'}, {'source': '1048', 'target': '1191', 'name': '药物组成', 'jl': '15'}, {'source': '1048', 'target': '1171', 'name': '药物组成', 'jl': '2.1'}, {'source': '1048', 'target': '1110', 'name': '药物组成', 'jl': '30'}, 
             {'source': '1048', 'target': '1111', 'name': '药物组成', 'jl': '15'}, {'source': '1048', 'target': '1094', 'name': '药物组成', 'jl': '15'}, {'source': '1048', 'target': '1134', 'name': '药物组成', 'jl': '15'}, {'source': '1066', 'target': '1135', 'name': '药物组成', 'jl': '9'}, 
             {'source': '1066', 'target': '1093', 'name': '药物组成', 'jl': '9'}, {'source': '1066', 'target': '1083', 'name': '药物组成', 'jl': '9'}, {'source': '1066', 'target': '1108', 'name': '药物组成', 'jl': '9'}, {'source': '1058', 'target': '1124', 'name': '药物组成', 'jl': '6'}, 
             {'source': '1058', 'target': '1208', 'name': '药物组成', 'jl': '6'}, {'source': '1058', 'target': '1107', 'name': '药物组成', 'jl': '9'}, {'source': '1058', 'target': '1087', 'name': '药物组成', 'jl': '9'}, {'source': '1058', 'target': '1148', 'name': '药物组成', 'jl': '9'}, 
             {'source': '1058', 'target': '1195', 'name': '药物组成', 'jl': '9'}, {'source': '1058', 'target': '1134', 'name': '药物组成', 'jl': '6'}, {'source': '1058', 'target': '1083', 'name': '药物组成', 'jl': '3'}, {'source': '1058', 'target': '1158', 'name': '药物组成', 'jl': '12'}, 
             {'source': '1058', 'target': '1122', 'name': '药物组成', 'jl': '6'}, {'source': '1033', 'target': '1202', 'name': '药物组成', 'jl': '9'}, {'source': '1033', 'target': '1114', 'name': '药物组成', 'jl': '9'}, {'source': '1033', 'target': '1167', 'name': '药物组成', 'jl': '3'}, 
             {'source': '1033', 'target': '1107', 'name': '药物组成', 'jl': '45'}, {'source': '1033', 'target': '1151', 'name': '药物组成', 'jl': '9'}, {'source': '1033', 'target': '1216', 'name': '药物组成', 'jl': '3'}, {'source': '1033', 'target': '1094', 'name': '药物组成', 'jl': '9'}, 
             {'source': '1033', 'target': '1148', 'name': '药物组成', 'jl': '45'}, {'source': '1033', 'target': '1165', 'name': '药物组成', 'jl': '6'}, {'source': '1033', 'target': '1134', 'name': '药物组成', 'jl': '1.2'}, {'source': '1033', 'target': '1248', 'name': '药物组成', 'jl': '3'},
             {'source': '667', 'target': '938', 'name': '种类'}, {'source': '316', 'target': '928', 'name': '种类'}, {'source': '691', 'target': '938', 'name': '种类'}, {'source': '681', 'target': '938', 'name': '种类'}, {'source': '667', 'target': '966', 'name': '辨识', 'score': '2.9'},
             {'source': '667', 'target': '978', 'name': '辨识', 'score': '7.9'}, {'source': '316', 'target': '956', 'name': '辨识', 'score': '7.9'}, {'source': '691', 'target': '956', 'name': '辨识', 'score': '7.9'}, {'source': '681', 'target': '978', 'name': '辨识', 'score': '7.1'}, 
             {'source': '681', 'target': '964', 'name': '辨识', 'score': '7.9'}, {'source': '684', 'target': '945', 'name': '辨识', 'score': '8.6'}, {'source': '684', 'target': '938', 'name': '种类'}]    
    
    # 将所有的节点信息和关系信息存放在一个字典中
    neo4j_data = {
        'data': data,
        'links': links
    }
    # 转换成json格式
    neo4j_data = json.dumps(neo4j_data)
    return neo4j_data


# 取预设值函数
def pre_nodes():
    # 定义data数组存储节点信息
    data = []
    # 定义link数组存储节点关系
    link = []
    # 设一个列表存症状
    zz_all = []
    # 设一个列表存症状种类
    zl_all = []
    # 设一个列表存证素
    zs_all = []
    # 取多个节点
    data1 = graph.run("MATCH(n:`症状`) RETURN n limit 10").data()
    # 取特定的单个节点
    # data1 = graph.run('MATCH(n:`症状`{`标准名`:"舌动异常"}) RETURN n').data()
    for n in data1:
        n = n['n']
        # 将节点信息转化为json格式，否则中文会不显示
        nodesStr = json.dumps(n, ensure_ascii=False)
        # 取出节点的属性
        node_id = json.loads(nodesStr)['id']
        node_ID = json.loads(nodesStr)['ID']
        node_bzm = json.loads(nodesStr)['标准名']
        node_py = json.loads(nodesStr)['拼音']
        node_zl = json.loads(nodesStr)['种类']
        node_image = json.loads(nodesStr)['image']
        zz_all.append(node_bzm)

        # 构造字典，存储单个节点信息
        data1_dict = {
            'id': node_id,
            'ID': node_ID,
            'name': node_bzm,
            'py': node_py,
            'zl': node_zl,
            'image': node_image,
            'category': '症状'
        }
        # 将单个节点信息存放在data数组中
        data.append(data1_dict)

        # 关系：症状->症状别名
        rel1 = graph.run('MATCH(n:`症状`{`标准名`:"' + node_bzm + '"})<-[rel]->(m:`症状别名`) return rel, m').data()
        for r in rel1:
            # 提取相应 症状别名 实体
            m = r['m']
            nodesStr = json.dumps(m, ensure_ascii=False)
            node_id = json.loads(nodesStr)['id']
            node_ID = json.loads(nodesStr)['ID']
            node_bzm = json.loads(nodesStr)['别名的标准名']
            node_name = json.loads(nodesStr)['标准名']
            node_py = json.loads(nodesStr)['拼音']

            data2_dict = {
                'id': node_id,
                'ID': node_ID,
                'bzm': node_bzm,
                'name': node_name,
                'py': node_py,
                'category': '症状别名'
            }
            data.append(data2_dict)

            # 提取相应关系 别名
            source = str(r['rel'].start_node['id'])
            target = str(r['rel'].end_node['id'])
            name = str(type(r['rel']).__name__)
            rel1_dict = {
                'source': source,
                'target': target,
                'name': name
            }
            link.append(rel1_dict)
        
        # 症状->症状种类
        rel2 = graph.run('MATCH(n:`症状`{`标准名`:"' + node_bzm + '"})<-[rel]->(m:`症状种类`) return rel, m').data()
        for r in rel2:
            # 提取相应 症状种类 实体
            m = r['m']
            nodesStr = json.dumps(m, ensure_ascii=False)
            node_name = json.loads(nodesStr)['标准名']
            zl_all.append(node_name)
        
        # 症状->证素
        rel3 = graph.run('MATCH(n:`症状`{`标准名`:"' + node_bzm + '"})<-[rel]->(m:`证素`) return rel, m').data()
        for r in rel3:
            # 提取相应 证素 实体
            m = r['m']
            nodesStr = json.dumps(m, ensure_ascii=False)
            node_name = json.loads(nodesStr)['标准名']
            zs_all.append(node_name)

    # 对症状种类合集去重
    zl_all = list(set(zl_all))

    # 实体：症状种类
    for zl_bzm in zl_all:
        data3 = graph.run('MATCH (m:`症状种类`{`标准名`:"' + zl_bzm + '"}) RETURN m').data()
        for k in data3:
            # 提取相应 症状种类 实体
            m = k['m']
            nodesStr = json.dumps(m, ensure_ascii=False)
            node_id = json.loads(nodesStr)['id']
            node_ID = json.loads(nodesStr)['ID']
            node_name = json.loads(nodesStr)['标准名']
            node_py = json.loads(nodesStr)['拼音']

            data3_dict = {
                'id': node_id,
                'ID': node_ID,
                'name': node_name,
                'py': node_py,
                'category': '症状种类'
            }
            data.append(data3_dict)
    
    # 关系：症状->症状种类
    for zz_bzm in zz_all:
        for zl_bzm in zl_all:
            rel2 = graph.run('MATCH(n:`症状`{`标准名`:"' + zz_bzm + '"})<-[rel]->(m:`症状种类`{`标准名`:"' + zl_bzm + '"}) return rel').data()
            if rel2 != []:
                for r in rel2:
                    # 提取相应关系 种类
                    source = str(r['rel'].start_node['id'])
                    target = str(r['rel'].end_node['id'])
                    name = str(type(r['rel']).__name__)
                    rel2_dict = {
                        'source': source,
                        'target': target,
                        'name': name
                    }
                    link.append(rel2_dict)
    
    # 对证素合集去重
    zs_all = list(set(zs_all))
    # 取前10证素
    zs_10 = zs_all[:10]

    # 实体：证素
    for zs_bzm in zs_10:
        data4 = graph.run('MATCH (m:`证素`{`标准名`:"' + zs_bzm + '"}) RETURN m').data()
        for k in data4:
            # 提取相应 证素 实体
            m = k['m']
            nodesStr = json.dumps(m, ensure_ascii=False)
            node_id = json.loads(nodesStr)['id']
            node_ID = json.loads(nodesStr)['ID']
            node_name = json.loads(nodesStr)['标准名']
            node_py = json.loads(nodesStr)['拼音']
            node_bw = json.loads(nodesStr)['病位']

            data4_dict = {
                'id': node_id,
                'ID': node_ID,
                'name': node_name,
                'py': node_py,
                'bw': node_bw,
                'category': '证素'
            }
            data.append(data4_dict)
    
    # 关系：症状->证素
    for zz_bzm in zz_all:
        for zs_bzm in zs_10:
            rel3 = graph.run('MATCH(n:`症状`{`标准名`:"' + zz_bzm + '"})<-[rel]->(m:`证素`{`标准名`:"' + zs_bzm + '"}) return rel').data()
            if rel3 != []:
                for r in rel3:
                    # 提取相应关系 种类
                    source = str(r['rel'].start_node['id'])
                    target = str(r['rel'].end_node['id'])
                    name = str(type(r['rel']).__name__)
                    score = r['rel']['得分']
                    rel3_dict = {
                        'source': source,
                        'target': target,
                        'name': name,
                        'score': score
                    }
                    link.append(rel3_dict)
    
    # 设一个列表存证
    zheng_all = []
    for zs_bzm in zs_10:
        # 证->证素
        rel4 = graph.run('MATCH(n:`证`)<-[rel]->(m:`证素`{`标准名`:"' + zs_bzm + '"}) return rel, n').data()
        for r in rel4:
            # 提取相应 证 实体
            n = r['n']
            nodesStr = json.dumps(n, ensure_ascii=False)
            node_name = json.loads(nodesStr)['标准名']
            zheng_all.append(node_name)   

    # 对证名合集去重
    zheng_all = list(set(zheng_all))
    # 取前10证
    zheng_10 = zheng_all[:10]

    # 实体：证
    for zheng_bzm in zheng_10:
        data5 = graph.run('MATCH (n:`证`{`标准名`:"' + zheng_bzm + '"}) RETURN n').data()
        for k in data5:
            # 提取相应 证 实体
            n = k['n']
            nodesStr = json.dumps(n, ensure_ascii=False)
            node_id = json.loads(nodesStr)['id']
            node_ID = json.loads(nodesStr)['ID']
            node_name = json.loads(nodesStr)['标准名']
            node_zl = json.loads(nodesStr)['种类']
            node_zf = json.loads(nodesStr)['脏腑']
            node_byzs = json.loads(nodesStr)['必有证素']
            temp = json.loads(nodesStr)
            if '或有证素' in temp:
                node_hyzs = json.loads(nodesStr)['或有证素']
            else:
                node_hyzs = ''

            data5_dict = {
                'id': node_id,
                'ID': node_ID,
                'name': node_name,
                'zl': node_zl,
                'zf': node_zf,
                'byzs': node_byzs,
                'hyzs': node_hyzs,
                'category': '证'
            }
            data.append(data5_dict)
    
    # 关系：证->证素
    for zheng_bzm in zheng_10:
        for zs_bzm in zs_10:
            rel4 = graph.run('MATCH(n:`证`{`标准名`:"' + zheng_bzm + '"})<-[rel]->(m:`证素`{`标准名`:"' + zs_bzm + '"}) return rel').data()
            if rel4 != []:
                for r in rel4:
                    # 提取相应关系 必有 或有
                    source = str(r['rel'].start_node['id'])
                    target = str(r['rel'].end_node['id'])
                    name = str(type(r['rel']).__name__)
                    rel4_dict = {
                        'source': source,
                        'target': target,
                        'name': name
                    }
                    link.append(rel4_dict)
        
    # 设一个列表存代表方
    dbf_all = []
    # 证->代表方
    for zheng_bzm in zheng_10:
        rel5 = graph.run('MATCH(n:`证`{`标准名`:"' + zheng_bzm + '"})<-[rel]->(m:`代表方`) return rel, m').data()
        for r in rel5:
            # 提取相应 代表方 实体
            m = r['m']
            nodesStr = json.dumps(m, ensure_ascii=False)
            node_name = json.loads(nodesStr)['代表方']
            dbf_all.append(node_name)
    
    # 对代表方合集去重
    dbf_all = list(set(dbf_all))
    print(dbf_all)

    # 实体：代表方
    for dbf_bzm in dbf_all:
        data6 = graph.run('MATCH (m:`代表方`{`代表方`:"' + dbf_bzm + '"}) RETURN m').data()
        for k in data6:
            # 提取相应 代表方 实体
            m = k['m']
            nodesStr = json.dumps(m, ensure_ascii=False)
            node_id = json.loads(nodesStr)['id']
            node_ID = json.loads(nodesStr)['ID']
            node_name = json.loads(nodesStr)['代表方']

            data6_dict = {
                'id': node_id,
                'ID': node_ID,
                'name': node_name,
                'category': '代表方'
            }
            data.append(data6_dict)
    
    # 关系：证->代表方
    for zheng_bzm in zheng_10:
        for dbf_bzm in dbf_all:
            rel5 = graph.run('MATCH(n:`证`{`标准名`:"' + zheng_bzm + '"})<-[rel]->(m:`代表方`{`代表方`:"' + dbf_bzm + '"}) return rel').data()
            if rel5 != []:
                for r in rel5:
                    # 提取相应关系 治疗方剂
                    source = str(r['rel'].start_node['id'])
                    target = str(r['rel'].end_node['id'])
                    name = str(type(r['rel']).__name__)
                    rel5_dict = {
                        'source': source,
                        'target': target,
                        'name': name
                    }
                    link.append(rel5_dict)

    # 设一个列表存中药
    cm_all = []
    # 代表方->中药
    for dbf_bzm in dbf_all:
        rel6 = graph.run('MATCH(n:`代表方`{`代表方`:"' + dbf_bzm + '"})<-[rel]->(m:`中药`) return rel, m').data()
        for r in rel6:
            # 提取相应 中药 实体
            m = r['m']
            nodesStr = json.dumps(m, ensure_ascii=False)
            node_name = json.loads(nodesStr)['中药名']
            cm_all.append(node_name)

    # 对中药合集去重
    cm_all = list(set(cm_all))
    # 取前10中药
    # cm_10 = cm_all[:10]

    # 实体：中药
    for cm_bzm in cm_all:
        data7 = graph.run('MATCH (m:`中药`{`中药名`:"' + cm_bzm + '"}) RETURN m').data()
        for k in data7:
            # 提取相应 中药 实体
            m = k['m']
            nodesStr = json.dumps(m, ensure_ascii=False)
            node_id = json.loads(nodesStr)['id']
            node_ID = json.loads(nodesStr)['ID']
            node_name = json.loads(nodesStr)['中药名']
            node_xw = json.loads(nodesStr)['性味']
            node_gj = json.loads(nodesStr)['归经']
            node_image = json.loads(nodesStr)['image']

            data7_dict = {
                'id': node_id,
                'ID': node_ID,
                'name': node_name,
                'xw': node_xw,
                'gj': node_gj,
                'image': node_image,
                'category': '中药'
            }
            data.append(data7_dict)
    
    # 关系：代表方->中药
    for dbf_bzm in dbf_all:
        for cm_bzm in cm_all:
            rel6 = graph.run('MATCH(n:`代表方`{`代表方`:"' + dbf_bzm + '"})<-[rel]->(m:`中药`{`中药名`:"' + cm_bzm + '"}) return rel').data()
            if rel6 != []:
                for r in rel6:
                    # 提取相应关系 药物组成
                    source = str(r['rel'].start_node['id'])
                    target = str(r['rel'].end_node['id'])
                    name = str(type(r['rel']).__name__)
                    jl = r['rel']['剂量']
                    rel6_dict = {
                        'source': source,
                        'target': target,
                        'name': name,
                        'jl': jl
                    }
                    link.append(rel6_dict)

    neo4j_data = {
        'data': data,
        'links': link
    }
    # 转换成json文件
    neo4j_data = json.dumps(neo4j_data)
    return neo4j_data


# 查询症状及其步长为1的关系节点
def search_one(value):
    # 定义data数组存储节点信息
    data = []
    # 定义links数组存储关系信息
    links = []
    # 查询节点是否存在
    # 通过别名找症状标准名
    node = graph.run('MATCH(n:`症状`{`标准名`:"' + value + '"}) return n').data()
    # 如果症状标准名中找不到，通过别名找症状标准名
    if node == []:
        node = graph.run('match(n:`症状`)-[r:`别名`]->(m:`症状别名`{`标准名`:"' + value + '"}) return n').data()
    # 如果还找不到，用模糊查询
    if node == []:
        node = graph.run('match (n:`症状`) where n.`标准名` =~ ".*' + value + '.*" return n').data()
    # 如果节点存在len(node)的值为1，不存在则len(node)的值为0
    if len(node):
        # 获取节点的所有属性  id 关系要用(唯一值)
        node_id = node[0]['n']['id']
        node_ID = node[0]['n']['ID']
        node_bzm = node[0]['n']['标准名']
        node_py = node[0]['n']['拼音']
        node_zl = node[0]['n']['种类']
        node_image = node[0]['n']['image']
        # 如果是模糊查询或症状别名的话，这里转变成标准名，方便后续查询
        value = node_bzm
        # 构造字典存放节点信息
        dict = {
            'id': node_id,
            'ID': node_ID,
            'name': node_bzm,
            'py': node_py,
            'zl': node_zl,
            'image': node_image,
            'category': '症状'
        }
        data.append(dict)

        # 证素
        # 查询与该节点有关的节点，步长为1，并返回这些节点
        nodes = graph.run('MATCH(n:`症状`{`标准名`:"' + value + '"})<-->(m:`证素`) return m').data()
        # 查询该节点所涉及的所有关系，步长为1，并返回这些关系
        reps = graph.run('MATCH(n:`症状`{`标准名`:"' + value + '"})<-[rel]->(m:`证素`) return rel').data()
        # 处理节点信息
        for n in nodes:
            # 将节点信息的格式转化为json
            node = json.dumps(n, ensure_ascii=False)
            node = json.loads(node)
            # 取出节点的信息（属性）
            zs_id = str(node['m']['id'])
            zs_ID = str(node['m']['ID'])
            zs_bzm = str(node['m']['标准名'])
            zs_py = str(node['m']['拼音'])
            zs_bw = str(node['m']['病位'])
            dict = {
                'id': zs_id,
                'ID': zs_ID,
                'name': zs_bzm,
                'py': zs_py,
                'bw': zs_bw,
                'category': '证素'
            }
            data.append(dict)

        # 存储关系
        for r in reps:
            # 起始节点
            source = str(r['rel'].start_node['id'])
            # 目的节点
            target = str(r['rel'].end_node['id'])
            # 关系名称
            name = str(type(r['rel']).__name__)
            score = r['rel']['得分']
            dict = {
                'source': source,
                'target': target,
                'name': name,
                'score': score
            }
            links.append(dict)
        
        # 症状别名
        nodes = graph.run('MATCH(n:`症状`{`标准名`:"' + value + '"})<-->(m:`症状别名`) return m').data()
        reps = graph.run('MATCH(n:`症状`{`标准名`:"' + value + '"})<-[rel]->(m:`症状别名`) return rel').data()
        for n in nodes:
            node = json.dumps(n, ensure_ascii=False)
            node = json.loads(node)
            bm_id = str(node['m']['id'])
            bm_ID = str(node['m']['ID'])
            bm_bzm = str(node['m']['别名的标准名'])
            bm_bm = str(node['m']['标准名'])
            bm_py = str(node['m']['拼音'])
            dict = {
                'id': bm_id,
                'ID': bm_ID,
                'bzm': bm_bzm,
                'name': bm_bm,
                'py': bm_py,
                'category': '症状别名'
            }
            data.append(dict)
        for r in reps:
            source = str(r['rel'].start_node['id'])
            target = str(r['rel'].end_node['id'])
            name = str(type(r['rel']).__name__)
            dict = {
                'source': source,
                'target': target,
                'name': name
            }
            links.append(dict)

        # 症状种类
        nodes = graph.run('MATCH(n:`症状`{`标准名`:"' + value + '"})<-->(m:`症状种类`) return m').data()
        reps = graph.run('MATCH(n:`症状`{`标准名`:"' + value + '"})<-[rel]->(m:`症状种类`) return rel').data()
        for n in nodes:
            node = json.dumps(n, ensure_ascii=False)
            node = json.loads(node)
            zl_id = str(node['m']['id'])
            zl_ID = str(node['m']['ID'])
            zl_bzm = str(node['m']['标准名'])
            zl_py = str(node['m']['拼音'])
            dict = {
                'id': zl_id,
                'ID': zl_ID,
                'name': zl_bzm,
                'py': zl_py,
                'category': '症状种类'
            }
            data.append(dict)
        for r in reps:
            source = str(r['rel'].start_node['id'])
            target = str(r['rel'].end_node['id'])
            name = str(type(r['rel']).__name__)
            dict = {
                'source': source,
                'target': target,
                'name': name
            }
            links.append(dict)

        # 构造字典存储data和links
        search_neo4j_data = {
            'data': data,
            'links': links
        }
        # 将dict转化为json格式
        search_neo4j_data = json.dumps(search_neo4j_data)
        return search_neo4j_data
    else:
        print("查无此节点")
        return 0

# 诊断 传入参数为多个症状
def diagnosis_score(value):
    # 分词，默认以空格为分隔符
    zzbm = value.split()
    # 去重且保持原来的顺序
    zzbm = [*pd.unique(zzbm)]
    # 计算症状数目
    length = len(zzbm)
    # 设置一个列表，存放证素
    zs_list = []
    # 设置一个字典，存所有症状的对应证素及其得分字典
    zz_score_zs = {}

    # 常用口语化词标准化
    for i in range(0, length):
        # 取出别名
        bm = zzbm[i]
        if bm == '发烧':
            bm = '发热'
        if bm == '胃痛':
            bm = '脘腹痛'
        if bm == '肚子痛':
            bm = '腹痛'
        if bm == '口干':
            bm = '口渴'
        if bm == '疲劳' or bm == '疲倦' or bm == '疲乏':
            bm = '倦怠乏力'
        if bm == '耳鸣':
            bm = '耳久鸣'
        if bm != '阴雨天疼痛加重' and bm != '肌肉疼痛':
            for index in range(len(bm)):
                if bm[index] == '疼':
                    # 将字符串转换成列表后修改值，然后用join组成新字符串
                    bm1 = list(bm)
                    bm1[index] = '痛'
                    bm = ''.join(bm1)

        # 通过别名找症状标准名
        zz = graph.run('match(n:`症状`)-[r:`别名`]->(m:`症状别名`{`标准名`:"' + bm + '"}) return n').data()
        # 如果症状别名中找不到，直接找症状
        if zz == []:
            zz = graph.run('match(n:`症状`{`标准名`:"' + bm + '"}) return n').data()
        # 如果还找不到，用模糊查询
        if zz == []:
            zz = graph.run('match (n:`症状`) where n.`标准名` =~ ".*' + bm + '.*" return n').data()
        # 取出症状
        zz = zz[0]['n']
        # 转化成json格式，取出症状的标准名
        nodesStr = json.dumps(zz, ensure_ascii=False)
        zz_bzm = json.loads(nodesStr)['标准名']
        # 通过症状查找其对应所有证素
        zs = graph.run('match(n:`症状`{`标准名`:"' + zz_bzm + '"})-[r:`辨识`]->(m:`证素`) return m, r.`得分` as score').data()
        # 设一个字典，存键值对 {证素标准名：得分}
        zs_score = {}
        # 取出某个症状对应的所有证素及得分
        for k in range(0, len(zs)):
            # 取出证素
            zs1 = zs[k]['m']
            # 取出得分
            score = zs[k]['score']
            # 转化为json格式，取出证素的标准名
            nodesStr1 = json.dumps(zs1, ensure_ascii=False)
            zs_bzm = json.loads(nodesStr1)['标准名']
            zs_list.append(zs_bzm)
            # 键值对 {证素标准名：得分}
            zs_score[zs_bzm] = round(float(score), 1)
        # 设置一个字典，存所有症状的对应证素及其得分字典
        zz_score_zs[zz_bzm] = zs_score

    # 症状-得分-证素 字典{症状1：{证素1：得分，证素2：得分}，症状2：{证素1：得分，证素3：得分}}
    # 转换成 证素1[得分，得分...]  证素2[得分，0...]  证素3[0，得分...]
    # 对zs_list去重
    new_zs = list(set(zs_list))
    # 保证去重后的顺序不变
    new_zs.sort(key=zs_list.index)

    # 每个证素一个列表   证素1[症状1得分，症状2得分...]
    l = []
    for i in range(0, len(new_zs)):
        l.append([])

    # 设置一个列表，存每个证素总得分 [证素1总得分，证素2总得分]
    score_list = []
    # 设置一个列表，存排序后证素名合集
    zs_list2 = []
    # 设置一个字典，存排序后 {证素：总得分}
    score_sort = {}

    # 外层为证素，内层为 症状-得分-证素 字典，先取外层字典的值，再取内层字典的键，得到证素
    for z in range(0, len(new_zs)):
        for key, value in zz_score_zs.items():
            flag = 0
            # 取出 {证素1：得分，证素2：得分} temp
            temp = zz_score_zs[key]
            for k, v in temp.items():
                # 该症状的证素与总证素列表相匹配，为了挑出该症状中没有的证素
                if k == new_zs[z]:
                    l[z].append(v)
                    #若添加过了，设一个标志
                    flag = 1
            # 说明这个症状没有此证素，得分设为0
            if flag != 1:
                l[z].append(0)

        # 通过l计算证素得分
        # 计算每个证素总得分
        temp_sum = 0
        for i in range(0, len(zzbm)):
            temp_sum = temp_sum + l[z][i]
        # 求总得分这里也要保留一位小数
        temp_sum = round(temp_sum, 1)
        score_list.append(temp_sum)
        # 得分排序（由高到低）
        score_id = sorted(range(len(score_list)), key=lambda k:score_list[k], reverse=True)
    # 取得分前五的证素及其总得分
    for i in range(0, 5):
        # id 定位到该值
        id = score_id[i]
        # 取对应证素名
        zs_name = new_zs[id]
        # 排序后证素名合集
        zs_list2.append(zs_name)
        # 取对应证素得分
        point = score_list[id]
        # 排序后 {证素：总得分}
        score_sort[zs_name] = point

    # 替换一些不能模糊查询的词
    b = ['心神' if i == '心神[脑][心][神]' else i for i in zs_list2]
    c = ['筋骨' if i == '筋骨[关节]' else i for i in b]
    d = ['火' if i == '火[热]' else i for i in c]
    e = ['津' if i == '津[液]亏' else i for i in d]
    f = ['精' if i == '精[髓]亏' else i for i in e]

    # 通过（必有 或有）证素找证
    # 设置一个列表，存放所有证
    zheng_list = []
    for k in range(0, len(f)):
         # 通过证素查找证，由于一个证包含多个证素，所以用模糊查询
         zheng = graph.run('match(n:`证`) where n.`必有证素` =~ ".*' + f[k] + '.*" return n').data()
         for j in range(0, len(zheng)):
            zheng1 = zheng[j]['n']
            nodesStr2 = json.dumps(zheng1, ensure_ascii=False)
            zheng_bzm = json.loads(nodesStr2)['标准名']
            zheng_list.append(zheng_bzm)
        
        # 加入或有证素
         zheng_hy = graph.run('match(n:`证`) where n.`或有证素` =~ ".*' + f[k] + '.*" return n').data()
         for j in range(0, len(zheng_hy)):
            zheng1 = zheng_hy[j]['n']
            nodesStr2 = json.dumps(zheng1, ensure_ascii=False)
            zheng_bzm = json.loads(nodesStr2)['标准名']
            zheng_list.append(zheng_bzm)

    # 对列表的值计数（Panda库）证1：次数，证2：次数  包含从高到低排序
    zheng_count = pd.value_counts(zheng_list)

    # 设置一个列表，存放次数大于1的证
    zheng_new = []
    # 取阈值 >1 的证
    for i in range(0, len(zheng_count)):
        if zheng_count[i] > 1:
            zheng_new.append(zheng_count.axes[0][i])
        else:
            break
    # 取前8个证
    zheng_new = zheng_new[:8]

    # 从证找证素，比对 计算证的总得分
    # 设置一个字典，{证1：{证素：得分，证素：得分}，证2：{证素：得分，证素：得分}}
    zh_dict = {}
    # 设置一个字典，{证：总得分}
    zheng_s_dict = {}
    # 设置一个字典，必有证素的{证：总得分}
    zheng_s_dict_by = {}

    for i in range(0, len(zheng_new)):
        # 通过证查找证素（必有 和 或有）
        zh_su = graph.run('match(n:`证`) where n.`标准名` = "' + zheng_new[i] + '" return n.`必有证素`, n.`或有证素`').data()
        zh_bysu = zh_su[0]['n.`必有证素`']
        zh_hysu = zh_su[0]['n.`或有证素`']
        # 分词，以、为分隔符
        # 必有
        zh_byzs_div = zh_bysu.split('、')
        # 必有 + 或有
        zh_su_div = zh_bysu.split('、')
        if zh_hysu != None:
            zh_su_div = zh_su_div + zh_hysu.split('、')

        # 设置一个字典，存放{证素：得分，证素：得分}
        zh_score_zs = {}
        # 总得分 必有 + 或有
        zheng_s = 0
        # 必有证素总得分
        zheng_by_s = 0

        # 将 排序后的证素 和 必有或有证素合集 进行匹配
        for m in range(0, len(zs_list2)):
            flag = 0
            for n in range(0, len(zh_su_div)):
                if zh_su_div[n] == zs_list2[m]:
                    zh_score_zs[zs_list2[m]] = score_sort[zs_list2[m]]
                    # 若添加过了，设一个标志
                    flag = 1
                    zheng_s = zheng_s + score_sort[zs_list2[m]]
                    zheng_s_dict[zheng_new[i]] = zheng_s
            # 说明证没有此证素，得分设为0
            if flag == 0:
                zh_score_zs[zs_list2[m]] = 0
            
            # 单独算只有必有证素的总得分
            for n in range(0, len(zh_byzs_div)):
                if zh_byzs_div[n] == zs_list2[m]:
                    zheng_by_s = zheng_by_s + score_sort[zs_list2[m]]
                    zheng_s_dict_by[zheng_new[i]] = zheng_by_s

        zh_dict[zheng_new[i]] = zh_score_zs

    # 设置一个列表 存排序后的证名 必有证素
    zheng_by_list = []
    # 设置一个列表 存排序后的证名 必有+或有 （由高到低）
    zheng_sort_list = []
    # 必有证素总得分排序 [（证名，总得分）...]
    zheng_sort_by = sorted(zheng_s_dict_by.items(), key=lambda d:d[1], reverse=True)
    # 取出其证名
    for i in range(0, len(zheng_sort_by)):
        zheng_by_list.append(zheng_sort_by[i][0])
    # 根据必有证素总得分排序的证名，对证总得分字典进行排序（将同分的，但必有证素得分高的排前面）
    zheng_sort = {k:zheng_s_dict[k] for k in zheng_by_list if k in zheng_s_dict}
    # 由于根据必有证素排会有整体得分低的排前面，则再对证总得分字典进行降序排序（此时同分的不会改变顺序）
    zheng_sort = sorted(zheng_sort.items(), key=lambda d:d[1], reverse=True)
    # 取出其证名
    for i in range(0, len(zheng_sort)):
        zheng_sort_list.append(zheng_sort[i][0])
    # 根据最终总得分排序的证名，对zh_dict进行排序（便于绘制联动图中的柱状图）
    zh_dict = {k:zh_dict[k] for k in zheng_sort_list if k in zh_dict}

    # 设置一个列表，放排序好的证的证名 (由低到高)
    zheng_order = zheng_sort_list[::-1]
    # 最终的证（诊断结果），即排名第一的证
    zheng_final = zheng_sort[0][0]

    # 通过证找代表方
    # 设置一个列表，存代表方
    dbf_list = []
    for i in range(0, len(zheng_order)):
        # 找该证的代表方
        dbf = graph.run('match(n:`证`{`标准名`:"' + zheng_order[i] + '"})-[r:`治疗方剂`]->(m:`代表方`) return m').data()
        # 取出代表方
        dbf1 = dbf[0]['m']
        # 转成json格式
        nodesStr = json.dumps(dbf1, ensure_ascii=False)
        # 再由json转回python对象，变成键值对形式，方便后续取值
        dbf_name = json.loads(nodesStr)['代表方']
        dbf_list.append(dbf_name)

    # 通过代表方找其药物组成
    # 设置一个字典，存代表方对应 药物组成字典 {{中药1：剂量1，中药2：剂量2}，{中药1：剂量1，中药2：剂量2}}
    dbf_cm_list = []
    for i in range(0, len(dbf_list)):
        # 找对应中药
        cm = graph.run('match(n:`代表方`{`代表方`:"' + dbf_list[i] + '"})-[r:`药物组成`]->(m:`中药`) return m, r.`剂量` as jl').data()
        # 设置一个字典，存中药及其对应剂量 {中药1：剂量1，中药2：剂量2}
        cm_jl_dict = {}
        for j in range(0, len(cm)):
            cm1 = cm[j]['m']
            jl = cm[j]['jl']
            nodesStr = json.dumps(cm1, ensure_ascii=False)
            cm_name = json.loads(nodesStr)['中药名']
            cm_jl_dict[cm_name] = round(float(jl), 1)
        dbf_cm_list.append(cm_jl_dict)

    # 将字典转换成更好调用的格式
    zh_dbf_cm = {
        'dbf': dbf_list,
        'cm_jl': dbf_cm_list,
    }

    # 设置一个列表，放得分前五证素的总得分
    zs_point_list = []
    for item in zs_list2:
        t = score_sort[item]
        zs_point_list.append(t)
    # 再放在一个字典里
    score_sort1 = {
        'zs': zs_list2,
        'score': zs_point_list
    }
    
    # 每个证素一个列表 [[证1的证素1的得分,证2的证素1的得分,...],[证1的证素2的得分,证2的证素2的得分,...]]
    l2 = []
    for i in range(0, len(zs_list2)):
        l2.append([])
    
    # 设置一个列表，存放每个证的{{证素：得分}, {证素：得分}}集合
    zh_zs_point_list = []
    for item in zheng_order:
        t = zh_dict[item]
        zh_zs_point_list.append(t)
    for m in range(0, len(zheng_order)):
        t = zh_zs_point_list[m]
        n = 0
        for k, v in t.items():
            # 将对应得分存到对应证素列表里
            l2[n].append(v)
            n = n + 1
    # 再放在一个字典里
    zh_dict1 = {
        'zheng': zheng_order,
        'zs': zs_list2,
        'score': l2
    }

    # 诊断结果处，总体展示症状-证素-证的关系图
    # 实体
    data_zheng = {
        'name': zheng_final,
        'category': 0
    }
    # 设置一个列表，存证素字典
    data_zs = []
    for item in zs_list2:
        dict_zs = {
            'name': item,
            'category': 1
        }
        data_zs.append(dict_zs)
    # 设置一个列表，存症状字典
    data_zz = []
    for item in zzbm:
        dict_zz = {
            'name': item,
            'category': 2
        }
        data_zz.append(dict_zz)

    # 关系
    # 设置一个列表存索引(取到症状别名对应证素的原始索引)
    ind = []
    for item in zs_list2:
        for i in range(0, len(new_zs)):
            if new_zs[i] == item:
                ind.append(i)
    # 设置一个列表，存所有关系
    dict_re = []
    for i in range(0, len(ind)):
        t = l[ind[i]]
        for j in range(0, len(zzbm)):
            # 设置一个字典，存 症状-证素 关系
            dict1 = {}
            temp = l[ind[i]][j]
            if temp != 0:
                dict1 = {
                    'source': zzbm[j],
                    'value': temp,
                    'target': zs_list2[i]
                }
            if dict1 != {}:
                dict_re.append(dict1)
    for i in range(0, len(zs_list2)):
        # 设置一个字典，存 证-证素 关系
        dict2 = {}
        score = zh_dict1['score'][i]
        tem = score[len(zheng_order)-1]
        if tem != 0:
            dict2 = {
                'source': zheng_order[len(zheng_order)-1],
                'value': tem,
                'target': zs_list2[i]
            }
        if dict2 != {}:
            dict_re.append(dict2)
    # 用一个总的字典存节点与关系  为 症状-证素-证的关系图 服务
    neo4j_data = {
        'data_zheng': data_zheng,
        'data_zs': data_zs,
        'data_zz': data_zz,
        'data_link': dict_re
    }
    return neo4j_data, zzbm , new_zs, l, score_sort1, zh_dict1, zheng_final, zh_dbf_cm

# 查询节点
def search_node(select, input_content):
    # 查找节点是否存在
    if select == '症状' or select == '证素' or select == '证' or select == '症状别名' or select == '症状种类':
        result = graph.run('match(n:`' + select + '`) where n.`标准名`="' + input_content + '" return n').data()
    elif select == '代表方':
        result = graph.run('match(n:`代表方`) where n.`代表方`="' + input_content + '" return n').data()
    elif select == '中药':
        result = graph.run('match(n:`中药`) where n.`中药名`="' + input_content + '" return n').data()
    if result == []:
            return False
    else:
        return True

# 修改功能 根据节点预填数据值 （查询）
def search_modify(select, search_input):
    if select == '症状' or select == '证素' or select == '证':
        result = graph.run('match(n:`' + select + '`) where n.`标准名`="' + search_input + '" return n').data()
    elif select == '中药':
        result = graph.run('match(n:`中药`) where n.`中药名`="' + search_input + '" return n').data()
    if result == []:
            flag_modify = 0
            modify_data = {}
    else:
        flag_modify = 1
        if select == '症状':
            zz = result[0]['n']
            # 转化成json格式，取出症状所有属性
            nodesStr = json.dumps(zz, ensure_ascii=False)
            zz_Id = json.loads(nodesStr)['ID']
            zz_bzm = json.loads(nodesStr)['标准名']
            zz_py = json.loads(nodesStr)['拼音']
            zz_zl = json.loads(nodesStr)['种类']
            zz_image = json.loads(nodesStr)['image']
            modify_data = {
                'flag_modify': flag_modify, 
                'zz_Id': zz_Id,
                'zz_bzm': zz_bzm,
                'zz_py': zz_py,
                'zz_zl': zz_zl,
                'zz_image': zz_image
            }
        elif select == '证素':
            zs = result[0]['n']
            nodesStr = json.dumps(zs, ensure_ascii=False)
            zs_Id = json.loads(nodesStr)['ID']
            zs_bzm = json.loads(nodesStr)['标准名']
            zs_py = json.loads(nodesStr)['拼音']
            zs_bw = json.loads(nodesStr)['病位']
            modify_data = {
                'flag_modify': flag_modify, 
                'zs_Id': zs_Id,
                'zs_bzm': zs_bzm,
                'zs_py': zs_py,
                'zs_bw': zs_bw,
            }
        elif select == '证':
            zheng = result[0]['n']
            nodesStr = json.dumps(zheng, ensure_ascii=False)
            zheng_Id = json.loads(nodesStr)['ID']
            zheng_bzm = json.loads(nodesStr)['标准名']
            zheng_zl = json.loads(nodesStr)['种类']
            zheng_zf = json.loads(nodesStr)['脏腑']
            zheng_byzs = json.loads(nodesStr)['必有证素']
            zheng_hyzs = json.loads(nodesStr)['或有证素']
            modify_data = {
                'flag_modify': flag_modify, 
                'zheng_Id': zheng_Id,
                'zheng_bzm': zheng_bzm,
                'zheng_zl': zheng_zl,
                'zheng_zf': zheng_zf,
                'zheng_byzs': zheng_byzs,
                'zheng_hyzs': zheng_hyzs
            }
        elif select == '中药':
            cm = result[0]['n']
            nodesStr = json.dumps(cm, ensure_ascii=False)
            cm_Id = json.loads(nodesStr)['ID']
            cm_zym = json.loads(nodesStr)['中药名']
            cm_xw = json.loads(nodesStr)['性味']
            cm_gj = json.loads(nodesStr)['归经']
            cm_image = json.loads(nodesStr)['image']
            modify_data = {
                'flag_modify': flag_modify, 
                'cm_Id': cm_Id,
                'cm_zym': cm_zym,
                'cm_xw': cm_xw,
                'cm_gj': cm_gj,
                'cm_image': cm_image
            }
    return modify_data

# 修改节点
def modify_node(select, modify_dict):
    if select == '症状':
        zz_Id_input = modify_dict['zz_Id_input']
        zz_bzm_input = modify_dict['zz_bzm_input']
        zz_py_input = modify_dict['zz_py_input']
        zz_zl_input = modify_dict['zz_zl_input']
        zz_image_input = modify_dict['zz_image_input']
        graph.run('match(n:`症状`{`标准名`:"' + zz_bzm_input + '"}) set n.ID = "' + zz_Id_input + '", n.`拼音` = "' + zz_py_input + '", n.`种类` = "' + zz_zl_input + '", n.image = "' + zz_image_input + '"').data()
    elif select == '证素':
        zs_Id_input = modify_dict['zs_Id_input']
        zs_bzm_input = modify_dict['zs_bzm_input']
        zs_py_input = modify_dict['zs_py_input']
        zs_bw_input = modify_dict['zs_bw_input']
        graph.run('match(n:`证素`{`标准名`:"' + zs_bzm_input + '"}) set n.ID = "' + zs_Id_input + '", n.`拼音` = "' + zs_py_input + '", n.`病位` = "' + zs_bw_input + '" return n').data()
    elif select == '证':
        zheng_Id_input = modify_dict['zheng_Id_input']
        zheng_bzm_input = modify_dict['zheng_bzm_input']
        zheng_zl_input = modify_dict['zheng_zl_input']
        zheng_zf_input = modify_dict['zheng_zf_input']
        zheng_byzs_input = modify_dict['zheng_byzs_input']
        zheng_hyzs_input = modify_dict['zheng_hyzs_input']
        graph.run('match(n:`证`{`标准名`:"' + zheng_bzm_input + '"}) set n.ID = "' + zheng_Id_input + '", n.`种类` = "' + zheng_zl_input + '", n.`脏腑` = "' + zheng_zf_input + '", n.`必有证素` = "' + zheng_byzs_input + '", n.`或有证素` = "' + zheng_hyzs_input + '" return n').data()
    elif select == '中药':
        cm_Id_input = modify_dict['cm_Id_input']
        cm_zym_input = modify_dict['cm_zym_input']
        cm_xw_input = modify_dict['cm_xw_input']
        cm_gj_input = modify_dict['cm_gj_input']
        cm_image_input = modify_dict['cm_image_input']
        graph.run('match(n:`中药`{`中药名`:"' + cm_zym_input + '"}) set n.ID = "' + cm_Id_input + '", n.`性味` = "' + cm_xw_input + '", n.`归经` = "' + cm_gj_input + '", n.image = "' + cm_image_input + '" return n').data()

# 删除节点
def del_node(select, input_content):
    if select == '症状' or select == '证素' or select == '证' or select == '症状别名' or select == '症状种类':
        graph.run('match(n:`' + select + '`{`标准名`:"' + input_content + '"}) delete n').data()
    elif select == '代表方':
        graph.run('match(n:`代表方`{`代表方`:"' + input_content + '"}) delete n').data()
    elif select == '中药':
        graph.run('match(n:`中药`{`中药名`:"' + input_content + '"}) delete n').data()

# 增加单个节点
def add_node(select, add_dict):
    if select == '症状':
        zz_bzm_add_input = add_dict['zz_bzm_add_input']
        zz_py_add_input = add_dict['zz_py_add_input']
        zz_zl_add_input = add_dict['zz_zl_add_input']
        zz_image_add_input = add_dict['zz_image_add_input']
        # 先判断节点是否存在
        result = graph.run('match(n:`症状`) where n.`标准名`="' + zz_bzm_add_input + '" return n').data()
        if result == []:
            # 先计算该实体的节点总个数，便于ID的增加
            count_num = graph.run('match(n:`症状`) return count(n)').data()
            # 语句运行需要是str
            zz_ID_add = str(int(count_num[0]['count(n)']) + 1)
            # 先计算实体总个数，便于id增加
            zz_id_num = graph.run('match(n) return count(*)').data()
            zz_id_add = str(int(zz_id_num[0]['count(*)']) + 1)
            graph.run('create(n:`症状`{id:"' + zz_id_add + '", ID:"' + zz_ID_add + '", `标准名`:"' + zz_bzm_add_input + '", `拼音`:"' + zz_py_add_input + '", `种类`:"' + zz_zl_add_input + '", `image`:"' + zz_image_add_input + '"}) return n').data()
            return True
        else:
            return False
    elif select == '证素':
        zs_bzm_add_input = add_dict['zs_bzm_add_input']
        zs_py_add_input = add_dict['zs_py_add_input']
        zs_bw_add_input = add_dict['zs_bw_add_input']
        # 先判断节点是否存在
        result = graph.run('match(n:`证素`) where n.`标准名`="' + zs_bzm_add_input + '" return n').data()
        if result == []:
            # 先计算该实体的节点总个数，便于ID的增加
            count_num = graph.run('match(n:`证素`) return count(n)').data()
            zs_ID_add = str(int(count_num[0]['count(n)']) + 1)
            # 先计算实体总个数，便于id增加
            zs_id_num = graph.run('match(n) return count(*)').data()
            zs_id_add = str(int(zs_id_num[0]['count(*)']) + 1)
            graph.run('create(n:`证素`{id:"' + zs_id_add + '", ID:"' + zs_ID_add + '", `标准名`:"' + zs_bzm_add_input + '", `拼音`:"' + zs_py_add_input + '", `病位`:"' + zs_bw_add_input + '"}) return n').data()
            return True
        else:
            return False
    elif select == '证':
        zheng_bzm_add_input =add_dict['zheng_bzm_add_input']
        zheng_zl_add_input = add_dict['zheng_zl_add_input']
        zheng_zf_add_input = add_dict['zheng_zf_add_input']
        zheng_byzs_add_input = add_dict['zheng_byzs_add_input']
        zheng_hyzs_add_input = add_dict['zheng_hyzs_add_input']
        # 先判断节点是否存在
        result = graph.run('match(n:`证`) where n.`标准名`="' + zheng_bzm_add_input + '" return n').data()
        if result == []:
            # 先计算该实体的节点总个数，便于ID的增加
            count_num = graph.run('match(n:`证`) return count(n)').data()
            zheng_ID_add = str(int(count_num[0]['count(n)']) + 1)
            # 先计算实体总个数，便于id增加
            zheng_id_num = graph.run('match(n) return count(*)').data()
            zheng_id_add = str(int(zheng_id_num[0]['count(*)']) + 1)
            graph.run('create(n:`证`{id:"' + zheng_id_add + '", ID:"' + zheng_ID_add + '", `标准名`:"' + zheng_bzm_add_input + '", `种类`:"' + zheng_zl_add_input + '", `脏腑`:"' + zheng_zf_add_input + '", `必有证素`:"' + zheng_byzs_add_input + '", `或有证素`:"' + zheng_hyzs_add_input + '"}) return n').data()
            return True
        else:
            return False
    elif select == '中药':
        cm_zym_add_input = add_dict['cm_zym_add_input']
        cm_xw_add_input = add_dict['cm_xw_add_input']
        cm_gj_add_input = add_dict['cm_gj_add_input']
        cm_image_add_input = add_dict['cm_image_add_input']
        # 先判断节点是否存在
        result = graph.run('match(n:`中药`) where n.`中药名`="' + cm_zym_add_input + '" return n').data()
        if result == []:
            # 先计算该实体的节点总个数，便于ID的增加
            count_num = graph.run('match(n:`中药`) return count(n)').data()
            cm_ID_add = str(int(count_num[0]['count(n)']) + 1)
            # 先计算实体总个数，便于id增加
            cm_id_num = graph.run('match(n) return count(*)').data()
            cm_id_add = str(int(cm_id_num[0]['count(*)']) + 1)
            graph.run('create(n:`中药`{id:"' + cm_id_add + '", ID:"' + cm_ID_add + '", `中药名`:"' + cm_zym_add_input + '", `性味`:"' + cm_xw_add_input + '", `归经`:"' + cm_gj_add_input + '", `image`:"' + cm_image_add_input + '"}) return n').data()
            return True
        else:
            return False
    elif select == '代表方':
        dbf_dbf_add_input = add_dict['dbf_dbf_add_input']
        # 先判断节点是否存在
        result = graph.run('match(n:`代表方`) where n.`代表方`="' + dbf_dbf_add_input + '" return n').data()
        if result == []:
            # 先计算该实体的节点总个数，便于ID的增加
            count_num = graph.run('match(n:`代表方`) return count(n)').data()
            dbf_ID_add = str(int(count_num[0]['count(n)']) + 1)
            # 先计算实体总个数，便于id增加
            dbf_id_num = graph.run('match(n) return count(*)').data()
            dbf_id_add = str(int(dbf_id_num[0]['count(*)']) + 1)
            graph.run('create(n:`代表方`{id:"' + dbf_id_add + '", ID:"' + dbf_ID_add + '", `代表方`:"' + dbf_dbf_add_input + '"}) return n').data()
            return True
        else:
            return False

# 批量增加 中药表
def adds_cm():
    path = 'D:/flask_project/bysj/MMKG/static/upload_files/ChineseMedicine.csv'
    data = pd.read_csv(path)
    # 按行取对应值
    for i, row in data.iterrows():
        cm = row['cm']
        xingwei = row['xingwei']
        guijing = row['guijing']
        cm_image = row['cm_image']
        # 判断内容是否为nan
        if pd.isna(cm) == False:
            # 先判断是否已存在
            result = graph.run('match(n:`中药`) where n.`中药名`="' + cm + '" return n').data()
            if result == []:
                # 先计算该实体的节点总个数，便于ID的增加
                ID_num = graph.run('match(n:`中药`) return count(n)').data()
                ID = str(int(ID_num[0]['count(n)']) + 1)
                # 先计算实体总个数，便于id增加
                id_num = graph.run('match(n) return count(*)').data()
                id = str(int(id_num[0]['count(*)']) + 1)
                graph.run('create(n:`中药`{id:"' + id + '", ID:"' + ID + '", `中药名`:"' + cm + '", `性味`:"' + xingwei + '", `归经`:"' + guijing + '", `image`:"' + cm_image + '"}) return n').data()
    return

# 批量增加 代表方-中药表
def adds_pcm():
    path = 'D:/flask_project/bysj/MMKG/static/upload_files/Prescription_CM.csv'
    data = pd.read_csv(path)
    # 按行取对应值
    for i, row in data.iterrows():
        perscription = row['perscription']
        cm1 = row['cm1']
        jl1 = str(row['jl1'])
        cm2 = row['cm2']
        jl2 = str(row['jl2'])
        cm3 = row['cm3']
        jl3 = str(row['jl3'])
        cm4 = row['cm4']
        jl4 = str(row['jl4'])
        cm5 = row['cm5']
        jl5 = str(row['jl5'])
        cm6 = row['cm6']
        jl6 = str(row['jl6'])
        cm7 = row['cm7']
        jl7 = str(row['jl7'])
        cm8 = row['cm8']
        jl8 = str(row['jl8'])
        cm9 = row['cm9']
        jl9 = str(row['jl9'])
        cm10 = row['cm10']
        jl10 = str(row['jl10'])
        cm11 = row['cm11']
        jl11 = str(row['jl11'])
        cm12 = row['cm12']
        jl12 = str(row['jl12'])
        cm13 = row['cm13']
        jl13 = str(row['jl13'])
        cm14 = row['cm14']
        jl14 = str(row['jl14'])
        cm15 = row['cm15']
        jl15 = str(row['jl15'])
        cm16 = row['cm16']
        jl16 = str(row['jl16'])
        cm17 = row['cm17']
        jl17 = str(row['jl17'])
        cm18 = row['cm18']
        jl18 = str(row['jl18'])
        # 添加实体：代表方
        # 判断内容是否为nan
        if pd.isna(perscription) == False:
            # 先判断节点是否存在
            result = graph.run('match(n:`代表方`) where n.`代表方`="' + perscription + '" return n').data()
            if result == []:
                # 先计算该实体的节点总个数，便于ID的增加
                count_num = graph.run('match(n:`代表方`) return count(n)').data()
                dbf_ID_add = str(int(count_num[0]['count(n)']) + 1)
                # 先计算实体总个数，便于id增加
                dbf_id_num = graph.run('match(n) return count(*)').data()
                dbf_id_add = str(int(dbf_id_num[0]['count(*)']) + 1)
                graph.run('create(n:`代表方`{id:"' + dbf_id_add + '", ID:"' + dbf_ID_add + '", `代表方`:"' + perscription + '"}) return n').data()
            else:
                # 假如代表方已存在，下面要用到其ID
                count_num = graph.run('match(n:`代表方`) return count(n)').data()
                dbf_ID_add = str(int(count_num[0]['count(n)']) + 1)
        # 判断内容是否为nan
        if pd.isna(cm1) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm1 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm1 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl1 + '"}]->(to)')
        if pd.isna(cm2) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm2 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm2 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl2 + '"}]->(to)')
        if pd.isna(cm3) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm3 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm3 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl3 + '"}]->(to)')
        if pd.isna(cm4) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm4 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm4 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl4 + '"}]->(to)')
        if pd.isna(cm5) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm5 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm5 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl5 + '"}]->(to)')
        if pd.isna(cm6) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm6 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm6 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl6 + '"}]->(to)')
        if pd.isna(cm7) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm7 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm7 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl7 + '"}]->(to)')
        if pd.isna(cm8) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm8 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm8 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl8 + '"}]->(to)')
        if pd.isna(cm9) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm9 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm9 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl9 + '"}]->(to)')
        if pd.isna(cm10) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm10 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm10 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl10 + '"}]->(to)')
        if pd.isna(cm11) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm11 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm11 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl11 + '"}]->(to)')
        if pd.isna(cm12) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm12 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm12 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl12 + '"}]->(to)')
        if pd.isna(cm13) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm13 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm13 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl13 + '"}]->(to)')
        if pd.isna(cm14) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm14 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm14 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl14 + '"}]->(to)')
        if pd.isna(cm15) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm15 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm15 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl15 + '"}]->(to)')
        if pd.isna(cm16) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm16 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm16 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl16 + '"}]->(to)')
        if pd.isna(cm17) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm17 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm17 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl17 + '"}]->(to)')
        if pd.isna(cm18) == False:
            # 判断中药是否存在
            cm_result = graph.run('match(n:`中药`) where n.`中药名`="' + cm18 + '" return n').data()
            if cm_result != []:
                # 添加关系：代表方→中药
                graph.run('match(from:代表方{代表方:"' + perscription + '"}), (to:中药{中药名:"' + cm18 + '"}) merge(from)-[r:药物组成{ID:"' + dbf_ID_add + '",剂量:"' + jl18 + '"}]->(to)')
    return

# 批量增加 证表
def adds_zheng():
    path = 'D:/flask_project/bysj/MMKG/static/upload_files/StandardZheng.csv'
    data = pd.read_csv(path)
    # 按行取对应值
    for i, row in data.iterrows():
        sZhengName = row['sZhengName']
        sType = row['sType']
        sBiyouZhengsu = row['sBiyouZhengsu']
        sHuoyouZhengsu = row['sHuoyouZhengsu']
        sZangfu = row['sZangfu']
        perscription = row['perscription']
        # 处理 或有证素为空 的情况
        if pd.isna(sHuoyouZhengsu) == True:
            sHuoyouZhengsu = ''
        # 添加实体：证
        # 判断内容是否为nan
        if pd.isna(sZhengName) == False:
            # 先判断节点是否存在
            result = graph.run('match(n:`证`) where n.`标准名`="' + sZhengName + '" return n').data()
            if result == []:
                # 先计算该实体的节点总个数，便于ID的增加
                count_num = graph.run('match(n:`证`) return count(n)').data()
                zheng_ID_add = str(int(count_num[0]['count(n)']) + 1)
                # 先计算实体总个数，便于id增加
                zheng_id_num = graph.run('match(n) return count(*)').data()
                zheng_id_add = str(int(zheng_id_num[0]['count(*)']) + 1)
                graph.run('create(n:`证`{id:"' + zheng_id_add + '", ID:"' + zheng_ID_add + '", `标准名`:"' + sZhengName + '", `种类`:"' + sType + '", `脏腑`:"' + sZangfu + '", `必有证素`:"' + sBiyouZhengsu + '", `或有证素`:"' + sHuoyouZhengsu + '"}) return n').data()
            # 添加关系：证→代表方
            if pd.isna(perscription) == False:
                # 判断代表方是否存在
                dbf_result = graph.run('match(n:`代表方`) where n.`代表方`="' + perscription + '" return n').data()
                if dbf_result != []:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:代表方{代表方:"' + perscription + '"}) merge(from) -[r:治疗方剂]->(to)')           
    return

# 批量增加 证-证素表
def adds_sz_zs():
    path = 'D:/flask_project/bysj/MMKG/static/upload_files/StandardZheng_Zhengsu.csv'
    data = pd.read_csv(path)
    # 按行取对应值
    for i, row in data.iterrows():
        sZhengName = row['sZhengName']
        sBiyouZhengsu1 = row['sBiyouZhengsu1']
        sBiyouZhengsu2 = row['sBiyouZhengsu2']
        sBiyouZhengsu3 = row['sHuoyouZhengsu3']
        sBiyouZhengsu4 = row['sHuoyouZhengsu4']
        sHuoyouZhengsu1 = row['sHuoyouZhengsu1']
        sHuoyouZhengsu2 = row['sHuoyouZhengsu2']
        sHuoyouZhengsu3 = row['sHuoyouZhengsu3']
        sHuoyouZhengsu4 = row['sHuoyouZhengsu4']
        sHuoyouZhengsu5 = row['sHuoyouZhengsu5']
        sHuoyouZhengsu6 = row['sHuoyouZhengsu6']
        # 判断内容是否为nan
        if pd.isna(sZhengName) == False:
            # 先判断节点是否存在
            result = graph.run('match(n:`证`) where n.`标准名`="' + sZhengName + '" return n').data()
            if result != []:
                # 添加关系：证→证素
                graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sBiyouZhengsu1 + '"}) merge(from) -[r:必有]->(to)')
                if pd.isna(sBiyouZhengsu2) == False:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sBiyouZhengsu2 + '"}) merge(from) -[r:必有]->(to)')
                if pd.isna(sBiyouZhengsu3) == False:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sBiyouZhengsu3 + '"}) merge(from) -[r:必有]->(to)')
                if pd.isna(sBiyouZhengsu4) == False:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sBiyouZhengsu4 + '"}) merge(from) -[r:必有]->(to)')
                if pd.isna(sHuoyouZhengsu1) == False:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sHuoyouZhengsu1 + '"}) merge(from) -[r:或有]->(to)')
                if pd.isna(sHuoyouZhengsu2) == False:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sHuoyouZhengsu2 + '"}) merge(from) -[r:或有]->(to)')
                if pd.isna(sHuoyouZhengsu3) == False:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sHuoyouZhengsu3 + '"}) merge(from) -[r:或有]->(to)')
                if pd.isna(sHuoyouZhengsu4) == False:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sHuoyouZhengsu4 + '"}) merge(from) -[r:或有]->(to)')
                if pd.isna(sHuoyouZhengsu5) == False:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sHuoyouZhengsu5 + '"}) merge(from) -[r:或有]->(to)')
                if pd.isna(sHuoyouZhengsu6) == False:
                    graph.run('match(from:证{标准名:"' + sZhengName + '"}), (to:证素{标准名:"' + sHuoyouZhengsu6 + '"}) merge(from) -[r:或有]->(to)')
    return

# 批量增加 症状表
def adds_symptom():
    path = 'D:/flask_project/bysj/MMKG/static/upload_files/Symptom.csv'
    data = pd.read_csv(path)
    # 按行取对应值
    for i, row in data.iterrows():
        sSymptom = row['sSymptom']
        sSymptomPy = row['sSymptomPy']
        sBeizhu = row['sBeizhu']
        sTypeName = row['sTypeName']
        image = row['image']
        # 处理 备注为空 的情况
        if pd.isna(sBeizhu) == True:
            sBeizhu = ''
        # 添加实体：症状
        # 判断内容是否为nan
        if pd.isna(sSymptom) == False:
            # 先判断节点是否存在
            result = graph.run('match(n:`症状`) where n.`标准名`="' + sSymptom + '" return n').data()
            if result == []:
                # 先计算该实体的节点总个数，便于ID的增加
                count_num = graph.run('match(n:`症状`) return count(n)').data()
                # 语句运行需要是str
                zz_ID_add = str(int(count_num[0]['count(n)']) + 1)
                # 先计算实体总个数，便于id增加
                zz_id_num = graph.run('match(n) return count(*)').data()
                zz_id_add = str(int(zz_id_num[0]['count(*)']) + 1)
                graph.run('create(n:`症状`{id:"' + zz_id_add + '", ID:"' + zz_ID_add + '", `标准名`:"' + sSymptom + '", `拼音`:"' + sSymptomPy + '", `种类`:"' + sTypeName + '", `image`:"' + image + '"}) return n').data()
            # 添加关系：症状→症状种类
            if pd.isna(sTypeName) == False:
                # 判断症状种类是否存在
                stype_result = graph.run('match(n:`症状种类`) where n.`标准名`= "' + sTypeName + '" return n').data()
                if stype_result != []:
                    graph.run('match(from:症状{标准名:"' + sSymptom + '"}), (to:症状种类{标准名:"' + sTypeName + '"}) merge(from) -[r:种类]->(to)')
    return

# 批量增加 症状别名表
def adds_snn():
    path = 'D:/flask_project/bysj/MMKG/static/upload_files/SymptomNickName.csv'
    data = pd.read_csv(path)
    # 按行取对应值
    for i, row in data.iterrows():
        sSymptom = row['sSymptom']
        sNickName = row['sNickName']
        sNickNamePy = row['sNickNamePy']
        sBeizhu = row['sBeizhu']
        # 处理 备注为空 的情况
        if pd.isna(sBeizhu) == True:
            sBeizhu = ''
        # 添加实体：症状别名
        # 判断内容是否为nan
        if pd.isna(sNickName) == False:
            # 先判断节点是否存在
            result = graph.run('match(n:`症状别名`) where n.`标准名`= "' + sNickName + '" return n').data()
            if result == []:
                # 先计算该实体的节点总个数，便于ID的增加
                count_num = graph.run('match(n:`症状别名·`) return count(n)').data()
                # 语句运行需要是str
                zzbm_ID_add = str(int(count_num[0]['count(n)']) + 1)
                # 先计算实体总个数，便于id增加
                zzbm_id_num = graph.run('match(n) return count(*)').data()
                zzbm_id_add = str(int(zzbm_id_num[0]['count(*)']) + 1)
                # 症状表查询 症状Id
                iSymptomId_add = graph.run('match(n:`症状`{`标准名`:"' + sSymptom + '"}) return n.ID').data()
                iSymptomId = iSymptomId_add[0]['n.ID']
                graph.run('create(n:`症状别名`{id:"' + zzbm_id_add + '", ID:"' + zzbm_ID_add + '", 症状ID:"' + iSymptomId + '", 别名的标准名:"' + sSymptom + '", 标准名:"' + sNickName + '", 拼音:"' + sNickNamePy + '", 备注:"' + sBeizhu + '"}) return n').data()
            # 添加关系：症状→症状别名
            if pd.isna(sSymptom) == False:
                # 判断症状是否存在
                zz_result = graph.run('match(n:`症状`) where n.`标准名`="' + sSymptom + '" return n').data()
                if zz_result != []:
                    graph.run('match(from:症状{标准名:"' + sSymptom + '"}), (to:症状别名{标准名:"' + sNickName + '"}) merge(from) -[r:别名]->(to)')
    return

# 批量增加 证素-症状表
def adds_zs_s():
    path = 'D:/flask_project/bysj/MMKG/static/upload_files/Zhengsu_Symptom.csv'
    data = pd.read_csv(path)
    # 按行取对应值
    for i, row in data.iterrows():
        sSymptom = row['sSymptom']
        sZhengsu = row['sZhengsu']
        sScoreMach = row['sScoreMach']
        # 判断内容是否为nan
        if pd.isna(sSymptom) == False and pd.isna(sZhengsu) == False:
            # 先判断节点是否存在
            zz_result = graph.run('match(n:`症状`) where n.`标准名`="' + sSymptom + '" return n').data()
            zs_result = graph.run('match(n:`证素`) where n.`标准名`="' + sZhengsu + '" return n').data()
            if zz_result != [] and zs_result != []:
                # 该关系总条数，便于ID的增加
                re_num = graph.run('match p=()-[r:`辨识`]->() return count(p)').data()
                re_ID = str(int(re_num[0]['count(p)']) + 1)
                # 症状表查询 症状Id
                iSymptomId_add = graph.run('match(n:`症状`{`标准名`:"' + sSymptom + '"}) return n.ID').data()
                iSymptomId = iSymptomId_add[0]['n.ID']
                # 证素表查询 证素Id
                iZhengsuId_add = graph.run('match(n:`证素`{`标准名`:"' + sZhengsu + '"}) return n.ID').data()
                iZhengsuId = iZhengsuId_add[0]['n.ID']
                # 按比例计算得分
                sScore = round((20 - 0)*(sScoreMach/5 + 8)/(20 + 8), 1)
                sScore = str(sScore)
                sScoreMach = str(sScoreMach)
                # 添加关系：症状→证素
                graph.run('match (from:症状{ID:"' + iSymptomId + '"}),(to:证素{ID:"' + iZhengsuId + '"}) merge (from)-[r:辨识{ID:"' + re_ID + '",得分:"' + sScore + '",证素:"' + sZhengsu + '",症状:"' + sSymptom + '",匹配得分:"' + sScoreMach + '"}]->(to)')
    return
