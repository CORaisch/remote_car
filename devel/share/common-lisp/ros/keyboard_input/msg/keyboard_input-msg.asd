
(cl:in-package :asdf)

(defsystem "keyboard_input-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ctrl_cmd" :depends-on ("_package_ctrl_cmd"))
    (:file "_package_ctrl_cmd" :depends-on ("_package"))
  ))