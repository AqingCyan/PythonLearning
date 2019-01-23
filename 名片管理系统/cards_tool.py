"""
保存所有程序功能函数
1.将对名片的新增、查询、修改、删除等功能封装在不同函数中
"""
# 存储名片信息的列表
card_list = [{
    "name": "Aqing",
    "phone": "13088974963",
    "qq": "1929667379",
    "email": "xuekaiqi@creatshare.com"
}]


def show_menu():
    """显示菜单"""
    print("*" * 60)
    print("欢迎使用【名片管理系统】V1.0".center(50, " "))
    print("")
    print("1.新增名片".center(50, " "))
    print("2.显示全部".center(50, " "))
    print("3.搜索名片".center(50, " "))
    print("")
    print("0.退出系统".center(50, " "))
    print("*" * 60)


def new_card():
    """新增名片"""
    print("新增名片")
    # 1.提示用户输入详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")
    # 2.根据输入信息建立名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str
                 }
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4，提示用户添加成功
    print("添加%s成功" % card_dict["name"])


def show_all():
    """显示所有名片"""
    print("-" * 60)
    print("显示所有名片")

    # 判断是否有名片记录，如果没有就提示然后直接返回
    if len(card_list) == 0:
        print("当前数据中没有任何信息，请使用名片添加功能！")
        return

    # 打印表头与分割线
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 60)
    # 循环遍历列表依次输出名片信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))


def search_card():
    """搜索名片"""
    print("搜索名片")
    # 1.提示用户输入要查询的姓名
    find_name = input("请输入要搜索的姓名：")
    # 2.遍历名片列表，查询要搜索的名片，如果没找到则提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("-" * 50)
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
            print("-" * 50)
            # 针对查询到的名片要进行的进一步操作
            deal_card(card_dict)
            break
    else:
        print("未找到您输入的姓名：%s" %find_name)

def deal_card(find_dict):
    """
    对查询到的名片进行操作
    :param find_dict:查询到的名片字典信息
    :return:返回空值，跳到开始菜单
    """
    action_str = input("请选择要执行的操作 【1】修改名片 【2】删除名片 【0】返回上级菜单：")
    if action_str == "1":
        find_dict["name"] = input_info(find_dict["name"], "姓名[不修改此项则直接回车]：")
        find_dict["phone"] = input_info(find_dict["phone"], "电话[不修改此项则直接回车]：")
        find_dict["qq"] = input_info(find_dict["qq"], "QQ[不修改此项则直接回车]：")
        find_dict["email"] = input_info(find_dict["email"], "邮箱[不修改此项则直接回车]：")
        print("修改成功")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除成功")
    else:
        return

def input_info(dict_value, tip_message):
    """
    控制修改名片信息
    :param dict_value:字典中原有值
    :param tip_message:输入的新值
    :return:如果用户输入了内容就返回新值，若未输入则返回旧值
    """
    # 1.提示用户输入内容
    result_str =  input(tip_message)
    # 2.针对用户输入内容进行判断，输入了则直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3、没有输入，则返回原值
    else:
        return dict_value