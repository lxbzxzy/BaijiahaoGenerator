def generate(subject: str, object: str) -> str:
    return '''
\t%s%s是怎么回事呢？%s相信大家都很熟悉，但是%s%s是怎么回事呢？下面就让小编带大家一起了解吧。
\t%s%s，其实这是一件很正常的事情，所以%s%s。大家可能会惊讶%s怎么会%s呢？但事实就是这样，小编也感到非常惊讶。
\t这就是关于为什么%s%s的事情了，大家有什么想法呢？欢迎在评论区告诉小编一起讨论哦！
    ''' % (subject, object, subject, subject, object, subject, object, subject, object, subject, object, subject, object)

if __name__ == "__main__":
    subject = input("请输入主语：")
    object = input("请输入谓宾：")
    print(generate(subject, object))
