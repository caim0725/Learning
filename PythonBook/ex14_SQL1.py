import sqlite3
#SQL語法都用大寫來撰寫命令句
conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()#cursor()類似handler

cur.execute('DROP TABLE IF EXISTS Tracks ')#DROP TABLE 刪除已存在的TABLE
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
#設定colum的名稱和型態(事前就要嚴格規範好)
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',#(?, ?)表示想寫入的值再下一行
   ( 'Thunderstruck', 20 ) )
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',
   ( 'My Way', 15 ) )
conn.commit()

print 'Tracks:'
cur.execute('SELECT title, plays FROM Tracks')#SELECT是檢索特定TABLE From database
#SELECT * FROM Tracks WHERE title = 'My Way' //*表示將Tracks中所有符合後面WHERE定義的TABLE都回傳
#SELECT title,plays FROM Tracks ORDER BY title //ORDER指令可以排序
#DELETE FROM Tracks WHERE title = 'My Way'  // 刪除表格的內容
#UPDATE Tracks SET plays = 16 WHERE title = 'My Way' //更新表格的值
for row in cur :#此時的cur可以做迴圈的動作
    print row

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
cur.close()