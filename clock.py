这里是一个简单的Python程序来生成一个专注时钟:
python
import time

print("专注时钟")
print("规则:如果你专注工作25分钟,你将获得一个5分钟的休息时间!") 
print("在专注时间内请将手机等电子设备静音或关闭。")

work_min = 25     # 工作时间(分钟)
rest_min = 5      # 休息时间(分钟)

total_cycles = 3   # 总循环次数

for i in range(total_cycles): 
    print(f"第{i+1}个循环(共{total_cycles}个循环)")
    
    # 工作时间
    print(f"{work_min} 分钟专注工作开始!")
    work_start = time.time()
    time.sleep(work_min * 60)
    work_end = time.time()
    print(f"{work_min} 分钟专注工作结束!")
    
    # 休息时间
    print(f"{rest_min} 分钟休息时间开始!")
    rest_start = time.time()
    time.sleep(rest_min * 60)
    rest_end = time.time()
    print(f"{rest_min} 分钟休息时间结束!")

print("You did great! 所有的循环已经完成,你可以自由活动了。") 
print("希望这个专注时钟能够帮助你养成良好的工作习惯!")
