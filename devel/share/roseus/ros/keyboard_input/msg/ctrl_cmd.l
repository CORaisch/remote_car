;; Auto-generated. Do not edit!


(when (boundp 'keyboard_input::ctrl_cmd)
  (if (not (find-package "KEYBOARD_INPUT"))
    (make-package "KEYBOARD_INPUT"))
  (shadow 'ctrl_cmd (find-package "KEYBOARD_INPUT")))
(unless (find-package "KEYBOARD_INPUT::CTRL_CMD")
  (make-package "KEYBOARD_INPUT::CTRL_CMD"))

(in-package "ROS")
;;//! \htmlinclude ctrl_cmd.msg.html


(defclass keyboard_input::ctrl_cmd
  :super ros::object
  :slots (_steer _throttle ))

(defmethod keyboard_input::ctrl_cmd
  (:init
   (&key
    ((:steer __steer) 0.0)
    ((:throttle __throttle) 0.0)
    )
   (send-super :init)
   (setq _steer (float __steer))
   (setq _throttle (float __throttle))
   self)
  (:steer
   (&optional __steer)
   (if __steer (setq _steer __steer)) _steer)
  (:throttle
   (&optional __throttle)
   (if __throttle (setq _throttle __throttle)) _throttle)
  (:serialization-length
   ()
   (+
    ;; float64 _steer
    8
    ;; float64 _throttle
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _steer
       (sys::poke _steer (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _throttle
       (sys::poke _throttle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _steer
     (setq _steer (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _throttle
     (setq _throttle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get keyboard_input::ctrl_cmd :md5sum-) "78f0fb3ce40503c7b89d4e7933ccfc59")
(setf (get keyboard_input::ctrl_cmd :datatype-) "keyboard_input/ctrl_cmd")
(setf (get keyboard_input::ctrl_cmd :definition-)
      "# steering value: [-1,1] = [full-left,full-right]
float64 steer

# throttle value: [-1,1] = [full-backward,full-forward]
float64 throttle

")



(provide :keyboard_input/ctrl_cmd "78f0fb3ce40503c7b89d4e7933ccfc59")


