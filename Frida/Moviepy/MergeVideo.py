# -*- coding: utf-8 -*-
# @Time   : 2020/11/11 2:11 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: MergeVideo.py
# @Software: PyCharm
'''
基于Moviepy 处理视频 实现对视频的拼接、叠加合成等。
获取视频时长 单位s  clip1.duration
获取视频尺寸       clip1.size

视频裁剪： https://www.freesion.com/article/3449998295/
    crop( clip, x1=None, y1=None, x2=None, y2=None, width=None,
    height=None, x_center=None, y_center=None)

音频提取： clip1.audio.to_audiofile("**.mp3")
'''

from moviepy.editor import VideoFileClip, concatenate_videoclips, clips_array, vfx, CompositeVideoClip, TextClip


def addedVideos():
    clip1 = VideoFileClip("text.mp4").margin(15)
    clip2 = clip1.fx(vfx.mirror_x)  # X 轴镜像
    clip3 = clip1.fx(vfx.mirror_y)  # Y 轴镜像
    clip4 = clip1.resize(0.6)  # 尺寸等比例缩放0。6

    final_clip = clips_array([
        [clip1], [clip3]
    ])
    final_clip.write_videofile("my_stack.mp4")


def mergeVideos():
    clip1 = VideoFileClip("text.mp4").subclip(0, 15)
    print(clip1.duration)
    clip2 = VideoFileClip("mhls.mp4").subclip(0, 15).resize(0.5)
    video = CompositeVideoClip([clip1,
                                clip2
                                ])
    CompositeVideoClip([clip1.set_pos("left", "center"), clip2.set_pos("right", "center")],
                       size=(clip1.w + clip1.w, clip2.h))

    video.write_videofile("merge_video.mp4")


def cutVideos():
    '''
    视频裁剪： https://www.freesion.com/article/3449998295/
    crop( clip, x1=None, y1=None, x2=None, y2=None, width=None,
    height=None, x_center=None, y_center=None)
    '''
    # 指定视频大小，对其进行裁剪
    clip1 = VideoFileClip("mhls.mp4").resize([540, 960])
    clip1 = clip1.crop(0, 200, 540, 760)
    clip1.write_videofile("cut_video.mp4")

    clip2 = VideoFileClip("cut_video.mp4")
    print(clip2.size)


#  对截取后的视频进行竖屏全屏处理，添加文字
def textclip():
    text_1 = (TextClip("剪辑不易 \n 关注啊", fontsize=70, color='white', font="FZZJ.TTF")
              .set_position(lambda t: ('center', 100 - t))
              .set_duration(15))
    text_2 = (TextClip("赶快右侧 \n 点赞啦", fontsize=70, color='red', font="FZZJ.TTF")
              .set_position(lambda t: ('center', 900 - t))
              .set_duration(15))

    clip1 = VideoFileClip("cut_video.mp4").fx(vfx.mirror_x)
    print(clip1.duration)
    result = CompositeVideoClip([clip1.set_position('center'), text_1, text_2],
                                size=[540, 1024])  # Overlay text on video
    result.write_videofile("final.mp4")


#  视频居中叠加 背景视频去除音乐。
def centerMerge():
    clip1 = VideoFileClip("text.mp4", audio=False).resize([540, 1024])
    print(clip1.duration)
    clip3 = VideoFileClip("cut_video.mp4", has_mask=True, audio=True)
    video = CompositeVideoClip([clip1, clip3.set_position('center')])
    video.write_videofile("centermergr.mp4")  # 先不加音频
    video.close()


if __name__ == '__main__':
    centerMerge()
