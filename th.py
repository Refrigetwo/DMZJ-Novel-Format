var = 1
while var == 1 :
    fname=input('请输入转换的文件名：')
    with open(fname + '.txt', "rt",encoding='utf8') as fin:
        with open("o.txt", "at",encoding='utf8') as fout:
            for line in fin:
                fout.write(line.replace('<br/>','').replace('<br />', '')\
                    .replace('&nbsp;',' ').replace('&mdash;','——')\
                        .replace('&hellip;','…').replace('&bull;','·'))