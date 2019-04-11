// Generated by gencpp from file keyboard_controller/ctrl_cmd.msg
// DO NOT EDIT!


#ifndef KEYBOARD_CONTROLLER_MESSAGE_CTRL_CMD_H
#define KEYBOARD_CONTROLLER_MESSAGE_CTRL_CMD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace keyboard_controller
{
template <class ContainerAllocator>
struct ctrl_cmd_
{
  typedef ctrl_cmd_<ContainerAllocator> Type;

  ctrl_cmd_()
    : steer(0.0)
    , throttle(0.0)  {
    }
  ctrl_cmd_(const ContainerAllocator& _alloc)
    : steer(0.0)
    , throttle(0.0)  {
  (void)_alloc;
    }



   typedef double _steer_type;
  _steer_type steer;

   typedef double _throttle_type;
  _throttle_type throttle;





  typedef boost::shared_ptr< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> const> ConstPtr;

}; // struct ctrl_cmd_

typedef ::keyboard_controller::ctrl_cmd_<std::allocator<void> > ctrl_cmd;

typedef boost::shared_ptr< ::keyboard_controller::ctrl_cmd > ctrl_cmdPtr;
typedef boost::shared_ptr< ::keyboard_controller::ctrl_cmd const> ctrl_cmdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::keyboard_controller::ctrl_cmd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace keyboard_controller

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'keyboard_controller': ['/home/ubuntu/catkin_ws/src/keyboard_controller/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "78f0fb3ce40503c7b89d4e7933ccfc59";
  }

  static const char* value(const ::keyboard_controller::ctrl_cmd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x78f0fb3ce40503c7ULL;
  static const uint64_t static_value2 = 0xb89d4e7933ccfc59ULL;
};

template<class ContainerAllocator>
struct DataType< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "keyboard_controller/ctrl_cmd";
  }

  static const char* value(const ::keyboard_controller::ctrl_cmd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# steering value: [-1,1] = [full-left,full-right]\n"
"float64 steer\n"
"\n"
"# throttle value: [-1,1] = [full-backward,full-forward]\n"
"float64 throttle\n"
;
  }

  static const char* value(const ::keyboard_controller::ctrl_cmd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.steer);
      stream.next(m.throttle);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ctrl_cmd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::keyboard_controller::ctrl_cmd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::keyboard_controller::ctrl_cmd_<ContainerAllocator>& v)
  {
    s << indent << "steer: ";
    Printer<double>::stream(s, indent + "  ", v.steer);
    s << indent << "throttle: ";
    Printer<double>::stream(s, indent + "  ", v.throttle);
  }
};

} // namespace message_operations
} // namespace ros

#endif // KEYBOARD_CONTROLLER_MESSAGE_CTRL_CMD_H
