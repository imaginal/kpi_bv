gcc -m32 -no-pie -fno-stack-protector target.c
checksec --file=a.out
