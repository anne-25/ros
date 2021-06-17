#include "ros/ros.h"
#include "std_msgs/String.h" // std_msgsのString型をインクルード
#include <sstream>

int main (int argc, char** argv)
{
  ros::init(argc, argv, "talker"); //　ノード名を宣言
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
  // パブリッシャの宣言 パブリッシャ= n.advertise<型名>(トピック名, キューサイズ)
  ros::Rate loop_rate(10); // プログラムの周期の宣言

  int count = 0;
  
  while (ros::ok())
  {
    std_msgs::String msg; // メッセージの型の宣言
    std::stringstream ss;
    ss << "hello world" << count;
    msg.data = ss.str();
    ROS_INFO("%s", msg.data.c_str());
    chatter_pub.publish(msg); // メッセージをパブリッシュする
    ros::spinOnce();
    loop_rate.sleep(); //　ループの周期の調整
    ++count;
  }

  return 0;
}
