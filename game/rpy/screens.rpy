################################################################################
## 初始化
################################################################################
init offset = -1
init python:
    class Song:
        def __init__(self, name, file):
            self.name = name
            self.file = file
    songs = [
        Song("歌曲1", "music/M01.ogg"),Song("歌曲2", "music/M01s.ogg"),Song("歌曲3", "music/M03.ogg"),
        Song("歌曲4", "music/M04.ogg"),Song("歌曲5", "music/M05.ogg"),Song("歌曲6", "music/M06.ogg"),
        Song("歌曲7", "music/M07.ogg"),Song("歌曲8", "music/M08.ogg"),Song("歌曲9", "music/M09.ogg"),
        Song("歌曲10", "music/M10.ogg"),Song("歌曲11", "music/M11.ogg"),Song("歌曲12", "music/M12.ogg"),
        Song("歌曲13", "music/M13.ogg"),Song("歌曲14", "music/M14.ogg"),Song("歌曲15", "music/M15.ogg"),
        Song("歌曲16", "music/M16.ogg"),Song("歌曲17", "music/M17.ogg"),Song("歌曲18", "music/M18.ogg"),
        Song("歌曲19", "music/M19.ogg"),Song("歌曲20", "music/M20.ogg"),Song("歌曲21", "music/M21.ogg"),
        Song("歌曲22", "music/M22.ogg"),Song("歌曲23", "music/M23.ogg"),Song("歌曲24", "music/M24.ogg"),
        Song("歌曲25", "music/M25.ogg"),Song("歌曲26", "music/M26.ogg"),Song("歌曲27", "music/M27.ogg"),
        Song("歌曲28", "music/M28.ogg"),Song("歌曲29", "music/M29.ogg"),Song("歌曲30", "music/M30.ogg"),
        ]
define stopall = renpy.music.stop
default page_index = 0
define songs_per_page = 7

################################################################################
## 样式
################################################################################
style default:
    properties gui.text_properties()
    language gui.language
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
style gui_text:
    properties gui.text_properties("interface")
style button:
    properties gui.button_properties("button")
style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
style prompt_text is gui_text:
    properties gui.text_properties("prompt")
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
################################################################################
## 游戏内界面
screen my_scr:
    key "K_RETURN" action Hide("nonexistent_screen")
    key "K_KP_ENTER" action Hide("nonexistent_screen")
    key "K_SPACE" action Hide("nonexistent_screen")
    key "mousedown_4" action Hide("nonexistent_screen")
    key "K_PAGEUP" action Hide("nonexistent_screen")
    key "mousedown_5" action Hide("nonexistent_screen")
    key "mouseup_3" action Hide("nonexistent_screen")
    key "mouseup_1" action Hide("nonexistent_screen")
    # 只允许ESC键跳过视频
    key "K_ESCAPE" action Return("smth")





################################################################################
## 0.对话界面 ########################################################################
##
## 对话界面用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此界面必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')
style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label
style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
## 1.输入界面 ########################################################################
screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos
            text prompt style "input_prompt"
            input id "input"
style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
## 1.选择界面 ########################################################################
screen block_click():
    imagemap:
        ground "images/picture/chapter1/bg1_2.png"
        hotspot (0, 0, 1280, 720) focus_mask None action None
#上半部分：
transform from_bottom_right:
    xalign 1.05
    yalign 1.0
    linear 0.5 xalign 1.05 yalign 0.82
init python:
    page = 1
    pagext = 1
    chapter1_names = ["猫的过错 星与死", "冬的早晨", "她的一日1", "她的一日2","洋馆的少女"]
    chapter1_5_names = ["回转的七天  1", "回转的七天  2", "回转的七天  3", "回转的七天  4"]
    chapter2_names = ["我们的午餐", "那又怎么了", "都市的做派"]
    chapter3_names = ["夜晚的事件"]
    chapter4_names = ["夜晚们的少女","就算被说不适合我","秘密的觉悟","夜晚来临"]
    chapter5_one_names = ["魔法使之夜1","魔法使之夜2","魔法使之夜3","魔法使之夜4","魔法使之夜5"]
    chapter5_two_names = ["魔法使之夜6","魔法使之夜7","魔法使之夜8","魔法使之夜9","魔法使之夜10","魔法使之夜11","魔法使之夜12","魔法使之夜13","魔法使之夜14"]
    chapter6_names = ["怀乡白梦","逢籁之前","唐突的青子","玻璃小瓶","洋馆的生活","或者，像鸟一样"]
    chapter7_names = ["鸟儿远飞","估算太天真","童话之庭","旅鸽"]

######################
###第1章：
screen choices_1():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    # 使用at参数来指定动画效果
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第1章" pos (41,0) color "#ffffff"
            if page > 1:
                textbutton "上一页" xpos 430 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page - 1)
            if page < 2:
                textbutton "下一页" xpos 525 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page + 1)

            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter1_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter1_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_1_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null
######################
###第1.5章：
screen choices_1_5():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第1.5章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter1_5_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter1_5_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_1_5_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null
######################
###第2章：
screen choices_2():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第2章" pos (41,0) color "#ffffff"

            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter2_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter2_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_2_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null
######################
###第3章：
screen choices_3():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第3章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter3_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter3_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_3_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

######################
###第4章：
screen choices_4():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第4章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter4_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter4_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_4_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null
######################
###第5章（前）：
screen choices_5_one():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第5章（前半）" pos (41,0) color "#ffffff"
            if page > 1:
                textbutton "上一页" xpos 430 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page - 1)
            if page < 2:
                textbutton "下一页" xpos 525 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page + 1)
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter5_one_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter5_one_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_5_1_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

######################
###第5章（后）：
screen choices_5_two():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第5章（后半）" pos (41,0) color "#ffffff"
            if page > 1:
                textbutton "上一页" xpos 430 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page - 1)
            if page < 2:
                textbutton "下一页" xpos 525 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page + 1)
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter5_two_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter5_two_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_5_2_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

######################
###第6章：
screen choices_6():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第6章" pos (41,0) color "#ffffff"
            if page > 1:
                textbutton "上一页" xpos 430 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page - 1)
            if page < 2:
                textbutton "下一页" xpos 525 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page + 1)

            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter6_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter6_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_6_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

######################
###第7章：
screen choices_7():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第7章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter7_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter7_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_7_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

######################
#########3下半部分：
transform from_bottom_self:
    xalign 1.05
    yalign -0.1
    linear 0.5 xalign 1.05 yalign 0.12
init python:
    page = 1
    pagexyz = 1
    chapter8_names = ["寒假的后山扫除","魔术师与野生儿 ", "礼物是项圈？？", "平和的上午", "黑板"]
    chapter8_5_names = ["不义之财事件"]
    chapter9_names = ["家常便饭 vs 外卖大餐","回礼 ", "水族馆", "姐姐回来了","苍崎家的故事 "]
    chapterfanwai1_names = ["为什么什么PLOY 1","为什么什么PLOY 2", "为什么什么PLOY 3", "为什么什么PLOY 4","为什么什么PLOY 5","为什么什么PLOY 6"]
    chapter10_names = ["冬天的一日-扫除","夜晚来临 ", "久违的魔女", "再见了 小红帽","雪落之痕 "]
    chapter11_names = ["去教会","狼的故事 ", "憧憬与焦躁", "----夜晚",]
    chapter12_names = ["青色的魔法","就这样---青色的魔法", ]
    chapter13_names = ["归途"]
    chapterfanwai2_names = ["寻蜜冒险"]
    chapterfanwai3_names = ["大家可以睡觉，但绝对不能笑出来"]
    chapter16_names = ["某天的事"]
######################
###第8章：
screen choices_8():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第8章" pos (41,0) color "#ffffff"
            if page > 1:
                textbutton "上一页" xpos 430 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page - 1)
            if page < 2:
                textbutton "下一页" xpos 525 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page + 1)

            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter8_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter8_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_8_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

########################
###第8.5章：
screen choices_8_5():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第8.5章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter8_5_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter8_5_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_8_5_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

######################
###第9章：
screen choices_9():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第9章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter9_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter9_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_9_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

######################
###番外1：
screen choices_fanwai1():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "番外1" pos (41,0) color "#ffffff"
            if page > 1:
                textbutton "上一页" xpos 430 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page - 1)
            if page < 2:
                textbutton "下一页" xpos 525 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page + 1)
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapterfanwai1_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapterfanwai1_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_fanwai1_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null


######################
###第10章：
screen choices_10():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第10章" pos (41,0) color "#ffffff"
            if page > 1:
                textbutton "上一页" xpos 430 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page - 1)
            if page < 2:
                textbutton "下一页" xpos 525 ypos 165 text_font "tl/test.ttf" text_size 20 action SetVariable("page", page + 1)
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter10_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter10_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_10_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

######################
###第11章：
screen choices_11():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第11章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter11_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter11_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_11_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null
######################
###第12章：
screen choices_12():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第12章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter12_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter12_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_12_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null
######################
###第13章：
screen choices_13():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第13章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter13_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter13_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_13_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null

######################
###第14章：
screen choices_fanwai2():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "番外2" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapterfanwai2_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapterfanwai2_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_fanwai2_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null
######################
###第15章：
screen choices_fanwai3():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "番外3" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapterfanwai3_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapterfanwai3_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_fanwai3_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null
######################
###第16章：
screen choices_16():
    add "gui/ui/bookxyz.png"
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 action Return()
    modal True
    frame at from_bottom_right:
        background "gui/ui/frame.png"
        xysize (623, 223)
        fixed:
            text "第13章" pos (41,0) color "#ffffff"
            grid 1 4:
                for i in range((page - 1) * 4, page * 4):
                    if i < len(chapter16_names):
                        # 定义一个变量来存储章节的名字
                        $ chapter_name = chapter16_names[i]
                        # 使用变量来创建文字按钮
                        textbutton "[chapter_name]" action Jump("story_16_{}".format(i + 1)) pos (35, 75) text_font "tl/test.ttf" text_size 20
                    else:
                        null
## 2.标题和游戏菜单界面
################################################################################
## (1)导航界面 (已经修改)########################################################################
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。
screen xyz():
    tag menu
    imagebutton idle "gui/ui/navigation/xyz.png" hover "gui/ui/navigation/xyz_hover.png" xcenter 0.92 ycenter 0.10 action ShowMenu("navigation")
##########################
screen navigation():
    add "gui/ui/navigation/confirm.png"
    add "gui/ui/navigation/navigation_bg.png"
    imagebutton idle "gui/ui/navigation/backbg.png" hover "gui/ui/navigation/backbg2.png" xalign 0.855 yalign  0.498 activate_sound "sound/click.ogg"   action Return()
    vbox:
        spacing 10
        xalign  0.90
        yalign  0.30
        imagebutton idle "gui/ui/navigation/save.png" hover "gui/ui/navigation/save_hover.png" activate_sound "sound/click.ogg"  action ShowMenu("save")
        imagebutton idle "gui/ui/navigation/load.png" hover "gui/ui/navigation/load_hover.png" activate_sound "sound/click.ogg"  action ShowMenu("load")
        imagebutton idle "gui/ui/navigation/title.png" hover "gui/ui/navigation/title_hover.png" activate_sound "sound/click.ogg"   action MainMenu()
    # 在这里添加一行代码，用于隐藏nvl模式的文字
    $ renpy.hide_screen("nvl")
###########################
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此界面与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。
###########################
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    frame:
        style "game_menu_outer_frame"
        hbox:
            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude

    label title
    if main_menu:

        key "game_menu" action ShowMenu("main_menu")




style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text
style game_menu_outer_frame:
    bottom_padding 23
    top_padding 90
    background "gui/overlay/game_menu.png"



style game_menu_navigation_frame:
    xsize 210
    yfill True
style game_menu_content_frame:
    left_margin 30
    right_margin 15
    top_margin 8

style game_menu_viewport:
    xsize 690
style game_menu_vscrollbar:
    unscrollable gui.unscrollable
style game_menu_side:
    spacing 8
style game_menu_label:
    xpos 38
    ysize 90
style game_menu_label_text:
    size 22
    color "#006666"
    yalign 0.5
style return_button:
    xpos 20
    yalign 1.0
    yoffset -22
###############################################################################
## (2)设置界面(已完工)
transform getIn:
    xoffset -40
    yoffset 0
    alpha 0.0
    easein 0.35 xoffset 0 alpha 1.0
###############
screen setting(choice_name="unknown"):
    tag menu
    modal True
    add "gui/ui/setting/BG_load.png":
        size(960,544)
    imagebutton idle "gui/ui/setting/back.png" hover "gui/ui/setting/back_hover.png" xcenter 0.5 ycenter 0.95  action Return()
    hbox:
        xalign 0.8
        yalign 0.0410
        spacing 30
        imagebutton:
            idle "gui/ui/setting/system.png"
            hover "gui/ui/setting/syetem_hover.png"
            selected choice_name=="syetem"
            action [Show("system", transition=None)]
            activate_sound "sound/click.ogg"
            xysize(80,39)
        imagebutton:
            idle "gui/ui/setting/message.png"
            hover "gui/ui/setting/message_hover.png"
            selected choice_name=="message"
            action [Show("message", transition=None)]
            activate_sound "sound/click.ogg"
            xysize(80,39)
        imagebutton:
            idle "gui/ui/setting/sound.png"
            hover "gui/ui/setting/sound_hover.png"
            selected choice_name=="sound"
            action [Show("sound", transition=None)]
            activate_sound "sound/click.ogg"
            xysize(130,39)
        imagebutton:
            idle "gui/ui/setting/key.png"
            hover "gui/ui/setting/key_hover.png"
            selected choice_name=="key"
            action [Show("key", transition=None)]
            activate_sound "sound/click.ogg"
            xysize(100,39)
## 设置4个子界面：
image my_slider_idle_thumb:
    "gui/ui/setting/conf_sbtn_002.png"
image my_slider_hover_thumb:
    "gui/ui/setting/conf_sbtn_001.png"
style myslider:
    ysize 20
    base_bar Frame("gui/ui/setting/conf_sbar_002.png",gui.slider_borders,tile=gui.slider_tile)
    idle_thumb "my_slider_idle_thumb"
    hover_thumb "my_slider_hover_thumb"
    thumb_offset -20
    yalign 1.0
    xalign 1.0
##第一个：
############
screen system():
    use setting("syetem")
    imagebutton idle "gui/ui/setting/back.png" hover "gui/ui/setting/back_hover.png" xcenter 0.5 ycenter 0.95  action Hide("system")
    frame:
        background "gui/ui/setting/system_bg.png"

        at getIn
##第二个：
#############
screen message():
    use setting("message")
    imagebutton idle "gui/ui/setting/back.png" hover "gui/ui/setting/back_hover.png" xcenter 0.5 ycenter 0.95  action Hide("message")
    frame:
        background "gui/ui/setting/message_bg.png"

        at getIn

##第三个：
############
screen sound():
    use setting("sound")
    imagebutton idle "gui/ui/setting/back.png" hover "gui/ui/setting/back_hover.png" xcenter 0.5 ycenter 0.95  action Hide("sound")
    frame:
        background "gui/ui/setting/sound_bg.png"
        fixed:
            vbox:
                frame:
                    background "gui/ui/setting/touming.png"
                    xpos 180
                    yoffset 120
                    grid 1 3:
                        xcenter 0.2
                        spacing 109
                        if config.has_music:
                            bar value Preference("music volume"):
                                xsize 300
                                style "myslider"
                        if config.has_voice:
                            bar value Preference("voice volume"):
                                xsize 300
                                style "myslider"
                        if config.has_sound:
                            bar value Preference("sound volume"):
                                xsize 300
                                style "myslider"
                at getIn
##第四个：
###############
screen key():
    use setting("key")
    imagebutton idle "gui/ui/setting/back.png" hover "gui/ui/setting/back_hover.png" xcenter 0.5 ycenter 0.95  action Hide("key")
    frame:
        background "gui/ui/setting/key_bg.png"
        at getIn
###############################################################################
 #(3)书籍界面(已完工)
#############################
init python:
    choices = 0
# 在屏幕的定义之前导入CallInNewContext动作
screen book():
    tag menu
    add "gui/ui/book/book-x.png"
    imagebutton idle "gui/ui/book/text1.png" hover "gui/ui/book/text1a.png" xcenter 0.15 ycenter 0.362  action [SetVariable("choices", 1), Jump("choices_1")]
    imagebutton idle "gui/ui/book/text1.5.png" hover "gui/ui/book/text1.5a.png" xcenter 0.30 ycenter 0.362  action [SetVariable("choices", 1.5), Jump("choices_1_5")]
    imagebutton idle "gui/ui/book/text2.png" hover "gui/ui/book/text2a.png" xcenter 0.35 ycenter 0.344  action [SetVariable("choices", 2), Jump("choices_2")]
    imagebutton idle "gui/ui/book/text3.png" hover "gui/ui/book/text3a.png" xcenter 0.40 ycenter 0.362  action [SetVariable("choices", 3), Jump("choices_3")]
    imagebutton idle "gui/ui/book/text4.png" hover "gui/ui/book/text4a.png" xcenter 0.45 ycenter 0.362  action [SetVariable("choices", 4), Jump("choices_4")]
    imagebutton idle "gui/ui/book/text5-1.png" hover "gui/ui/book/text5-1a.png" xcenter 0.485 ycenter 0.358  action [SetVariable("choices", 5.1), Jump("choices_5_one")]
    imagebutton idle "gui/ui/book/text5-2.png" hover"gui/ui/book/text5-2a.png" xcenter 0.52 ycenter 0.358  action [SetVariable("choices", 5.2), Jump("choices_5_two")]
    imagebutton idle "gui/ui/book/text6.png" hover "gui/ui/book/text6a.png" xcenter 0.8 ycenter 0.362  action [SetVariable("choices", 6), Jump("choices_6")]
    imagebutton idle "gui/ui/book/text7.png" hover "gui/ui/book/text7a.png" xcenter 0.9 ycenter 0.362  action [SetVariable("choices", 7), Jump("choices_7")]

    imagebutton idle "gui/ui/book/text8.png" hover "gui/ui/book/text8a.png" xcenter 0.15 ycenter 0.77  action [SetVariable("choices", 8), Jump("choices_8")]
    imagebutton idle "gui/ui/book/text8.5.png" hover "gui/ui/book/text8.5a.png" xcenter 0.23 ycenter 0.77  action [SetVariable("choices", 8.5), Jump("choices_8_5")]
    imagebutton idle "gui/ui/book/text9.png" hover "gui/ui/book/text9a.png" xcenter 0.31 ycenter 0.77  action [SetVariable("choices", 9), Jump("choices_9")]
    imagebutton idle "gui/ui/book/text-fanwai.png" hover "gui/ui/book/text-fanwaia.png" xcenter 0.388 ycenter 0.77  action [SetVariable("choices", 9.5), Jump("choices_fanwai1")]
    imagebutton idle "gui/ui/book/text10.png" hover "gui/ui/book/text10a.png" xcenter 0.46 ycenter 0.77  action [SetVariable("choices", 10), Jump("choices_10")]
    imagebutton idle "gui/ui/book/text11.png" hover "gui/ui/book/text11a.png" xcenter 0.575 ycenter 0.77  action [SetVariable("choices", 11), Jump("choices_11")]
    imagebutton idle "gui/ui/book/text12.png" hover "gui/ui/book/text12a.png" xcenter 0.672 ycenter 0.77  action [SetVariable("choices", 12), Jump("choices_12")]
    imagebutton idle "gui/ui/book/text13-1.png" hover "gui/ui/book/text13-1a.png" xcenter 0.72 ycenter 0.77  action [SetVariable("choices", 13), Jump("choices_13")]
    imagebutton idle "gui/ui/book/text-fanwai2.png" hover "gui/ui/book/text-fanwai2a.png" xcenter 0.74 ycenter 0.77  action [SetVariable("choices", 14), Jump("choices_fanwai2")]
    imagebutton idle "gui/ui/book/text-fanwai3.png" hover "gui/ui/book/text-fanwai3a.png" xcenter 0.76 ycenter 0.77  action [SetVariable("choices", 15), Jump("choices_fanwai3")]
    imagebutton idle "gui/ui/book/text13-2.png" hover "gui/ui/book/text13-2a.png" xcenter 0.95 ycenter 0.77  action [SetVariable("choices", 16), Jump("choices_16")]
    imagebutton idle "gui/ui/book/backa.png" hover "gui/ui/book/backb.png" xcenter 0.5 ycenter 0.95 activate_sound "sound/click.ogg"  action MainMenu()
###################################################################################
###（4）壁纸模式（已完工）
##########################################################################################################
define chapter_wallpapers = [
    [1,2,3,4,17,18],
    [5,18,19,20,21,22,23],
    [6,5,18,19,20,2],
    [7,5,18,19,20,2],
    [8,5,18,19,20,2],
    [9,5,18,19,20,2],
    [10,5,18,19,20,2],
    [11,5,18,19,20,2],
    [12,5,18,19,20,2],
    [13,5,18,19,20,2],
    [14,5,18,19,20,2],
    [15,5,18,19,20,2],
    [16,5,18,19,20,2],
    [16,5,18,19,20,2,1,2,3,4,5]]
######################
screen combined_screen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 840
        pos (0, 0)
        use wallpaper_picture(chapter=1)
        imagebutton idle "gui/ui/setting/back.png" hover "gui/ui/setting/back_hover.png"  xcenter 0.65 ycenter 0.929 activate_sound "sound/click.ogg"  action Hide("combined_screen")
#####################
screen wallpaper_main():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 120
        pos (0, 0)
        add Solid("#000")
        add "gui/ui/wallpaper_mode/bg_main.png"
        viewport:
            scrollbars "vertical"
            vbox:
                spacing 2
                for i in range(1, 15):
                    imagebutton idle "gui/ui/wallpaper_mode/chapter_{}_idle.png".format(i) hover "gui/ui/wallpaper_mode/chapter_{}_hover.png".format(i):
                        xpos 5
                        ypos 30
                        action [Show("wallpaper_picture", chapter=i, transition=None)]
#####################
######################
default current_page = 1
screen wallpaper_picture(chapter):
    use wallpaper_main
    frame:
        xalign 0.0
        yalign 0.0
        xsize 960
        pos (120, 0)
        add Solid("#000")
        add "gui/ui/wallpaper_mode/bg_picture.png"
        imagebutton idle "gui/ui/wallpaper_mode/fanhuia.png" hover "gui/ui/wallpaper_mode/fanhuib.png" xcenter 0.10 ycenter 0.929 action Hide("wallpaper_picture")
        vbox:
            spacing 20
            xalign 0.0
            yalign 0.354
            grid 4 4:
                for i in chapter_wallpapers[chapter-1][(current_page-1)*16:current_page*16]:
                    frame:
                        background Frame("gui/ui/wallpaper_mode/frame.png", 10)
                        has hbox:
                            xalign 0.5
                            yalign 0.3
                            imagebutton idle "images/wallpaper/thumb.png" hover "images/wallpaper/thumb.png" action Show("wallpaper_fullscreen", wallpaper=i)
                for i in range(16 - len(chapter_wallpapers[chapter-1][(current_page-1)*16:current_page*16])):
                    null
        hbox:
            if current_page > 1:
                imagebutton idle "gui/ui/music_room/pre.png" hover "gui/ui/music_room/pre_hover.png" xpos 770 ypos 480 action SetVariable("current_page", current_page - 1)
            else:
                null
            imagebutton idle "gui/ui/music_room/next.png" hover "gui/ui/music_room/next_hover.png" xpos 780 ypos 480 action SetVariable("current_page", current_page + 1)
##############
#全屏幕查看
screen wallpaper_fullscreen(wallpaper):
    add Solid("#000")
    add "images/wallpaper/bg[wallpaper].png"
    imagebutton idle "gui/ui/setting/back.png" hover "gui/ui/setting/back_hover.png" xcenter 0.5 ycenter 0.95 activate_sound "sound/click.ogg" action Hide("wallpaper_fullscreen")
################################################################################
## (5)music_gallery音乐欣赏画面(已完工)
################################################################################
default pre_enabled = False
screen music_gallery(before=stopall):
    tag menu
    add "gui/ui/music_room/BG_load.png"
    vbox:
        spacing 20
        xalign  0.8
        yalign  0.321
        for i in range(page_index * songs_per_page, (page_index + 1) * songs_per_page):
            if i < len(songs):
                textbutton songs[i].name action Play("music", songs[i].file):
                    text_style "song_text_selected"

    imagebutton idle "gui/ui/setting/back.png" hover "gui/ui/setting/back_hover.png" xcenter 0.5 ycenter 0.95  action Return()
    imagebutton idle "gui/ui/music_room/play.png" hover "gui/ui/music_room/play_hover.png" xcenter 0.109 ycenter 0.88  action Stop("music")
    imagebutton idle "gui/ui/music_room/stop.png" hover "gui/ui/music_room/stop_hover.png" xcenter 0.235 ycenter 0.88  action Stop("music")
    imagebutton idle "gui/ui/music_room/next.png" hover "gui/ui/music_room/next_hover.png" xcenter 0.90 ycenter 0.90 action [SetVariable("page_index", page_index + 1), SetVariable("pre_enabled", True)]
    imagebutton idle "gui/ui/music_room/pre.png" hover "gui/ui/music_room/pre_hover.png" xcenter 0.85 ycenter 0.90 sensitive pre_enabled action [SetVariable("page_index", page_index - 1), If(page_index == 1, SetVariable("pre_enabled", False))]
style song_text_selected:
    color "#F8F8FF"
    size 20
    font "tl/test.ttf"
################################################################################
 #(5)主标题菜单的子菜单(已完工)
## #############################################################################
image green ="gui/ui/green.png"
image snow = SnowBlossom("green",count=40,border=10,xspeed=(-2,50),yspeed=(20,30),start=0, fast =True,horizontal=False)
screen screen_main(before=stopall):
    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu
    add "gui/ui/title_bg1.png"
    add "gui/ui/main/title_titlelogo1.png" xcenter 0.5 ycenter 0.32
    add "snow"
    frame:
        style "main_menu_frame"
    vbox:
        spacing 10
        xalign  0.5
        yalign  0.85
        imagebutton idle "gui/ui/main_screen/book.png" hover "gui/ui/main_screen/book_hover.png" activate_sound "sound/click.ogg" action Start()
        imagebutton idle "gui/ui/main_screen/picture.png" hover "gui/ui/main_screen/picture_hover.png"  activate_sound "sound/click.ogg" action ShowMenu("combined_screen")
        imagebutton idle "gui/ui/main_screen/music.png" hover "gui/ui/main_screen/music_hover.png" activate_sound "sound/click.ogg" action ShowMenu("music_gallery")
        imagebutton idle "gui/ui/main_screen/back.png" hover "gui/ui/main_screen/back_hover.png" activate_sound "sound/click.ogg" action Return()
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 210
    yfill True
style main_menu_vbox:
    xalign 1.0
    xoffset -15
    xmaximum 600
    yalign 1.0
    yoffset -15

################################################################################
 #(6)主标题菜单(已完工)
## #############################################################################
image green ="gui/ui/green.png"
image snow = SnowBlossom("green",count=40,border=10,xspeed=(-2,50),yspeed=(20,30),start=0, fast =True,horizontal=False)
screen main_menu(before=stopall):
    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu
    add "gui/ui/title_bg1.png"
    add "gui/ui/main/title_titlelogo1.png" xcenter 0.5 ycenter 0.32
    add "snow"
    frame:
        style "main_menu_frame"
    vbox:
        spacing 10
        xalign  0.5
        yalign  0.85
        imagebutton idle "gui/ui/main/start.png" hover "gui/ui/main/start_hover.png" activate_sound "sound/click.ogg"  action Start()
        imagebutton idle "gui/ui/main/load.png" hover "gui/ui/main/load_hover.png" activate_sound "sound/click.ogg"  action ShowMenu("load")
        imagebutton idle "gui/ui/main/setting.png" hover "gui/ui/main/setting_hover.png"  activate_sound "sound/click.ogg" action ShowMenu("setting")
        imagebutton idle "gui/ui/main/extra.png" hover "gui/ui/main/extra_hover.png" activate_sound "sound/click.ogg" action ShowMenu("screen_main")

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 210
    yfill True
style main_menu_vbox:
    xalign 1.0
    xoffset -15
    xmaximum 600
    yalign 1.0
    yoffset -15
################################################################################
## （7）关于界面 （待修改）
################################################################################
##
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此界面没有什么特别之处，因此它也是如何制作自定义界面的一个例子。
screen about():
    tag menu









###############################################################################
## （8）读取和保存界面  （已修改）
################################################################################
transform getIn:
    xoffset -40
    yoffset 0
    alpha 0.0
    easein 0.35 xoffset 0 alpha 1.0
##########################
screen save():
    tag menu
    use file_slots(_("保存"))
screen load():
    tag menu
    use file_slots(_("读取游戏"))
screen file_slots(title):
    add "gui/ui/load/load_bg.PNG"
    imagebutton idle "gui/ui/setting/back.png" hover "gui/ui/setting/back_hover.png" xcenter 0.71 ycenter 0.92  action Return()
    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))
    fixed at getIn:
        order_reverse True
        button:
            style "page_label"
            key_events True
            xalign 0.5
            action page_name_value.Toggle()
            input:
                style "page_label_text"
                value page_name_value
        ## 存档位网格。
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"
            xalign 0.235
            yalign 0.45
            spacing 20
            for i in range(gui.file_slot_cols * gui.file_slot_rows):
                $ slot = i + 1
                button:
                    action FileAction(slot)
                    has vbox
                    add FileScreenshot(slot) xalign 0.5
                    text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                        style "slot_time_text"
                    text FileSaveName(slot):
                        style "slot_name_text"
                    key "save_delete" action FileDelete(slot)
        hbox:
            style_prefix "page"
            xalign 0.42
            yalign 0.94
            spacing 30

            ## “range(1, 10)”给出 1 到 9 之间的数字。
            for page in range(1, 5):
                textbutton "[page]" style "my_textbutton_style" activate_sound "sound/click.ogg" action FilePage(page)

style my_textbutton_style:
    text_align 0.5
    idle_color "#ffffff" # 文字颜色为白色
    hover_color "#ffff00" # 鼠标悬停时的文字颜色为黄色
style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
style page_label:
    xpadding 38
    ypadding 3
style page_label_text:
    text_align 0.5
    layout "subtitle"
style page_button:
    properties gui.button_properties("page_button")
style page_button_text:
    properties gui.button_text_properties("page_button")
style slot_button:
    properties gui.button_properties("slot_button")
style slot_button_text:
    properties gui.button_text_properties("slot_button")
###############################################################################
## （9）旧版设置界面
########################################################################
screen preferences():
    tag menu
    use game_menu(_("设置"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "radio"
                    label _("回退操作区")
                    textbutton _("禁用") action Preference("rollback side", "disable")
                    textbutton _("屏幕左侧") action Preference("rollback side", "left")
                    textbutton _("屏幕右侧") action Preference("rollback side", "right")
                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续") action Preference("after choices", "toggle")
                    textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))
                ## 可以在此处添加类型为“radio_pref”或“check_pref”的其他“vbox”，
                ## 以添加其他创建者定义的首选项设置。
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("文字速度")
                    bar value Preference("text speed")
                    label _("自动前进时间")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("音乐音量")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("音效音量")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("语音音量")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2
style pref_label_text:
    yalign 1.0
style pref_vbox:
    xsize 169
style radio_vbox:
    spacing gui.pref_button_spacing
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
style radio_button_text:
    properties gui.button_text_properties("radio_button")
style check_vbox:
    spacing gui.pref_button_spacing
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style check_button_text:
    properties gui.button_text_properties("check_button")
style slider_slider:
    xsize 263
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 8
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_vbox:
    xsize 338
###############################################################################
## （10）旧版帮助界面
########################################################################
screen help():
    tag menu
    default device = "keyboard"
    use game_menu(_("帮助"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 12
            hbox:
                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")
                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
screen keyboard_help():
    hbox:
        label _("回车")
        text _("推进对话并激活界面。")
    hbox:
        label _("空格")
        text _("推进对话但不激活选项。")
    hbox:
        label _("方向键")
        text _("导航界面。")
    hbox:
        label _("Esc")
        text _("访问游戏菜单。")
    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")
    hbox:
        label _("Tab")
        text _("切换对话快进。")
    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")
    hbox:
        label _("Page Down")
        text _("向前至之后的对话。")
    hbox:
        label "H"
        text _("隐藏用户界面。")
    hbox:
        label "S"
        text _("截图。")
    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")
    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")
screen mouse_help():
    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")
    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")
    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")
    hbox:
        label _("鼠标滚轮上\n点击回退操作区")
        text _("回退至先前的对话。")
    hbox:
        label _("鼠标滚轮下")
        text _("向前至之后的对话。")
screen gamepad_help():
    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")
    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")
    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")
    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")
    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")
    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")
    textbutton _("校准") action GamepadCalibrate()
style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text
style help_button:
    properties gui.button_properties("help_button")
    xmargin 6
style help_button_text:
    properties gui.button_text_properties("help_button")
style help_label:
    xsize 188
    right_padding 15
style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
################################################################################
## 3.其他界面
################################################################################
## （1）确认界面(已修改) ########################################################################
##
## 当 Ren'Py 需要询问玩家有关确定或取消的问题时，会调用确认界面。
transform gettn:
    xoffset -40
    yoffset 0.5
    alpha 0.0
    easein 0.5 xoffset 0.5 alpha 1.0
screen confirm(message, yes_action, no_action):
    ## 显示此界面时，确保其他界面无法输入。
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame at gettn :
        vbox:
            xalign .5
            yalign .5
            spacing 23
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 75
                imagebutton idle "gui/ok.png" hover "gui/ok2.png" activate_sound "sound/click.ogg"   action yes_action
                imagebutton idle "gui/cancel.png" hover "gui/cancel2.png" activate_sound "sound/click.ogg"   action no_action
    key "game_menu" action no_action
style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text
style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    color "#ffffff"
style confirm_button:
    properties gui.button_properties("confirm_button")
style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
## （2）快进指示界面 ######################################################################
##
## “skip_indicator”界面用于指示快进正在进行中。
##
## https://www.renpy.cn/doc/screen_special.html#skip-indicator
screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 5
            text _("正在快进")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text
style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding
style skip_text:
    size gui.notify_text_size
style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"

#############################################################################
## （3）通知界面
########################################################################
## 通知界面用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    timer 3.25 action Hide('notify')
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
style notify_frame is empty
style notify_text is gui_text
style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
style notify_text:
    properties gui.text_properties("notify")
## 4.NVL 模式界面 ####################################################################
## 此界面用于 NVL 模式的对话和菜单。
## https://www.renpy.cn/doc/screen_special.html#nvl
screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing
        ## 在“vpgrid”或“vbox”中显示对话框。
        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)
        else:
            use nvl_dialogue(dialogue)
        ## 如果给定，则显示“menu”。 如果“config.narrator_menu”设置为“True”，
        ## 则“menu”可能显示不正确，如前述。
        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"
    add SideImage() xalign 0.0 yalign 1.0
screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            fixed:
                yfit gui.nvl_height is None
                if d.who is not None:
                    text d.who:
                        id d.who_id
                text d.what:
                    id d.what_id
## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length
style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text
style nvl_window:
    xfill True
    yfill True
    background "gui/nvl.png"
    padding gui.nvl_borders.padding
style nvl_entry:
    xfill True
    ysize gui.nvl_height
style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign
style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign
style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
