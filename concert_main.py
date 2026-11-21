import time

performers = [
    {
        "name": "SOOBIN HOANG SON",
        "songs": "Không Xi Nhê, Giá Như, Dancing in The Dark, Vinh Quang Đang Chờ Ta",
        "fee": "$50,000",
        "time": "22:00 - 22:55"
    },
    {
        "name": "7UPPERCUTS",
        "songs": "Yêu, Trốn Tìm, Bài Ca Con Gà, DOPAMINE",
        "fee": "$5,000",
        "time": "19:00 - 19:55"
    },
    {
        "name": "PHUNG KHANH LINH",
        "songs": "Em Đau, Hôm Nay Tôi Buồn, Anh Là Thằng Tồi, Cảm Ơn Người Đã Thức Cùng Tôi",
        "fee": "$30,000",
        "time": "20:00 - 20:55"
    },
    {
        "name": "DAM VINH HUNG",
        "songs": "Xin Lỗi Tình Yêu, Bình Minh Sẽ Mang Em Đi, Tình Ơi Xin Ngủ Yên, Nếu Như Ta Chẳng Còn",
        "fee": "$40,000",
        "time": "21:00 - 21:45"
    }
]

while True:
    lineup_str = " - ".join([p["name"] for p in performers])
    
    print(f"""
                                WELCOME TO

                        ♫★YEAR END FESTIVAL 2026★♫
                            CIS COMPANY © 2026
                            
        {lineup_str}
""")
    
    print("""
                         ------------------------------

                    30 DEC 2026 | START FROM 19.00 - 23.00

                    NONE STADIUM 123 ANYWHERE ST., ABC CITY

""")
    print("    |                    |                      |                   |")
    print("    |  1 - CHECK TICKET  |  2 - GET TICKET NOW  |     3 - STAFF     |")
    print("    |                    |                      |                   |")
    
    print()
    
    choice = input("ENTER NUMBER TO SELECT AN OPTION: ")
    
    if choice == "1":
        
        print("\n========== CHECK TICKET ==========")

    elif choice == "2":
        print("GET TICKET NOW")

    elif choice == "3":
        print("\n========== STAFF LOGIN ==========")

        password = input("ENTER STAFF PASSWORD: ")

        if password == "tton-dangcaps1tg":
            print("\nACCESS GRANTED!")
            print("WELCOME TO STAFF MANAGEMENT SYSTEM")
        
            while True:
                print("""
========== PERFORMER MANAGEMENT ==========
1 - VIEW LINEUP DETAILS (Songs, Fee, Time)
2 - ADD NEW PERFORMER
3 - REMOVE PERFORMER
4 - EDIT PERFORMER INFORMATION
5 - LOGOUT / RETURN TO MAIN MENU
==========================================
""") 
                staff_choice = input("SELECT STAFF OPTION: ")
                
                if staff_choice == "1":
                    print("\n--- CURRENT LINEUP DETAILS ---")
                    for i,p in enumerate(performers, 1):
                        print(f"{i}, ARTIST: {p['name']}")
                        print(f"   SONGS : {p['songs']}")
                        print(f"   FEE : {p['fee']}")
                        print("-" * 35)
                    time.sleep(2)