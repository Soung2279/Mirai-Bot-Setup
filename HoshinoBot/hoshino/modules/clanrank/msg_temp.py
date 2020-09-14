# 对应中文信息列表
msg_dic = {
    'clan_name':'公会名称',
    'rank':'公会排名',
    'damage':'分数',
    'boss': 'BOSS进度',# 需要调用函数，特殊处理
    'index':'信息编号', # 特殊处理
    'leader_name': '会长名',
    #'member_num':'总人数', # v0.1.5适配查询网站，不再返回人数信息 
    'ts':'更新时间', # 预先处理
    'leader_viewer_id':"会长UID",
    'full':'全部查询结果：' # 预先处理
}

# 常用查询模板列表
# 注意full/ts由于其特殊性质，会被预先处理，不会收到位置影响
# 每日排名推送
daily_push_list = [
    'clan_name','rank','damage'
]

# 查询会长UID
leader_id_query_list = [
    'full','clan_name','leader_name','leader_viewer_id','rank','index','boss'
]
# 本公会查询
self_clan_query_list = [
    'clan_name','leader_name','ts','rank','damage','boss'
]

# 分数线模板
line_list = [
    'rank','damage','boss'
]