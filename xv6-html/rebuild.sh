#!/bin/sh
#
# rebuild.sh: rebuild hypertext with the previous context.
#
# Usage:
#	% sh rebuild.sh
#
cd /Users/takuo/xv6 && GTAGSCONF=':skip=HTML/,HTML.pub/,tags,TAGS,ID,y.tab.c,y.tab.h,gtags.files,cscope.files,cscope.out,cscope.po.out,cscope.in.out,SCCS/,RCS/,CVS/,CVSROOT/,{arch}/,autom4te.cache/,*.orig,*.rej,*.bak,*~,#*#,*.swp,*.tmp,*_flymake.*,*_flymake:langmap=c\:.c.h,yacc\:.y,asm\:.s.S,java\:.java,cpp\:.c++.cc.hh.cpp.cxx.hxx.hpp.C.H,php\:.php.php3.phtml:script_alias=/cgi-bin/:ncol#4:tabs#8:normal_suffix=html:gzipped_suffix=ghtml:' htags -sanow
