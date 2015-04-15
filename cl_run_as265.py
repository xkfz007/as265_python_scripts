#!/usr/bin/python
import os
import sys
import lib
encoder_id="as265"
enc=lib.Encoder_prop(encoder_id)

param_list=lib.get_default_param_list()
#param_list['encder_exe']=lib.get_encoder_exe()
#param_list['output_path']="F:/encoder_test_output/as265_output/"
#param_list['input_path']="E:/sequences/"
#param_list['frame_num_to_encode']=100

#param_list['input_filename']="BlowingBubbles_416x240_50.yuv"
#seq_name="BlowingBubbles_416x240_50"
#param_list['eRcType']=1

cons="tmp_cons.log"
#if len(sys.argv)> 1:
cons,extra_cls=lib.configure_param(enc,param_list)

cmd_line=lib.get_full_cmd(enc,param_list)
cmd_line+=" "+extra_cls

if lib.determin_sys()=="cygwin":
  cmd_line+=(" 2>&1 |tee -a "+cons)
  pf=open(cons,"w")
  print >>pf,"%s" %cmd_line
  pf.close()

os.system(cmd_line)

