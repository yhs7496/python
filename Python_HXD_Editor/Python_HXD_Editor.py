import sys;

while True:
    print("1.파일 열기, 2.색터 정보, 0.종료")
    info = input("번호를 입력해주세요: ")

    if info == "1":
        file_name = input("파일 이름 : ")
        try:
            f = open(file_name, "rb")
        except:
            print("File Error")

    if info == "2":
            sector_num = int(input("섹터 번호를 입력해주세요: "))
            start_sector = sector_num * 512
            f.seek(start_sector)
            print("offset(h) 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F")
            print("=========================================================")
            for line in range(32):
                data = f.read(16)
                offset = "%08X " % (line*16)
                hexs = [format(b, '02X') for b in data]
                asciis = [chr(b) if 15 < b < 127 else '.' for b in data]
                print(offset, *hexs,''.join(asciis))

    if info == "0":
        f.close()
        sys.exit()
