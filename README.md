# flowMoniter

### /cpu Get
return
{
        "memory": 内存使用情况,
        "gpu": gpu[0]的占用率 ,
        "cpu": cpu占用率
    } 
### /speed Get
[
                {
                    "key": 网络类型,
                    "in": 下行速率,
                    "out": 上行速率
                }
]
sum需要前端轮询speed的api（间隔1s）
### /speed/sum Get
[

                {
                    "key": 网络类型,
                    "in": 下行总量,
                    "out": 上行总量
                }
]

all文件夹下
pcaps下放有pcap包，包名即获取的时间
tools里面deletefile目前可以独立运行，自动删除超出10s的pcap包

