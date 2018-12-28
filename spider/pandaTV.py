from urllib import request
import re
class Spider():
    mydict = {}
    num = 1
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>' # 加上小括号就可以提取中间的内容了 ?在小括号的里面和外面也是不一样的
    num_pattern = '<span class="video-number">(.*?)</span>'
    name_pattern = '<span class="video-nickname" title="(.*?)">'

    def __fetch_html(self):
        r = request.urlopen(self.__class__.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        return html

    def __analysis(self, html):
        list_info = re.findall(self.__class__.root_pattern, html)
        for i in list_info:
            name = re.findall(self.__class__.name_pattern, i)
            num = re.findall(self.__class__.num_pattern, i)
            self.__class__.mydict[str(name[0])] = str(num[0])
        # print(self.__class__.mydict)
    
    def __show(self):
        # print(self.__class__.mydict)
        for i in self.__class__.mydict:
            print('第' + str(self.__class__.num) + '名是：' + i[0] + '--------' + str(i[1]))
            self.__class__.num += 1
    
    def __refine(self):
        dict_new = {}
        for name, value in self.__class__.mydict.items():
            num = re.findall('\d+[\.\d]*', value)
            if '万' in value:
                num = float(num[0]) * 10000
            else:
                num = float(num[0])
            dict_new[name] = float(num)
        self.__class__.mydict.update(dict_new)

    def __sort(self):
        # 因为字典无序，此处sorted将dict转为list
        self.__class__.mydict = sorted(self.__class__.mydict.items(), key=lambda item: item[1], reverse=True)

    def go(self):
        html = self.__fetch_html()
        self.__analysis(html)
        self.__refine()
        self.__sort()
        self.__show()
spider = Spider()
spider.go()