; Auto-generated. Do not edit!


(cl:in-package keyboard_controller-msg)


;//! \htmlinclude ctrl_cmd.msg.html

(cl:defclass <ctrl_cmd> (roslisp-msg-protocol:ros-message)
  ((steer
    :reader steer
    :initarg :steer
    :type cl:float
    :initform 0.0)
   (throttle
    :reader throttle
    :initarg :throttle
    :type cl:float
    :initform 0.0))
)

(cl:defclass ctrl_cmd (<ctrl_cmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ctrl_cmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ctrl_cmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name keyboard_controller-msg:<ctrl_cmd> is deprecated: use keyboard_controller-msg:ctrl_cmd instead.")))

(cl:ensure-generic-function 'steer-val :lambda-list '(m))
(cl:defmethod steer-val ((m <ctrl_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader keyboard_controller-msg:steer-val is deprecated.  Use keyboard_controller-msg:steer instead.")
  (steer m))

(cl:ensure-generic-function 'throttle-val :lambda-list '(m))
(cl:defmethod throttle-val ((m <ctrl_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader keyboard_controller-msg:throttle-val is deprecated.  Use keyboard_controller-msg:throttle instead.")
  (throttle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ctrl_cmd>) ostream)
  "Serializes a message object of type '<ctrl_cmd>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'steer))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'throttle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ctrl_cmd>) istream)
  "Deserializes a message object of type '<ctrl_cmd>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'steer) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'throttle) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ctrl_cmd>)))
  "Returns string type for a message object of type '<ctrl_cmd>"
  "keyboard_controller/ctrl_cmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ctrl_cmd)))
  "Returns string type for a message object of type 'ctrl_cmd"
  "keyboard_controller/ctrl_cmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ctrl_cmd>)))
  "Returns md5sum for a message object of type '<ctrl_cmd>"
  "78f0fb3ce40503c7b89d4e7933ccfc59")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ctrl_cmd)))
  "Returns md5sum for a message object of type 'ctrl_cmd"
  "78f0fb3ce40503c7b89d4e7933ccfc59")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ctrl_cmd>)))
  "Returns full string definition for message of type '<ctrl_cmd>"
  (cl:format cl:nil "# steering value: [-1,1] = [full-left,full-right]~%float64 steer~%~%# throttle value: [-1,1] = [full-backward,full-forward]~%float64 throttle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ctrl_cmd)))
  "Returns full string definition for message of type 'ctrl_cmd"
  (cl:format cl:nil "# steering value: [-1,1] = [full-left,full-right]~%float64 steer~%~%# throttle value: [-1,1] = [full-backward,full-forward]~%float64 throttle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ctrl_cmd>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ctrl_cmd>))
  "Converts a ROS message object to a list"
  (cl:list 'ctrl_cmd
    (cl:cons ':steer (steer msg))
    (cl:cons ':throttle (throttle msg))
))
