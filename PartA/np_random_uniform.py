import numpy as np

print(np.random.uniform(-0.01, 0.01, [5, 20]))
print(np.random.uniform(-0.01, 0.01, [5, ]))

"""
输出结果为

[[-9.53646754e-03 -6.02886454e-03  4.20582999e-03  2.89456042e-04
   4.04231061e-03  5.74625826e-03 -7.69020443e-03  8.07618084e-03
  -5.53703364e-03  8.07052515e-03  7.57287865e-03  9.43560084e-03
   2.15824977e-03  2.10249423e-03 -6.40166520e-03  3.78450333e-03
  -3.94897321e-03 -8.70000220e-03 -5.11837200e-03 -7.99380044e-03]
 [-8.66994765e-04 -4.53739998e-03  2.27302693e-03  1.51073104e-03
   2.39174719e-03  1.08911060e-03  9.61006806e-03 -6.72812609e-03
   6.47883770e-03  5.49402778e-03 -8.60700467e-03  9.61498855e-03
  -6.97291349e-04  8.66738195e-03 -3.52396399e-03  1.16638929e-03
   2.85750255e-03 -4.82669604e-03  1.32409079e-03  1.13592684e-03]
 [ 8.82744596e-03  8.75728416e-03  5.34933303e-03  7.97283552e-03
   3.82271182e-03 -9.62697845e-03 -4.43987799e-03  3.37162606e-03
   1.49419182e-03  8.28554199e-03  3.55530096e-03  5.61805668e-03
   9.96365468e-03  7.77736740e-03 -3.27610460e-04  5.85579426e-03
   1.30881443e-03  7.34552136e-03  8.93026107e-03  8.89183830e-04]
 [-7.61019033e-03  1.03874154e-03  9.36632911e-03  4.07373181e-03
  -1.16288127e-03 -2.67748852e-03 -5.13807511e-03 -3.94582558e-03
   4.12080335e-03 -5.48174865e-03 -7.28328538e-03  8.79440921e-03
   4.50731545e-03 -1.36796709e-03  9.73092898e-03 -4.58498509e-03
   1.04341829e-03  4.04184761e-03 -2.67599645e-03 -6.66336094e-03]
 [ 3.70553895e-03  7.91900738e-03  6.38330707e-03  1.76752972e-03
   7.34545354e-03  4.86964638e-04  8.64421784e-03  7.19867348e-03
  -9.28461526e-03 -9.58267995e-03  7.50424086e-04 -5.08560147e-03
  -2.64438435e-03  3.80117901e-03 -5.12933887e-03 -7.98624665e-05
  -9.41665106e-03  7.16658369e-03 -8.70236765e-03 -2.79090255e-03]]



另一个结果：
[-0.00228719  0.00753145  0.00623294  0.00701429  0.00628767]


"""


