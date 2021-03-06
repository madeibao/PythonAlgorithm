import numpy as np

file1 = './test/embedding.txt'   # 自定义一个文件夹。
word2vec = np.random.uniform(-0.01, 0.01, [3, 4])
print(word2vec)
with open(file1, 'w', encoding='utf-8') as wf:
    for i in range(0, len(word2vec)):
        for j in range(0, 4):
            # print(word2vec[i][j], end=" ")
            wf.write(str(word2vec[i][j])+" ")
        wf.write("\n")





numpy的格式为：
[[-0.00241726  0.0086579  -0.00388996  0.00063193]
 [-0.00339615 -0.00259244 -0.00603745 -0.00927019]
 [ 0.00360275  0.00759145  0.00263766  0.00436169]]

txt文件中的存储的格式为：
-0.0024172629724766035 0.008657902909502564 -0.003889957616653155 0.0006319302942007447 
-0.0033961525668787292 -0.0025924400979527376 -0.006037449929704693 -0.009270185629651357 
0.003602750634543645 0.007591446301600939 0.002637659518584053 0.004361689966719026 
