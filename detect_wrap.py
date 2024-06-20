import subprocess

def run_detect(weights, source, iou_thresh):
    command = [
        'python3', './yolov7/detect.py',
        '--weights', "./yolov7/yolov7.pt",
        '--source', "./yolov7/inference/images/bus.jpg",
        '--project', "output",
        '--name', "",
        # '--iou-thres', str(iou_thresh)
    ]
    print(command)
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

# 使用例
run_detect(weights='path/to/weights.pt', source='path/to/source', iou_thresh=0.6)

# import importlib.util
# import sys
# import os

# # detect.py のパス
# module_path = './yolov7/detect.py'
# sys.path.append("./yolov7/")

# # 引数の設定
# sys.argv = [
#     'detect.py',
#     '--weights', 'path/to/weights.pt',
#     '--source', 'path/to/source',
#     '--iou-thres', '0.6'
# ]

# # モジュール名
# module_name = 'detect'

# # モジュールを読み込む
# spec = importlib.util.spec_from_file_location(module_name, module_path)
# detect_module = importlib.util.module_from_spec(spec)
# sys.modules[module_name] = detect_module
# spec.loader.exec_module(detect_module)