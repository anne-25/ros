#include "ros/ros.h"
#include "std_msgs/String.h" // std_msgsのString型をインクルード

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg -> data.c_str());
}

int main (int argc, char** argv)
{
  ros::init(argc, argv, "listener"); // ノード名の宣言
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
  // サブスクライバの宣言 サブスクライバ = n.subscribe(トピック名, キューサイズ, コールバック関数);
  ros::spin();
  return 0;
}
