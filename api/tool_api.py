import os
import re


class DataProcess():

    # 获取脚本全路径
    def getHqlScriptPaths(self, dir):
        scriptPaths = []
        walk = os.walk(dir)
        print(type(walk))
        for root, dirs, files in os.walk(dir):
            # root代表根目录
            # dirs代表根目录下的目录名称
            # files代表根目录下文件名称
            for fileName in files:
                if fileName.endswith(".hql"):
                    scriptPath = os.path.join(root, fileName)
                    print(fileName)
                    scriptPaths.append((root, fileName))
        return scriptPaths

    def getFmtMsg(self, color, msg):
        msg = '<html><div style= "color:{}">{}</div></html>'.format(color, msg)
        return msg

    # 脚本解析,获取依赖表
    def sciptAnalysis(self, scriptPath, ourFile):
        # with open(scriptPath, 'r', encoding='UTF-8') as f:
        #     lines = f.readlines()
        #     tokens = sql_metadata.get_query_tokens(''.join(lines))
        #     tables = sql_metadata.get_query_tables(''.join(lines))
        #     columns = sql_metadata.get_query_columns(''.join(lines))
        res = set()
        dir = scriptPath[0]
        scriptName = scriptPath[1]
        with open(os.path.join(dir, scriptName), 'r', encoding="UTF-8") as f:
            # with open(scriptPath, 'r', encoding="UTF-8") as f:
            lines = ''.join(f.readlines()).replace("\n", "").upper()
        # searchObj = re.search(r'(FROM|JOIN)[\s]+[\S]+', lines, re.M | re.I)
        # 分两次正则，尬尬
        # findall = re.findall(r'(FROM|JOIN)[\s]+([\S]+)', lines)
        fromAll = re.findall(r'FROM[\s]+([\S]+)', lines)
        joinAll = re.findall(r'JOIN[\s]+([\S]+)', lines)
        findall = fromAll + joinAll
        for tableName in findall:
            tableName = re.sub("\${[\S]+}\.", "", tableName)
            print(tableName)
            res.add(tableName)
        print(','.join(res))
        # 写入excel
        with open(ourFile, 'a') as f:
            f.write(scriptName.replace(".hql", "") + "," + '|'.join(res) + "\n")
        return
