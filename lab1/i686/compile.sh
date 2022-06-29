gcc -m32 -march=i686 -no-pie -fno-stack-protector target.c
checksec --file=a.out
