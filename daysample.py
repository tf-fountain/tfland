#*******************************************************************************
#
# DAYSAMPLE
#
#　　引数によって出力を変える　／　0,1,2 以外は無指定と同じ
#　　　0　：　日付のみ （無指定の場合も同様）
#　　　1　：　[朝]()　を付加
#　　　2　：　[朝](か)　と改行を付加
#
#
#    2019/08/01 Fri by T.Fujioka　　オプション（引数）で出力を変えるようにした
#
#!/usr/bin/env python
# -*- coding: utf8 -*-
#*******************************************************************************

## 
import sys
import datetime 
import locale
import calendar

## DATA .....
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

days = [31,28,31,30,31,30,   31,31,30,31,30,31]

args = sys.argv   # コマンドライン引数
opt = 0

line = '-------------------------------------------------------------------------------\n'


## ********** 引数（0-2）で 出力フォーマットを決定
if len(args) > 1:
    opt = args[1]  ## 0,1,2 （これら以外は 0 と同じ）


## 入力 （年）
year_in   = input('year  ? = ')

year   = int(year_in)
outfile = 'sample%d.day.txt' % (year)
print(outfile)

## うるう年チェック
leap = calendar.isleap(year)

## 出力ファイル　OPEN
with open(outfile, mode='w') as f:


#   ######  LOOP  START !!!#  
    for month in range(0,12):

#       #### 毎月のタイトル出力
        f.write('\f' + '\n')
        f.write(line)

        month_s = months[month]
        title =  '\t' + month_s + '\t' + year_in + '\n'
#       print (title)

        f.write(title)
        f.write(line)
        f.write(line)


#       ## 毎日の明細行（／月）の処理
    
        end =  days[month]+1

#       ## うるう年の2月は1日多く処理する
        if leap == True and month==1:
            end = end +1  

#       ######  LOOP  START  !!!
        for day in  range( 1, end):
            dt = datetime.datetime(year, month+1, day)
            youbi = dt.strftime('%a')
    
            dayline = year_in+'/'+'{:02}'.format(month+1)+'/'+'{:02}'.format(day)+' '+youbi+'\n'
#           print (dayline)
 
            f.write(dayline)

            if opt=='2': 
                f.write('\n')
                f.write('\n')
                f.write('\n')
            
            if opt=='1':
                f.write('　[朝]()\n')
                f.write('　[昼]()\n')
                f.write('　[夜]()\n')
                f.write('　[酒]\n')

            if opt=='2':
                f.write('　[朝](か)\n')
                f.write('　[昼](か)\n')
                f.write('　[夜](か)\n')
                f.write('　[酒]\n')
                f.write('\n')
                f.write('\n')

            f.write(line)
#           print(day)

#       ######  LOOP  END  !!!


#   ######  LOOP  END  !!!

print('%d 年の SAMPLE.DAY を 出力しました。' % (year))

