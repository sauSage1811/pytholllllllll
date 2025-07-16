import requests

while(True):

    
        SBD = input("📋 Nhập Số Báo Danh (SBD) của bạn (hoặc 'exit' để thoát): ").strip()
        if SBD == "exit":
            print("👋 Tạm biệt!")
            break
        url = "https://s6.tuoitre.vn/api/diem-thi-thpt.htm"
        params = {
        "sbd": SBD,
        "year": "2025"
        }

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "vi,vi-VN;q=0.9",
            "origin": "https://tuoitre.vn",
            "referer": "https://tuoitre.vn/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            if data["success"] and data["total"] > 0:
                diem_data = data["data"][0]
                diem_mon = {
                    mon: diem for mon, diem in diem_data.items()
                    if mon not in ["TONGDIEM"] 
                    and not mon.startswith("DM")
                    and isinstance(diem, (int, float)) 
                    and diem > 0
                }

                # Thêm TỔNG ĐIỂM
                diem_mon["TONGDIEM"] = diem_data.get("TONGDIEM", 0)

                print("\n📄 Kết quả tra cứu:")
                for mon, diem in diem_mon.items():
                    print(f"- {mon}: {diem}")
            else:
                print("❌ Không tìm thấy dữ liệu cho SBD này.")
        else:
            print("❌ Lỗi khi kết nối API.")
        

        

