def generate_news_script(title, content):
    script = f"""
【校园新闻播报稿】

各位老师、同学们，大家好。下面为大家播报一则校园新闻。

本条新闻的主题是：{title}

{content}

以上就是本条新闻的主要内容。感谢大家收听。
"""
    return script


def main():
    title = input("请输入新闻标题：")
    content = input("请输入新闻正文：")

    result = generate_news_script(title, content)

    print("\n生成结果：")
    print(result)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("已生成 output.txt 文件")


if __name__ == "__main__":
    main()
