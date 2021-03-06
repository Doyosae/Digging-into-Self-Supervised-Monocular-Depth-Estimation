import argparse



def options():
    parser = argparse.ArgumentParser(description = "Input optional guidance for training")
    parser.add_argument("--datapath",
        default = "./dataset/kitti",
        type = str, help = "데이터셋 경로")
    parser.add_argument("--splits",
        default = "./splits",
        type = str, help = "데이터셋 splits 경로")


    parser.add_argument("--dataset",
        default = "kitti_mono",
        type = str, help = ["kitti_mono", "kitti_stere"])
    parser.add_argument("--datatype",
        default = "kitti_eigen_zhou",
        type = str, help = ["kitti_benchmark", "kitti_eigen_full", "kitti_eigen_zhou"])


    parser.add_argument("--epoch",
        default = 24,
        type = int, help = "모델 에포크 수")
    parser.add_argument("--batch",
        default = 12,
        type = int, help = "모델 배치 사이즈")
    parser.add_argument("--prepetch",
        default = 2,
        type = int, help = "데이터 로더의 prefetch_factor")
    parser.add_argument("--num_workers",
        default = 12,
        type = int, help = "데이터 로더의 num_workers")
    # 0.001이 아니라 0.0001로 할 것 (1e-4 = 0.0001)
    parser.add_argument("--learning_rate",
        default = 1e-4,
        type = str, help = "모델 러닝 레이트")
    parser.add_argument("--scheduler_step",
        default = 15,
        type = int, help = "모델 스케줄러 스텝 값")
    parser.add_argument("--disp_smoothness",
        default = 1e-3,
        type = float, help = "smooth loss loss의 가중치 값")
    parser.add_argument("--save",
        default = "test",
        type = str, help = "저장할 모델 정보의 입력")
    

    parser.add_argument("--height", 
        default = 192, 
        type = int, help = "이미지의 높이")
    parser.add_argument("--width", 
        default = 640, 
        type = int, help = "이미지의 너비")
    parser.add_argument("--scales",
        default = range(4), 
        type = str, help = "뎁스 디코더의 레인지 범위")

        
    parser.add_argument("--min_depth",
        default = 0.1, 
        type = float, help = "최소 깊이")
    parser.add_argument("--max_depth",
        default = 100.0, 
        type = float, help = "최대 깊이")
    parser.add_argument("--frame_ids",
        default = [0, -1, 1], 
        type = str, help = "프레임 리스트의 아이디")
    parser.add_argument("--pose_frames",
        default = 2, 
        type = str, help = "포즈 네트워크에 입력될 프레임 수")
    parser.add_argument("--num_layers",
        default = 18, 
        type = int, help = "Resnet 모델 버전 18, 34 중 18이 기본")
    parser.add_argument("--weight_init",
        default = True,
        type = str, help = "이미지넷 사전 학습 모델 사용 여부")
    # separate가 monodepth2의 아이디어
    parser.add_argument("--pose_type",
        default = "separate",
        type = str, help = ["posecnn", "shared", "separate"])


    parser.add_argument("--use_automasking",
        default = True,
        type = bool, help = "오토 마스킹 옵션")
    args = parser.parse_args()
    return args