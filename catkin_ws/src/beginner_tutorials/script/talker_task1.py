#!/usr/bin/env python
# coding: UTF-8

import rospy
from std_msgs.msg import Int64 #std_msgsのInt64型をインポート

def talker():
    pub = rospy.Publisher('chatter', Int64, queue_size = 10)
    #パブリッシャの宣言　パブリッシャ＝ rospy.Publisher(トピック名, 型名, キューサイズ)
    rospy.init_node('talker', anonymous=True) #ノード名を宣言
    r = rospy.Rate(10) #プログラムの周期を宣言
    while not rospy.is_shutdown():
        str =  rospy.get_time()
        #メッセージの型の宣言を行わなければならない場合もある 例：str = String()
        rospy.loginfo(str)
        pub.publish(str) #メッセージをパブリッシュする
        r.sleep() #ループの周期を調整

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
