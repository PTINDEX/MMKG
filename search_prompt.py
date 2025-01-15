# @Author: PT
# @CreateTime: 2024-06-05
# @Description:字典树实现智能搜索提示
# @Version:1.0

# 导入包
from pytrie import StringTrie
import pypinyin
import pandas as pd

# 文本转拼音 每个字的拼音按空格分开  eg. pi fu ma mu
def pinyin(text):
    gap = ' '
    piny = gap.join(pypinyin.lazy_pinyin(text))
    return piny

# 获取拼音的每个首字母
def get_every_word_first(text):
    return ''.join([i[0] for i in pinyin(text).split(' ')])

# 获取所有拼音 中间无间隔 eg. pifumamu
def get_all_pinying(text):
    gap = ''
    piny = gap.join(pypinyin.lazy_pinyin(text))
    return piny

# 自定义字典树类
class Suggester(object):
    def __init__(self):
        self.trie = None
        self.trie = StringTrie()

    def update_trie(self, word_list):
        for word in word_list:
            word = word.lower()
            # 拼音提取
            word_pinyin1 = get_every_word_first(word)
            word_pinyin2 = get_all_pinying(word)
            # 拼音建立字典树
            self.trie[word] = word
            self.trie[word_pinyin1] = word_pinyin1
            self.trie[word_pinyin2] = word_pinyin2

    def search_prefix(self, prefix):
        return self.trie.values(prefix=prefix)

# 构建字典树
def build_all_trie(wordlist):
    # 字典树
    sug = Suggester()
    sug.update_trie(wordlist)
    # 映射数据集
    data = pd.DataFrame({"word": wordlist})
    # apply() 可以直接对DataFrame中元素进行逐元素遍历操作
    data['pinyin1'] = data['word'].apply(lambda x: get_every_word_first(x))
    data['pinyin2'] = data['word'].apply(lambda x: get_all_pinying(x))
    return sug, data

# 判断字符串只包含中文
def check_contain_chinese(check_str):
    flag = True
    for ch in check_str:
        if u'\u4e00' >= ch or ch >= u'\u9fff':
            flag =  False
    return flag

# 搜索提示查询
# 参数：字典树 映射数据集 搜索词；返回搜索提示词列表
def get_tips_word(sug, data, s):
    try:
        if len(s) > 0:
            # 判断输入是否只包含中文，若只有中文，则按中文查
            if check_contain_chinese(s) is True:
                # 查找前缀
                kk = sug.search_prefix(s)
                # isin()方法可以同时判断数据是否与多个值相等
                # result3包括 word(症状名) pinyin1(首字母) pinyin2(全拼)
                result3 = data[data['word'].isin(kk)]
                # result6只有 word
                result6 = list(set(result3['word']))
                return result6
            # 若不是只包含中文，转换为英文去查询
            else:
                s1=get_all_pinying(s)
                kk = sug.search_prefix(s1)
                result1 = data[data['pinyin1'].isin(kk)]
                result2 = data[data['pinyin2'].isin(kk)]
                result3 = data[data['word'].isin(kk)]
                result4 = pd.concat([result1, result2], ignore_index=True)
                result5 = pd.concat([result3, result4], ignore_index=True)
                # 输出结果
                result6 = list(set(result5['word']))
                return result6
        else:
            return
    except Exception as e:
        print("{0}".format(str(e)))
