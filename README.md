# AICovidVN115m - Giải pháp đạt Hạng 3 vòng Về đích (AUC 0.92)

Cuộc thi "[AICV-115M Challenge](https://aihub.vn/competitions/22#learn_the_details)" là một cuộc thi về nhận diện Covid19 qua tiếng ho với tổng giải thưởng 115 triệu VND với 168 cá nhân tham gia.  
Chúng tôi - nhóm `đi thi` đã đạt được **Hạng 3** với điểm (tính bằng AUC) là **0.92** (chính xác hơn là 0.921527). Vậy nên, chúng tôi mong repository này sẽ cung cấp một nguồn tham khảo về giải pháp mà chúng tôi đã triển khai, cũng như là một sự tham khảo cho những người muốn quan tâm. Để đào sâu vào chi tiết, bạn có thể tham khảo báo cáo kỹ thuật, slide và video thuyết trình trong thư mục `reports/`. Những ý kiến đóng góp sẽ luôn được chúng tôi đón nhận.

<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/report/score.jpg" width="1000"></p>
<p align="center"><i>Hình 1. Điểm số cao nhất đạt được của nhóm (AUC 0.921527)</i></p>
<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/report/ranking.jpg" width="1000"></p>
<p align="center"><i>Hình 2. Nhóm "đi thi" đạt Hạng 3 chung cuộc (thua 2 nhóm đầu xấp xỉ 0.01)</i></p>

## 1. Môi trường và Những thư viện cần thiết

Môi trường cần thiết là Python 3.X, bạn có thể dễ dàng cài đặt theo trang thủ https://www.python.org/ (nếu cần thiết) hoặc có thể sử dụng những nơi tích hợp sẵn như https://colab.research.google.com/.

Về phần thư viện, chúng tôi đã ghi chú ở trong tệp tin `requirements.txt`. Nếu bạn muốn cài đặt nhanh gọn, có thể sử dụng câu lệnh ở trên cửa sổ dòng lệnh (Command Prompt, Terminal, ...).
```
pip install -r requirements.txt
```

Giả sử bạn sử dụng Google Colab, việc cài đặt thư viện là không cần thiết. Còn nếu trong trường hợp bạn sử dụng môi trường máy cá nhân, chúng tôi khuyến khích tạo và sử dụng riêng môi trường ảo hoá của Python để đảm bảo độc lập, tránh xung đột với môi trường sẵn có (https://docs.python.org/3/tutorial/venv.html).  
Sau bước này, cơ bản là bạn đã có thể sử dụng được những mã nguồn cần thiết.

Trong `requirements.txt` cũng đã có những thư viện hỗ trợ chạy API là Django và một số thư viện hỗ trợ liên quan, nên sau khi cài đặt bạn cũng hoàn toàn có thể thử nghiệm API.  
Riêng về phần frontend thì bạn hoàn toàn có thể bỏ qua nếu thấy không cần thiết, trong trường hợp muốn sử dụng frontend, môi trường Node.js https://nodejs.org/en/download/ cần phải được cài đặt. Tiếp đến là cài đặt vue-cli cho việc biên dịch máy chủ:
```
npm i
```

## 2. Cấu trúc chính của repository

```
aicovidvn115m
│   LICENSE
|   main.py
│   README.md
│   requirements.txt
|   submission.ipynb
│
└───data/ - nơi lưu trữ thông tin về tập dữ liệu và chính tập dữ liệu
│   │   extra/ - 20 mẫu dữ liệu âm thanh dương tính được lấy từ tập aicv115m_extra_public_1235samples của BTC
│   |   private/ - 1627 mẫu dữ liệu dùng để kiểm tra mô hình
|   |   private_features/ - lưu trữ những đặc trưng được trích lọc ra từ private/
|   |   train/ - 4505 mẫu dữ liệu huấn luyện
|   |   train_features/ - lưu trữ những đặc trưng được trích lọc từ train/
|   |   ...
└───modules/ - tất cả những mã nguồn đã sử dụng để xây dựng mô hình
|   |   __init__.py
│   │   ...
│
└───report/ - báo cáo kỹ thuật, slides và những hình ảnh liên quan
|   |   report.pdf
|   |   ranking.jpg
│   │   ...
│
└───src/ - mã nguồn cho api backend và frontend
│   └───backend/- lưu trữ api
|   |   |   manage.py - tệp tin thực thi để dựng máy chủ backend
│   |   frontend/ - lưu trữ frontend
└───weights/ - mô hình đã được huấn luyện
│   │   modles/ - lưu trữ 100 mô hình đã được huấn luyện
│   │   scalers/ - lưu trữ 4 scaler dùng để chuẩn hoá dữ liệu
│
```

## 3. Huấn luyện và Dự đoán

### 3.1 Huấn luyện

Để có thể huấn luyện mô hình, trong thư mục `modules`, sử dụng câu lệnh:
```
python train.py
```

Lưu ý: khi huấn luyện, các mô hình sẽ được lưu ở thư mục `weigths/models/`, để chắc chắn những mô hình huấn luyện không ghi đè lên những mô hình đã được huấn luyện của chúng tôi, bạn có thể lưu trữ những mô hình đã có ở nơi khác hoặc thay đổi đường dẫn lưu trữ mô hình trong tệp tin mã nguồn `modules/train.py`.

### 3.2 Dự đoán

Cũng trong thư mục `modules`, sử dụng câu lệnh:
```
python predict.py
```

Kết quả sẽ được ghi ra ở tệp tin `modules/results.csv`. Tệp tin `modules/results.csv` có sẵn là kết quả mà chúng tôi đã sử dụng giúp đạt được thứ hạng trong cuộc thi.

## 4. Sử dụng trực tiếp

Bạn có thể sử dụng mô hình của chúng tôi ở đường dẫn chính bằng việc thực thi tệp tin `main.py`.
```
python main.py -f audio_file_name
```

`audio_file_name` có thể là tên hoặc đường dẫn của một tệp tin âm thanh. Định dạng yêu cầu của tệp tin là `.wav`, bạn vui lòng dùng các công cụ chuyển đổi để đưa về định dạng phù hợp.

## 5. API

Chúng tôi xây dựng một API đơn giản với khung Django. Các bạn có thể dựng máy chủ API này bằng cách thực thi lệnh sau ở thu mục `src/backend/`:
```
python manage.py runserver
```

Máy chủ mặc định sẽ được dựng ở địa chỉ IP loopback `127.0.0.1`, cổng `8000` (http://127.0.0.1.8000/). Thông thường các máy hiện nay sẽ có loopback là `localhost`, nên các bạn có thể thay thế địa chỉ IP trên với từ khoá `localhost`.  
Đường dẫn (endpoint) để sử dụng API được chúng tôi cài đặt tại đường dẫn `api/predict/` với phương thức POST. Để cho đơn giản, chúng tôi đã bỏ đi những yếu tố bảo mật như CSRF, CORS. Tệp tin âm thanh gửi qua theo dạng biểu mẫu (form) với tên `"audio"`. Kết quả trả về có định dạng JSON như sau.
```json
{
    "prob": 0.123456789
}
```

<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/report/api.jpg" width="1000"></p>
<p align="center"><i>Hình 3. Thử nghiệm API trên phần mềm Postman</i></p>

## 6. Frontend

Để thực hiện bước này, đảm bảo rằng bạn đã khởi động máy chủ API.  
Tiếp đó, dựng máy chủ frontend bằng cách thực thi dòng lệnh sau ở trong thư mục `src/frontend/`:
```
npm run serve
```

Địa chỉ mà máy chủ được dựng lên mặc định sẽ là http://localhost:8080/. Một tính năng thú vị của npm là sẽ giúp bạn xây dựng thêm một địa chỉ mạng (network) bằng địa chỉ IP địa phương (local IP) và với cổng 8080 tương ứng. Địa chỉ này sẽ được thông báo ra cửa sổ dòng lệnh sau khi máy chủ được biên dịch xong.  
Địa chỉ API mà frontend được cài đặt là giống như mặc định của địa chỉ máy chú API, đảm bảo rằng nếu bạn thay đổi địa chỉ máy chủ API thì cũng phải đồng bộ địa chỉ mà frontend sử dụng ở trong `src/frontend/src/App.vue`, dòng 72.  

Giao diện chúng tôi xây dựng cũng khá đơn giản, hy vọng sẽ không làm khó bạn trong khi sử dụng. Kết quả thực thi mỗi lần khoảng dưới 15 giây với cấu hình máy trung bình hiện nay.

<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/report/frontend.jpg" width="1000"></p>
<p align="center"><i>Hình 4. Thử nghiệm frontend</i></p>

Kết quả xuất ra có màu từ xanh lục rồi dần dần đến đỏ tuỳ theo xác suất trả về. Nếu là màu đỏ, khả năng cao là bạn phải đi cách ly. Chúng tôi mong rằng mẫu thử nghiệm của bạn sẽ hiện ra màu xanh như trong Hình 4.

## 7. Lời cảm ơn

Xin gửi lời cảm ơn đến những người đã lập nên dự án cộng đồng AICovidVN để tổ chức cuộc thi này. Đây không chỉ là sân chơi cho chúng tôi, những sinh viên đại học, có cơ hội được áp dụng những kiến thức đã học mà còn giúp chung tôi học thêm được nhiều điều mới.  
Ngoài khía cạnh kỹ thuật, cuộc thi cũng đòi hỏi chúng tôi phải tìm hiểu thêm về COVID-19, nhờ đó mà chúng tôi đã có thêm những hiểu biết rõ ràng về dịch bệnh đang diễn ra trên toàn thế giới.  
Mục đích cuộc thi nhằm xây dựng một giải pháp giúp cho việc chẩn đoán COVID-19, chúng tôi hy vọng rằng cũng đã đóng góp ít nhiều cho mục đích cao cả này và mong sẽ sớm được thấy những giải pháp trí tuệ nhân tạo được đưa vào áp dụng thực tế.

## 8. Giấy phép

[MIT](https://github.com/dee-ex/aicovidvn115m/blob/main/LICENSE)
