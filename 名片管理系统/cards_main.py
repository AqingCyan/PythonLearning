"""
保存主程序功能代码
1.程序入口
2.每一次启动程序都通过main启动
"""
import cards_tool

# 使用一直循环的操作使其能一直在选择操作界面
while True:
    cards_tool.show_menu()  # 功能菜单显示
    # 提示用户输入
    action_str = input("请选择希望执行的操作：")  # 返回值就是我们输入的内容

    # 1、2、3对应操作
    if action_str in ["1", "2", "3"]:
        print("您选择的操作是：【%s】" % action_str)
        # 新增名片
        if action_str == "1":
            cards_tool.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tool.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tool.search_card()
    # 0 退出系统
    elif action_str == "0":
        print("您选择了%s，欢迎再次使用" % action_str)
        break  # 打破循环，退出操作界面
    # 其他操作
    else:
        print("您输入的是%s，操作有误" % action_str)
