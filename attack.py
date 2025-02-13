import asyncio
import websockets
import socket
import uuid
import json
async def get_local_ip():
    """Lấy địa chỉ IP nội bộ của máy một cách chính xác"""
    try:
        # Tạo socket kết nối tới một server external
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Kết nối tới Google DNS để lấy IP thực
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        # Phương án dự phòng nếu không lấy được IP
        return socket.gethostbyname(socket.gethostname())
async def send_message(command):
    uri = "ws://127.0.0.1:8080"


    # Tạo một ID cố định duy nhất cho máy này
    device_id = 'hacker'

    async with websockets.connect(uri) as websocket:
        # print("✅ Connected to the server.")
        data_hacker = {
            'IP': device_id
        }
        # Gửi ID cố định của máy lên server
        await websocket.send(json.dumps(data_hacker))
        # print(f"📤 Sent device ID to server: {device_id}")

        while True:
            # command = input(f"\nEnter command (GET_CLIENTS or SENDTO:<device_id>:<message>): ")
            if command.lower() == "exit":
                break
            
            await websocket.send(command)
            response = await websocket.recv()
            data = json.loads(response)
            # return (f"📩 Server response: {response}")
            if data['type'] == "get_clients":
                return data['data']
                # print(data['data'])
                # for line in data['data']:
                #     print(f"📩 Server response: {line}")
            elif data['type'] == "message_sent":
                return (data['data'])

# async def main():
#     await send_message()

# Chạy chương trình
# asyncio.run(main())