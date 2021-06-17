#!/usr/bin/env python
# coding: UTF-8

import rospy
from std_msgs.msg import Int64 #std_msgsのInt64型をインポート
from std_msgs.msg import Float32

def talker():
    pub1 = rospy.Publisher('/chatter/int64', Int64, queue_size = 10)
    pub2 = rospy.Publisher('/chatter/float32', Float32, queue_size = 10)
    #パブリッシャの宣言　パブリッシャ＝ rospy.Publisher(トピック名, 型名, キューサイズ)
    rospy.init_node('talker', anonymous=True) #ノード名を宣言
    r = rospy.Rate(100) #プログラムの周期を宣言
    while not rospy.is_shutdown():
        int =  3000
        float = 1.1
        #メッセージの型の宣言を行わなければならない場合もある 例：str = String()
        rospy.loginfo(int)
        rospy.loginfo(float)
        pub1.publish(int) #メッセージをパブリッシュする
        pub2.publish(float)
        r.sleep() #ループの周期を調整

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
