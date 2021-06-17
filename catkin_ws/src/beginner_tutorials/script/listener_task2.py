#!/usr/bin/env python
# coding: UTF-8

import rospy
from std_msgs.msg import String #std_msgsのString型をインポート
from std_msgs.msg import Float32,Int64

def callback_int64(data): #コールバック関数
    pass

def callback_float32(data):
    pass

def listener():
    rospy.init_node('listener', anonymous=True)
    #ノード名を宣言
    x=rospy.Subscriber("/chatter/int64", Int64, callback_int64)

    print x
    rospy.Subscriber("/chatter/float32", Float32, callback_float32)
    #サブスクライバを宣言 rospy.Subscriber(トピック名, 型名, コールバック関数)
    rospy.spin()
    #メッセージをサブスクライブしたときにコールバック関数を実行

if __name__ == '__main__':
    listener()
