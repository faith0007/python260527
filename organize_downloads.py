import os
import shutil
from pathlib import Path

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 파일 분류 규칙
file_categories = {
    'images': ['.jpg', '.jpeg'],
    'data': ['.csv', '.xlsx'],
    'docs': ['.txt', '.doc', '.pdf'],
    'archive': ['.zip']
}

def create_folders():
    """필요한 폴더 생성"""
    for category in file_categories.keys():
        folder_path = os.path.join(download_folder, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"✓ 폴더 생성: {folder_path}")
        else:
            print(f"✓ 폴더 이미 존재: {folder_path}")

def organize_files():
    """파일을 분류하여 해당 폴더로 이동"""
    try:
        files_moved = 0
        files_skipped = 0
        
        for filename in os.listdir(download_folder):
            file_path = os.path.join(download_folder, filename)
            
            # 파일인지 확인 (폴더는 건너뛰기)
            if not os.path.isfile(file_path):
                continue
            
            # 파일 확장자 확인
            file_ext = os.path.splitext(filename)[1].lower()
            
            # 해당하는 카테고리 찾기
            moved = False
            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    destination = os.path.join(download_folder, category, filename)
                    try:
                        shutil.move(file_path, destination)
                        print(f"✓ 이동 완료: {filename} → {category}/")
                        files_moved += 1
                        moved = True
                        break
                    except Exception as e:
                        print(f"✗ 이동 실패 [{filename}]: {e}")
                        files_skipped += 1
            
            if not moved:
                files_skipped += 1
        
        print(f"\n{'='*50}")
        print(f"정리 완료!")
        print(f"이동된 파일: {files_moved}개")
        print(f"건너뛴 파일: {files_skipped}개")
        
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    print("다운로드 폴더 정리 시작...")
    print(f"위치: {download_folder}\n")
    
    # 1단계: 폴더 생성
    print("[1단계] 필요한 폴더 생성")
    create_folders()
    
    # 2단계: 파일 이동
    print("\n[2단계] 파일 분류 및 이동")
    organize_files()
