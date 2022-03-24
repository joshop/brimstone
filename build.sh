java -jar ../target/scala-2.12/millfork.jar -t nes_cnrom -Wextra-comparisons -s -fsource-in-asm -fsubroutine-extraction -finline -fipo -fillegals main.mfk -O$1
