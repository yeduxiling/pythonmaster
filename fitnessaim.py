weight = 84.1
fat_rate = 0.213
fat_weight = weight * fat_rate
weight_aim = 75
fat_rate_aim = 0.18
fat_weight_aim = weight_aim * fat_rate_aim

print("距离目标体重还需要减重：", weight-weight_aim,"kg")
print("还需要减掉", fat_rate - fat_rate_aim,"的体脂率")
print("也就是要减掉",fat_weight - fat_weight_aim,"kg的脂肪")
