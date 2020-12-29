2.4 使用Itertools生成排列和组合¶
对于排列，元素的顺序很重要，因此(“sam”、“devon”)表示与(“devon”、“sam”)不同的配对，这意味着它们都将包含在列表中。




import itertools
friends = ['BeiJing', 'ShangHai', 'ChongQing', 'GuangZhou']
print(list(itertools.permutations(friends, r=2)))



# 下面是全排列
[('BeiJing', 'ShangHai'), ('BeiJing', 'ChongQing'), ('BeiJing', 'GuangZhou'), 
('ShangHai', 'BeiJing'), ('ShangHai', 'ChongQing'), ('ShangHai', 'GuangZhou'), 
('ChongQing', 'BeiJing'), ('ChongQing', 'ShangHai'), ('ChongQing', 'GuangZhou'),
 ('GuangZhou', 'BeiJing'), ('GuangZhou', 'ShangHai'), ('GuangZhou', 'ChongQing')]



# 下面是全组合。
[('BeiJing', 'ShangHai'), ('BeiJing', 'ChongQing'), ('BeiJing', 'GuangZhou'), ('ShangHai', 'ChongQing'), ('ShangHai', 'GuangZhou'), ('ChongQing', 'GuangZhou')]
