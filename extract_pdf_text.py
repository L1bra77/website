import PyPDF2
import os

def extract_pdf_text(pdf_path):
    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        print(f"PDF文件不存在: {pdf_path}")
        return ""
    
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # 提取所有页面的文本
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() or ""
    except Exception as e:
        print(f"提取PDF文本时出错: {e}")
    
    return text

# 测试提取当前目录下的简历文件
if __name__ == "__main__":
    pdf_path = "张豫坤简历(1).pdf"
    extracted_text = extract_pdf_text(pdf_path)
    print("提取的文本内容:")
    print(extracted_text)
    # 将提取的文本保存到文件
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)
    print("\n文本已保存到 extracted_text.txt")