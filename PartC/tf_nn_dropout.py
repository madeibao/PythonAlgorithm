inputs = tf.reshape(np.array(range(50), dtype=np.float32), [5, 10])  #原始数据
keep_prob = 0.5                                          #参数 
outputs = tf.nn.dropout(inputs, keep_prob)                    #操作后的数据

with tf.Session() as sess:
	tf.global_variables_initializer().run()
	print(sess.run(inputs))
	print(sess.run(outputs))



# 通过丢弃率，来保持一定的结果值。
[[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]
 [10. 11. 12. 13. 14. 15. 16. 17. 18. 19.]
 [20. 21. 22. 23. 24. 25. 26. 27. 28. 29.]
 [30. 31. 32. 33. 34. 35. 36. 37. 38. 39.]
 [40. 41. 42. 43. 44. 45. 46. 47. 48. 49.]]
 
[[ 0.  2.  0.  0.  0. 10. 12. 14. 16.  0.]
 [ 0. 22. 24. 26. 28.  0. 32. 34.  0.  0.]
 [40.  0. 44. 46.  0.  0. 52.  0. 56. 58.]
 [ 0. 62. 64. 66. 68.  0.  0. 74.  0.  0.]
 [80.  0. 84. 86.  0.  0. 92. 94. 96.  0.]]
