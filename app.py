import os
import shutil

def main():
  # 指定要整理的檔案目錄
  directory = "D:\\下載\\app\\result"

  # 建立一個檔案名稱的集合
  file_names = set()

  # 遍歷目錄中的所有檔案
  for file in os.listdir(directory):
    # 取得檔案的名稱和副檔名
    filename, extension = os.path.splitext(file)

    # 將副檔名轉換為小寫
    extension = extension.lower()

    # 檢查檔案名稱是否重複
    if filename in file_names:
      # 檔案名稱重複，判斷檔案類型
      if extension in [".heic", ".jpg", ".jpeg", ".png"]:
        # 留下 HEIF、JPG、JPEG 或 PNG 檔
        shutil.move(os.path.join(directory, file), os.path.join(directory, "kept", file))
      else:
        # 移除重複的非 HEIF、JPG、JPEG 或 PNG 檔
        os.remove(os.path.join(directory, file))
    else:
      # 檔案名稱不重複，將檔案名稱加入集合
      file_names.add(filename)

if __name__ == "__main__":
  main()
