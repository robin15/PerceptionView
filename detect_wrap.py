import subprocess

def run_detect():
    command = [
        'python3', './yolov7/detect.py',
        '--weights', "./yolov7/yolov7.pt",
        '--source', "./bus.jpg",
        '--project', "output",
        '--name', "",
    ]
    result = subprocess.run(command, capture_output=True, text=True)

run_detect()
