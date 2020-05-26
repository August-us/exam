from PIL import Image
import paddlehub as hub



def catPicture():
    humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
    results = humanseg.segmentation(data={'image':[r'C:\Users\August-us\Desktop\helin.jpg']})

    for mask in results:

        # 读取背景图片
        mask =Image.fromarray(mask['data']).convert('L')

        bg = Image.open(r'C:\Users\August-us\Desktop\back.jpg')
        im = Image.open(r'C:\Users\August-us\Desktop\helin.jpg').convert('RGBA')
        im.thumbnail((bg.size[1], bg.size[1]))
        mask.thumbnail((bg.size[1], bg.size[1]))
        mask.save('mask.jpg')

        # 分离通道
        r, g, b, a = im.split()
        print(bg.size, im.size, mask.size)
        # 将抠好的图片粘贴到背景上
        bg.paste(im, (100,3456-2042),mask=mask)
        bg.save('12.jpg')

def wordcloud():
    from wordcloud import WordCloud
    import matplotlib.pyplot  as  plt  # 绘制图像的模块
    import jieba  # jieba分词
    from PIL import Image
    import numpy as np

    path_txt = r'C:\Users\August-us\Desktop\python.txt'
    f = open(path_txt, 'r', encoding='UTF-8').read()

    # 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
    mask = np.array(Image.open(r'C:\Users\August-us\Desktop\helin1.jpg').convert('L').resize((4608, 3456,)))

    cut_text = " ".join(jieba.cut(f))

    wordcloud = WordCloud(
        # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
        font_path="C:/Windows/Fonts/simfang.ttf",
        mask=mask,
        # 设置了背景，宽高
        background_color="white").generate(cut_text)

    wordcloud.to_file(r'C:\Users\August-us\Desktop\123.jpg')