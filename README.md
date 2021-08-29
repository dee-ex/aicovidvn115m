# AICovidVN115m - Giải pháp đạt Hạng 3 vòng Về đích (AUC 0.92)

Cuộc thi "AICV-115M Challenge" là một cuộc thi về nhận diện Covid19 qua tiếng ho với tổng giải thưởng 115 triệu VND với 168 cá nhân tham gia.  
Chúng tôi - nhóm `đi thi` đã đạt được Hạng 3 với điểm (tính bằng AUC) là 0.92 (chính xác hơn là 0.921527). Vậy nên, chúng tôi mong repository này sẽ cung cấp một cái nhìn rõ ràng hơn về giải pháp mà chúng tôi đã triển khai, cũng như là một sự tham khảo cho những người muốn quan tâm. Những ý kiến đóng góp sẽ luôn được chúng tôi đón nhận.

<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/images/score.jpg" width="1000"></p>
<p align="center"><i>Hình 1. Điểm số cao nhất đạt được của nhóm (AUC 0.921527)</i></p>
<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/images/ranking.jpg" width="1000"></p>
<p align="center"><i>Hình 2. Nhóm `đi thi` đạt Hạng 3 chung cuộc (thua 2 nhóm đầu xấp xỉ 0.01)</i></p>

## Môi trường và Những thư viện cần thiết

Môi trường cần thiết là Python 3.X, bạn có thể dễ dàng cài đặt theo trang thủ https://www.python.org/ (nếu cần thiết) hoặc có thể sử dụng những nơi tích hợp sẵn như https://colab.research.google.com/.

Về phần thư viện, chúng tôi đã ghi chú ở trong tệp tin `requirements.txt`. Nếu bạn muốn cài đặt nhanh gọn, có thể sử dụng câu lệnh ở trên cửa sổ dòng lệnh (Command Prompt, Terminal, ...).
```
pip install -r requirements.txt
```

Giả sử bạn sử dụng Google Colab, việc cài đặt thư viện là không cần thiết. Còn nếu trong trường hợp bạn sử dụng môi trường máy cá nhân, chúng tôi khuyến khích tạo và sử dụng riêng môi trường ảo hoá của Python để đảm bảo độc lộp, tránh xung lập với môi trường sẵn có.

## Cấu trúc chính của repository

```
aicovidvn115m
│   LICENSE
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
└───modules/ - tất cả những mã nguồn sử dụng
|   |   __init__.py
│   │   ...
│
└───weights/ - mô hình đã được huấn luyện
│   │   model_10_1.pkl
│   │   ...
│
```

## Huấn luyện và Dự đoán

### Huấn luyện

Để có thể huấn luyện, trong thư mục `modules`, sử dụng câu lệnh:
```
python train.py
```
Lưu ý: khi huấn luyện, các mô hình sẽ được lưu ở thư mục `weigths/`, để chắc chắn những mô hình này không bị ảnh hưởng, bạn có thể lưu trữ những mô hình này ở nơi khác hoặc thay đổi đường dẫn lưu trữ trong tệp tin `modules/train.py`.

### Dự đoán

Cũng trong thư mục `modules`, sử dụng câu lệnh:
```
python predict.py
```

Kết quả sẽ được ghi ra ở tệp tin `modules/results.csv`. Tệp tin `modules/results.csv` là kết quả mà chúng tôi đã sử dụng giúp đạt được thứ hạng trong cuộc thi.

## Lời cảm ơn

Xin gửi lời cảm ơn đến những người đã lập nên dự án cộng đồng AICovidVN để tổ chức cuộc thi này. Đây không chỉ là sân chơi cho chúng tôi, những sinh viên đại học, có cơ hội được áp dụng những kiến thức đã học mà còn giúp chung tôi học thêm được nhiều điều mới.  
Ngoài khía cạnh kỹ thuật, cuộc thi cũng đòi hỏi chúng tôi phải tìm hiểu thêm về COVID-19, nhờ đó mà chúng tôi đã có thêm những hiểu biết rõ ràng về dịch bệnh đang diễn ra trên toàn thế giới.  
Mục đích cuộc thi nhằm xây dựng một giải pháp giúp cho việc chẩn đoán COVID-19, chúng tôi hy vọng rằng cũng đã đóng góp ít nhiều cho mục đích cao cả này và mong sẽ sớm được thấy những giải pháp trí tuệ nhân tạo được đưa vào áp dụng thực tế.

## Giấy phép

MIT
