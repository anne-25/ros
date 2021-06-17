#!/usr/bin/env python
# coding: UTF-8

import rospy
from std_msgs.msg import Int64 #std_msgsのInt64型をインポート

def callback(data): #コールバック関数
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    #ノード名を宣言
    rospy.Subscriber("chatter", Int64, callback)
    #サブスクライバを宣言 rospy.Subscriber(トピック名, 型名, コールバック関数)
    rospy.spin()
    #メッセージをサブスクライブしたときにコールバック関数を実行

if __name__ == '__main__':
    listener()
