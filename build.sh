java -jar ../target/scala-2.12/millfork.jar -t nes_nrom -Wall -G mesen -Wextra-comparisons -s -fsource-in-asm -fsubroutine-extraction -fdangerous-optimizations -finline -fipo -fillegals main.mfk -O$1
