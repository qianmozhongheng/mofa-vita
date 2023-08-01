#################################
$ forbid_saving = True

##人物：
define a = Character("角色a",what_font="tl/test.ttf", what_size=32, color="#ff0000",  kind=nvl)
define narrator = nvl_narrator
# 定义一个Movie显示对象，设置它的大小和忽略点击属性






########################################################
###视频：
image logo = Movie(size=(960, 544), play="audio/logo.webm",ignore_clicks=True, loop=0)
image xuqu = Movie(play="audio/chapter1/xuqu.webm", image="images/picture/chapter1/bg3_51_4.jpg",ignore_clicks=True, loop=0)
image chapter1_1_1 = Movie(play="audio/chapter1/chapter1_1_1.webm", image="images/picture/chapter1/bg1_12.jpg", ignore_clicks=True,loop=0)
image chapter1_1_2 = Movie(play="audio/chapter1/chapter1_1_2.webm", image="images/picture/chapter1/bg1_10.jpg", ignore_clicks=True,loop=0)
image chapter1_1_5 = Movie(play="audio/chapter1/chapter1_1_5.webm", image="images/picture/chapter1/bg3_52.jpg",ignore_clicks=True, loop=0)
image chapter1_1_6 = Movie(play="audio/chapter1/chapter1_1_6.webm", image="images/picture/chapter1/bg3_53.jpg", ignore_clicks=True,loop=0)
image chapter1_1_7 = Movie(play="audio/chapter1/chapter1_1_7.webm", image="images/picture/chapter1/bg3_54.jpg", ignore_clicks=True,loop=0)
image chapter1_1_8 = Movie(play="audio/chapter1/chapter1_1_8.webm", image="images/picture/chapter1/bg3_173.jpg", ignore_clicks=True,loop=0)
image chapter1_1_4 = Movie(size=(960, 544), ignore_clicks=True, play="audio/chapter1/chapter1_1_4.webm",loop=0)

###################################################################
#####################################################################
###转场动画：
transform move:
    linear 1.0 xoffset 100
transform shake:
    xoffset 0
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    repeat 10
transform move_from_right:
    xalign 1.0
    linear 100.0 xalign 0.0
transform move_from_bottom:
    yalign 1.0
    linear 100.0 yalign 0.0
transform move_from_right_fast:
    xalign 1.0
    linear 10.0 xalign 0.0
transform move_from_right_superfast:
    xalign 1.0
    linear 1.0 xalign 0.0
transform move_from_bottom_fast:
    yalign 1.0
    linear 10.0 yalign 0.0
################################################################################
image bg1_4 = Animation("images/picture/chapter1/bg1_4_1.jpg", 0.5, "images/picture/chapter1/bg1_4_2.jpg", 0.5)
image bg1_5 = Animation("images/picture/chapter1/bg1_5_1.jpg", 0.5, "images/picture/chapter1/bg1_5_2.jpg", 0.5)
image bg1_6 = Animation("images/picture/chapter1/bg1_6_1.jpg", 0.5, "images/picture/chapter1/bg1_6_2.jpg", 0.5)
image bg1_7 = Animation("images/picture/chapter1/bg1_7_1.jpg", 0.5)
image bg1_8 = Animation("images/picture/chapter1/bg1_8_1.jpg", 0.5, "images/picture/chapter1/bg1_8_2.jpg", 0.5)
image bg1_9 = Animation("images/picture/chapter1/bg1_9_1.jpg", 0.5, "images/picture/chapter1/bg1_9_2.jpg", 0.5)
image bg1_11 = Animation("images/picture/chapter1/bg1_11_1.jpg", 0.5, "images/picture/chapter1/bg1_11_2.jpg", 0.5)
image bg2_6:
    "images/picture/chapter1/bg2_6.jpg"
    xpos -1.0
    align (0.0, 0.5)
    linear 5.0 xpos 0.0
##################################################################################
label start():
    call screen book with dissolve
    pause
    return
################################################################################
##########流转标签：
#################################################################################
label choices_1():
    call screen choices_1
    return
label choices_1_5():
    call screen choices_1_5
    return
label choices_2():
    call screen choices_2
    return
label choices_3():
    call screen choices_3
    return
label choices_4():
    call screen choices_4
    return
label choices_5_one():
    call screen choices_5_one
    return
label choices_5_two():
    call screen choices_5_two
    return
label choices_6():
    call screen choices_6
    return
label choices_7():
    call screen choices_7
    return
label choices_8():
    call screen choices_8
    return
label choices_8_5():
    call screen choices_8_5
    return
label choices_9():
    call screen choices_9
    return
label choices_fanwai1():
    call screen choices_fanwai1
    return
label choices_10():
    call screen choices_10
    return
label choices_11():
    call screen choices_11
    return
label choices_12():
    call screen choices_12
    return
label choices_13():
    call screen choices_13
    return
label choices_fanwai2():
    call screen choices_fanwai2
    return
label choices_fanwai3():
    call screen choices_fanwai3
    return
label choices_16():
    call screen choices_16
    return
#################################################################################
label story_1_1:
    nvl clear
    show screen xyz with  dissolve
    stop music
    scene black with  dissolve
    show bg1_1 with dissolve
    narrator ""
    narrator ""
    narrator "成为那个孩子的影子，是在8年前的那个冬天。" with dissolve
    narrator ""
    narrator ""
    narrator "那是在她初次接触到生命的肃穆早晨发生的事。" with dissolve
    hide bg1_1
    nvl clear
    show bg1_2 with  dissolve
    hide bg1_2 with dissolve
    show bg1_4 with dissolve
    play music "music/M19.OGG" fadein 1.0 fadeout 2.0
    narrator ""
    narrator ""
    narrator "她的家在山腰上。" with dissolve
    narrator ""
    narrator "周围是一片荒地。" with dissolve
    narrator "根本不能指望有什么住在附近的青梅竹马，上学或是出去玩也极为不便。" with dissolve
    hide bg1_4
    nvl clear
    show bg1_5 with dissolve
    narrator ""
    narrator ""
    narrator "但是，水很清澈，星星也很美丽" with dissolve
    narrator "是一个让人有些许不满，却又非常安逸"with dissolve
    narrator "能让人永远铭记的家。"with dissolve
    narrator "      " with dissolve
    nvl clear
    show bg1_6 with dissolve
    narrator ""
    narrator ""
    narrator "不过，这也仅限于在夏天。      " with dissolve
    narrator "山里的冬天气温很低，早上总是冷得要命。" with dissolve
    narrator "虽然父亲会用车送她到车站，" with dissolve
    narrator "但车窗总是结了一层厚厚的霜，在出门前必须提早几十分钟发动引擎，不然就开不动。" with dissolve
    hide bg1_6
    nvl clear
    show bg1_7 with dissolve
    narrator ""
    narrator ""
    narrator "「-----,能帮我启动下引擎吗？”」 " with dissolve
    narrator "父亲在享受饭后咖啡的时候，出门去发动引擎是她每天的工作。" with dissolve
    narrator "走到门外，呵着白气穿过院子，打开老爷车的门。" with dissolve
    narrator "和往常一样插入钥匙转了一圈，" with dissolve
    narrator "引擎噗噜噜地震动起来。" with dissolve
    narrator "就在做完这件已经重复了几十次，让幼小的自己引以自豪的工作时――" with dissolve
    nvl clear
    narrator ""
    narrator "「-------!!!!!!!」 " with dissolve
    narrator "一阵尖利的惨叫响起。" with dissolve
    narrator "那微弱的声音虽然并非人类的话语，但在她听来，却如同在哭叫着痛苦似的。" with dissolve
    narrator "几分钟后。" with dissolve
    narrator "呜------，引擎发动了。" with dissolve
    narrator "父亲打开汽车的前盖，在其中看到了一个小小的生命。" with dissolve
    hide bg1_7
    nvl clear
    show bg1_8 with dissolve
    narrator ""
    narrator "嘎吱嘎吱的轮带， " with dissolve
    narrator "怪物一般的引擎，" with dissolve
    narrator "这些东西将整个箱子塞得满满当当。" with dissolve
    narrator "而那只看上去像是母亲的猫，以及那两只小猫，显得如此的格格不入。" with dissolve
    narrator ""
    narrator "三只猫在引擎室里仿若相依相偎一般地缩成一团。" with dissolve
    nvl clear
    narrator ""
    narrator "母猫没有了脖子以上的部分。" with dissolve
    narrator "一只小猫大部分被机械轮带卷住，一动都不动。应该是死亡了吧？"
    narrator "剩下的那只小猫半张脸染满了鲜血，像是被雨打湿的狗一样，呼呼喘着气。" with dissolve
    narrator "小猫拼命地想要靠近那具尸骸" with dissolve
    narrator "不，应该说是有一半都成了肉片的母猫" with dissolve
    narrator "用那大概只剩几分钟的生命拼命地往母亲的怀里钻。" with dissolve
    narrator "「真可怜---」" with dissolve
    nvl clear
    narrator ""
    narrator "　父亲仿佛是在为它们悲叹。" with dissolve
    narrator "昨晚气温急剧下降。"
    narrator "这些猫是在父亲开车回来后，大概是被引擎的暖气所吸引而躲进前车盖的。" with dissolve
    narrator "它们在引擎盖下熬过了一晚，" with dissolve
    narrator "  " with dissolve
    narrator "第二天早上被卷进轮带里才醒来。" with dissolve
    narrator "气密性差的80年代轿车，似乎经常会发生这种事。" with dissolve
    hide bg1_8
    nvl clear
    show bg1_9 with dissolve
    narrator ""
    narrator "「―――没关系的。不是　　的错。」 " with dissolve
    narrator " 父亲这么说着就走了。" with dissolve
    narrator "她对父亲的话语恍若未闻。" with dissolve
    narrator "小猫有着一身毛茸茸的灰毛。" with dissolve
    narrator "上面有着母亲和兄弟的血，还有被削去一半身体的自己的血，" with dissolve
    narrator "―――啊，圆圆的头盖骨都露出来了―――" with dissolve
    narrator "小生命被血染成灰红斑驳。" with dissolve
    narrator "不知是不是因为已经看不见了，小猫一边发抖，一边拼命钻进已死的母亲怀里。" with dissolve
    hide bg1_8
    nvl clear
    show bg1_2 with  dissolve
    pause
    hide bg1_2 with dissolve
    show bg1_6 with dissolve
    narrator ""
    narrator "「......等等」 " with dissolve
    narrator ""
    narrator "她抱起了小猫。" with dissolve
    narrator "向与她一家分居住在深山中的祖父那里跑去。" with dissolve
    narrator "是因为后悔而内心动摇呢？" with dissolve
    narrator "还是由于悲伤而混乱了呢？老实说，她直到现在都不清楚。" with dissolve
    narrator "她拼命忍住涌上来的眼泪，跑进了祖父的工房。" with dissolve
    nvl clear
    narrator ""
    narrator "祖父是魔法使，没有他办不到的事情。" with dissolve
    narrator ""
    narrator "她自己虽然没见过什么「魔法」，而且明白这是童话里的空想，但她也知道，祖父是那种不能以常识作为基准来衡量的人。 " with dissolve
    narrator ""
    narrator "所以....." with dissolve
    narrator "     "
    narrator "祖父一定能救活它。" with dissolve
    hide bg1_6
    nvl clear
    show bg1_10 with dissolve
    narrator ""
    narrator ""
    narrator "「你的意思是要我改变这只小猫的命运?」  " with dissolve
    narrator " 住在洞窟里的魔法使用冷漠的口气说道。 " with dissolve
    nvl clear
    hide bg1_10
    show bg1_11 with dissolve
    narrator ""
    narrator ""
    narrator "「求你了!」 " with dissolve
    narrator " 她恳求道。"
    narrator "魔法使既没说这是小事一桩，也没说这是会改变世界的大事" with dissolve
    narrator "就如机械一般爽快地实现了她任性的愿望。" with dissolve
    hide bg1_11
    nvl clear
    scene bg1_2
###########################
    show screen my_scr
    $ renpy.movie_cutscene("audio/chapter1/chapter1_1_1.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/chapter1/chapter1_1_1_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    show bg1_12
############################
    play music "sound/se13010.ogg" fadein 1.0 fadeout 2.0
    narrator ""
    narrator "「啊」 " with dissolve
    narrator ""
    narrator "回过神来的时候，她手中拿着一个小小的遗骸。" with dissolve
    narrator "毛皮无比冰冷。" with dissolve
    narrator "早已失去了生命的温度。" with dissolve
    narrator "　强忍住的眼泪从眼中零落。" with dissolve
    narrator "心中充满犹如灰色天空一般无垠而巨大的悔意。" with dissolve
    narrator "「只是徒劳啊。怎么可能恢复原状呢？」" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "她无法理解到底发生了什么。" with dissolve
    narrator "这十分钟的空白里经历了什么，" with dissolve
    narrator "遇见了谁，" with dissolve
    narrator "甚至连知道了什么，都已经恢复原状，显得如此地不负责任。" with dissolve
    narrator "可以确定的，那就是即将死去的生命无法挽回，" with dissolve
    narrator "「请问―――有谁在那边吗？」" with dissolve
    hide bg1_12 with dissolve
    nvl clear
    scene black with  dissolve
    narrator ""
    narrator ""
    narrator "以及那一天，" with dissolve
    narrator "“我”这个错误从她身上诞生。" with dissolve
    stop music
    play music "music/M19.OGG" fadein 1.0 fadeout 2.0
    narrator "啊啊……" with dissolve
    narrator "不管如何，" with dissolve
    narrator "这都是让人怀念的遥远往事了。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "这就是8年前的那场童话。" with dissolve
    narrator "无论使用什么魔法都无法挽回的，她们初次邂逅的那一天。" with dissolve
    nvl clear
    show screen my_scr
    $ renpy.movie_cutscene("audio/chapter1/chapter1_1_2.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/chapter1/chapter1_1_2_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    show bg1_10
    pause
    narrator ""
    narrator ""
    narrator "傲慢，贪婪，除了破坏一无所长，" with dissolve
    narrator "我一定是狼吧。" with dissolve
    narrator "撞到南墙也绝不回头，" with dissolve
    narrator "如果从哪天起，真的变成一匹独狼的话，那我也只能说抱歉了。" with dissolve
    nvl clear
    show black
    narrator ""
    narrator ""
    narrator "反正不管如何，" with dissolve
    narrator "最后总是会被小红帽轻松解决吧----。" with dissolve
    nvl clear
    hide black with  dissolve
    hide screen xyz with  dissolve
    stop music
    return
###########################################################################
label story_1_2:
    nvl clear
    show screen xyz with  dissolve
    stop music
    scene black with  dissolve
    show bg2_1 with Dissolve(4)
    pause
    hide bg2_1 with Dissolve(4)
    pause
    play music "sound/se01003.ogg" fadein 1.0 fadeout 2.0
    pause
    show bg2_2 with Dissolve(3)
    pause
    hide bg2_2 with Dissolve(3)
    stop music
    show bg2_3 with Dissolve(3)
    play music "sound/se01001.ogg" fadein 1.0 fadeout 2.0
    pause
    narrator ""
    narrator ""
    narrator "那是一个静谧的早晨。" with dissolve
    narrator "即使从床上能看到天空仿佛被染料涂鸦成了灰色" with dissolve
    narrator "即使温度计上显示着六度左右这个即使在十一月也显得相当低的数值|记录" with dissolve
    nvl clear

    narrator ""
    narrator ""
    narrator "即使早已过了吃早饭的时候，很可耻地因为肚子饿而醒来――" with dissolve
    narrator "但光是能这样悠闲地睡着，对她来说，这就是一个幸福的早晨。"with dissolve

    pause
    stop music
    scene black with  dissolve
    nvl clear
    pause
    play music "sound/se01003.ogg" fadein 1.0 fadeout 2.0
    show bg2_4 with Dissolve(3)
    narrator ""
    narrator ""
    narrator "时针早就过了早晨八点。" with dissolve
    narrator "在平时这样的时间已经会让人绝望，不管怎么挣扎都绝对会迟到，但今天是建校纪念日因此放假了。" with dissolve
    narrator "也多亏了这样，她才能享受一个难得的悠闲早晨。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "必须重复一次，窗外是忧郁的灰铁色，让人觉得不像是早晨而像是傍晚。" with dissolve
    narrator "即使是说得再好听，也无法将其称之为心旷神怡的早晨。"with dissolve
    nvl clear
    narrator ""
    narrator "但，对于三小时前还在熬夜的她来说，外面的天气都无所谓了。" with dissolve
    narrator "现在睡意就是一切。"with dissolve
    narrator "能在床上打个盹就能让人心旷神怡，于是窗外的情况都被她隔绝在外，表示当局不干涉一切外部事务。"with dissolve
    nvl clear
    pause
    show bg2_5 with Dissolve(3)
    pause
    play sound "sound/se01011.ogg"
    show bg2_6 with Dissolve(3)
    narrator ""
    narrator ""
    pause
    narrator "拉上窗帘" with dissolve
    stop music
    nvl clear
    play music "sound/se01001.ogg" fadein 1.0 fadeout 2.0
    hide bg2_6
    hide bg2_5
    show bg2_7 with Dissolve(3)
    play sound "sound/se01009.ogg"
    narrator ""
    narrator ""
    narrator "再次闭上眼睛，努力地想要迅速地回到睡眠中。" with dissolve
    play sound "sound/se01010.ogg"
    narrator "“愿我能至少再做两个小时平凡的梦吧……”"with dissolve
    nvl clear
    show bg2_8 with Dissolve(3)
    narrator ""
    narrator ""
    narrator "睡意还很强烈，幸福马上就到来了。"
    narrator "意识渐渐下沉。" with dissolve
    narrator "“可是，”"with dissolve
    narrator "她那渺小的愿望，却被无情地否定了。"with dissolve
    play sound "sound/se01007.ogg"
    hide bg2_8 with Dissolve(2)
    nvl clear
    show bg2_7 with Dissolve(3)
    narrator ""
    narrator ""
    narrator "叮铃铃铃---"
    play sound "sound/se01008.ogg"
    narrator "声音虽小，却尖锐地传入耳中。" with dissolve
    narrator "是电话铃声没错。"with dissolve
    narrator "似乎已经习惯成自然了。刚闭上的双眼违背了她的意志猛然张开。" with dissolve
    narrator "“真是的，偏偏在这种日子里……”"
    nvl clear
    play sound "sound/se01008.ogg"
    narrator ""
    narrator ""
    narrator "电话放在一楼前厅。" with dissolve
    narrator "与这个房间相隔着十米的走廊，以及一层楼梯。" with dissolve
    narrator "对睡眠不足的她来说，这个距离比“苦海彼岸”近一些，又比“前路漫漫”远一点。" with dissolve
    nvl clear
    hide bg2_7 with Dissolve(3)
    scene black with  dissolve
    play sound "sound/se01008.ogg"
    narrator ""
    narrator ""
    narrator "电话铃声仍然孜孜不倦地响着。"with dissolve
    narrator "虽然只要无视掉的话，迟早是会停的，但她还没对自己放纵到能做出这种事。" with dissolve
    nvl clear
    hide black
    ####################################
    play movie "audio/chapter1/chapter1_1_3.webm"
    $ renpy.pause(3)
    ##########################################
    scene black
    show bg2_9
    play sound "sound/se01008.ogg"
    narrator ""
    narrator ""
    narrator "「有珠，你就不去接下电话吗？」"with dissolve
    narrator "她依依不舍地试着期待下同居人的表现，但马上就放弃了。" with dissolve
    narrator "仔细想想，休息的只有自己学校那里，同居人则是小丘上那个学院的大小姐。早就去学校了。"with dissolve
    narrator "               "
    nvl clear
    hide bg2_9 with Dissolve(3)
    show bg2_10 with Dissolve(3)
    stop music
    play music "sound/se01004.ogg" fadein 1.0 fadeout 2.0
    play sound "sound/se01008.ogg"
    narrator ""
    narrator ""
    narrator "电话铃声仍然不厌其烦地响着。"with dissolve
    narrator "由于实在太烦，感觉声音听起来更响了。" with dissolve
    narrator "「啊啊啊，真是的，好不容易能睡个懒觉……」"with dissolve
    narrator "               "
    nvl clear
    stop music
    hide bg2_10 with Dissolve(3)
    show bg2_11 with dissolve
    narrator ""
    narrator ""
    play music "sound/se01001.ogg" fadein 1.0 fadeout 2.0
    play sound "sound/se01010.ogg"
    narrator ""
    narrator "她无奈地爬出被窝"with dissolve
    play sound "sound/se01013.ogg"
    narrator "披上一件外套"
    narrator "离开了屋子"
    play sound "sound/se01014.ogg"
    play music "sound/se01004a.ogg" fadein 1.0 fadeout 2.0
    nvl clear
    hide bg2_11 with dissolve
    show bg1_2 with Dissolve(3)
    show bg2_12 with Dissolve(3)
    narrator ""
    narrator ""
    narrator "「呼，真冷……」"with dissolve
    play sound "sound/se01008.ogg"
    narrator "合起手来暖和一下冻僵的手指。" with dissolve
    narrator " 这座房子的供暖很差。" with dissolve
    narrator " 因此，冬天的气温是可怕的强敌。 " with dissolve
    hide bg2_12
    nvl clear
    show bg2_13 with Dissolve(3)
    play sound "sound/se01008.ogg"
    narrator ""
    narrator ""
    narrator "在这个阴云笼罩的早晨更是如此，就算不看温度计，她也清楚此时如隆冬一般寒冷。"with dissolve
    narrator "这栋房子坐落在深山，周围是范围不小的老林，所以冬天要比镇上来得更早。" with dissolve
    hide bg2_13 with Dissolve(3)
    nvl clear
    show bg2_12 with Dissolve(3)
    play sound "sound/se01008.ogg"
    narrator ""
    narrator ""
    narrator "长长的走廊里回响着枯燥的铃声。"with dissolve
    narrator "馆内的家具虽然打扫得还算干净，但却感觉不到生活的气息。" with dissolve
    narrator " 感觉不到豪华，反而是凸显了孤寂。" with dissolve
    narrator " 在加上昏暗的早晨，简直会让人以为这里是个鬼屋。 " with dissolve
    hide bg2_12
    nvl clear
    show bg2_14 with Dissolve(3)
    play sound "sound/se01008.ogg"
    narrator ""
    narrator ""
    narrator " 「……嗯，本来就是个鬼屋嘛。"
    narrator "而且只是两个人住的话，这个家实在太大了。」"with dissolve
    narrator "电话已经响了三十多声了。" with dissolve
    narrator " 是对方实在太闲呢，还是因为很清楚这个家的情况呢。……" with dissolve
    narrator " 抬头仰望，窗口透出了忧郁的颜色。" with dissolve
    hide bg2_14
    nvl clear
    show bg2_15 at Move((0.5, -0.2), (0.5, 0.5), 10, xanchor=0.5, yanchor=0.5)
    show nvx with dissolve
    play sound "sound/se01008.ogg"
    narrator ""
    narrator ""
    narrator "她仿佛像是要将这完全不知自重为何物的电话铃声逮捕似地加快了脚步。"with dissolve
    play sound "sound/se01015.ogg"
    pause
    narrator "同时她也预感到，在抓住的瞬间，幸福的早晨将会化为泡影。" with dissolve
    play sound "sound/se01008.ogg"
    hide nvx with dissolve
    pause
    narrator ""
    narrator ""
    hide bg2_15 with Dissolve(3)
    nvl clear
    show bg2_16 with Dissolve(3)
    narrator ""
    narrator ""
    narrator "总之，这就是那一系列事件的起点。"with dissolve
    narrator "是有点缺乏诗意，不过还请多多包涵。" with dissolve
    narrator "根据统计，或者是一般来说，" with dissolve
    narrator " 大部分的故事，都是这样平凡、平稳地开始的―――　　" with dissolve
    hide bg2_16
    nvl clear
    show screen my_scr
    $ renpy.movie_cutscene("audio/chapter1/chapter1_1_4.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/chapter1/chapter1_1_4_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    stop music
    pause
    hide screen xyz with  dissolve
    return
label story_1_3:
    nvl clear
    stop music
    show screen xyz with  dissolve
    scene bg1_2 with Dissolve(3)
    show bg3_1 with Dissolve(3)
    play music "sound/se01004b.ogg" fadein 1.0 fadeout 2.0
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "当她到达正门的时候，雨势已经变小了。"with dissolve
    narrator "远方的天空隐约能看到阳光" with dissolve
    narrator "照着势头，过了中午雨也许就会停了" with dissolve
    nvl clear
    hide nvx with dissolve
    show bg3_2 with Dissolve(3)
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "「-----话虽如此，这和我没关系就是了」"with dissolve
    narrator "与天气相反，她的运气是一塌糊涂" with dissolve
    narrator "不但在通宵后的早晨被叫起床，还碰上一场冬雨" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_3 with Dissolve(3)
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "这样看来，摊上的十有八九也不是什么正经事"with dissolve
    narrator "          "
    narrator "她一边对这种预感觉得头疼，一边穿过正门向校舍走去" with dissolve
    narrator "        "
    hide nvx with dissolve
    nvl clear
    show bg3_4 at move_from_right
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "途中没遇到任何学生"with dissolve
    play sound "sound/se01022a.ogg" fadein 1.0 fadeout 2.0
    narrator "也没看到有什么人在进行社团活动" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_5 at move_from_bottom
    show nvx with dissolve
    narrator ""
    narrator " 教职工大门的接待处竖着“休息中” 的板子     " with dissolve
    narrator " 学校给与学生们平等的假日     " with dissolve
    narrator " 当然，这个时候还被叫出来的她不算     " with dissolve
    narrator " 这个事实让她越发地生气     " with dissolve
    hide nvx with dissolve
    nvl clear
    play sound "sound/se01025.ogg"
    pause
    play sound "sound/se01017.ogg"
    show bg3_6 with Dissolve(3)
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "她打开职员室的门，一个熟悉的老师正坐在桌前。"with dissolve
    narrator "穿着质朴而笔挺的衬衫与西装，" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "一副温和的样子，但却戴着不敢小瞧的细框眼镜"with dissolve
    narrator "这是一个吸着与他形象不符的香烟，年纪在25岁上下的文雅男人。" with dissolve
    narrator "看来他还没察觉她的到来" with dissolve
    nvl clear
    narrator ""
    narrator ""
    play sound "sound/se01018.ogg"
    narrator "「-山城老师」"with dissolve
    narrator "她用力关上门" with dissolve
    narrator "这个叫山城的老师听到了声音也没感到吃惊，抬起了头"with dissolve
    hide nvx with dissolve
    nvl clear
    stop music
    show bg3_7 with dissolve
    play music "music/M27.OGG" fadein 1.0 fadeout 2.0
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「-啊，早上好，苍崎同学，已经听说要做什么了吧？」"with dissolve
    narrator "「-是的，一小时在自己家里听说的，而且是在事先没有任何通知的情况下。」" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_8 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "从这所高中毕业的山城，年纪也不比学生大多少" with dissolve
    narrator "因此，他比其他老师更受学生们的爱戴。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_9 with dissolve
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "话题丰富，语气温和。"with dissolve
    narrator "与其说是教师，更像是个可靠的学长。但很不巧，她对他没有什么爱戴可言。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "教师必须冷酷" with dissolve
    narrator "对于学生，老师必须是让他们爱恨交织的悬崖峭壁，绝不能是这种会在休息场所笑嘻嘻的大哥哥，这就是她的看法。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "山城老师是与她心目中的老师形象完全相反的人物，对他说话的语气自然就谈不上热情了。" with dissolve
    narrator ""
    narrator "...不过，应该说热情这种可爱的态度，她从来就不曾拥有过。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_7 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「-唉，你今天似乎还想心情不好呢。」" with dissolve
    narrator " 「-那是老师你多心了，并不是说只有今天如此。」" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "虽然回答得如此爽快，但是她很清楚自己现在的表情很糟糕。" with dissolve
    narrator " 被叫起床的不快，外加睡眠不足的疲劳，她估计自己现在的眼神凶的像是在瞪着仇人吧。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_10 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「-是吗，那样就好，不过别对他也这么凶哦。老实说，我们现在也不知道该怎么和他相处。」" with dissolve
    narrator " 「-老师，那件事还没告诉我详情呢。」" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_10_1 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator " 对于她有如剑般锐利的视线与声音，山城老师哦了一声，然后掐灭了香烟。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_1 with dissolve
    narrator ""
    narrator ""
    stop music
    play music "music/M27.ogg" fadein 1.0 fadeout 2.0
    show nvx with dissolve
    narrator "「-嗯，....你在电话里听到的是什么？」" with dissolve
    narrator " 「-只说是为了转学生介绍学校。" with dissolve
    narrator " 是个既没有原因也没有条理的说明。」" with dissolve
    nvl clear
    narrator ""
    narrator "对于这简洁的回答，山城吃惊地挑起眉。" with dissolve
    narrator " 他看得出她在生气，但没想到并不是因为休息日被叫到学校，" with dissolve
    narrator " 而是因为电话内容不得要领。" with dissolve
    show bg3_10 with dissolve
    show nvx with dissolve
    narrator "山城老师苦笑了一下，没想到她如此严格。" with dissolve
    hide nvx with dissolve
    hide bg3_10 with dissolve
    nvl clear
    show bg3_11 with dissolve
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "「-老师，如果你认为这很好笑的话，那我是不是可以回去了呢？」" with dissolve
    narrator " 「哎呀，对不起对不起，我道歉，这不是开玩笑，而是很认真的。像请你帮个忙。」" with dissolve
    narrator " 「-真是转学生的问题？」" with dissolve
    hide nvx
    show bg3_12 with dissolve
    narrator ""
    narrator ""
    nvl clear
    narrator ""
    narrator ""
    narrator "「-嗯，有点特别，或者说有点难办。" with dissolve
    narrator " 他........这位叫做草十郎的同学，稍稍有些脱节呢，比起让我们来带他参观学校" with dissolve
    narrator " 不如让同年代的你来做更合适，我是这么想的」" with dissolve
    scene bg3_12 with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "「.........」" with dissolve
    narrator " 她一脸怀疑的表情。" with dissolve
    narrator " 将教师的工作推给学生已经是玩忽职守了，而且还说转校生脱节，到底是怎么回事？" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "如果说是品行有问题导致不知道如何相处，那倒还比较容易想象。" with dissolve
    narrator " 但是所谓的脱节又是怎么回事？" with dissolve
    hide nvx
    nvl clear
    show bg3_14 with dissolve
    narrator ""
    narrator ""
    narrator "「脱节这种说法还是挺少见的.....」" with dissolve
    show bg3_15 with dissolve
    narrator " 虽然满腹疑云，但她立刻中止了思考。" with dissolve
    narrator " 再怎么烦劳也没有用" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "这种对话本身感觉就有点脱节，让人很不舒服，本身就缺少情报，再说自己像拒绝的话，现在早就倒在床上像个贝壳安逸地睡着了。" with dissolve
    nvl clear
    show bg3_16 with dissolve
    narrator ""
    narrator ""
    narrator " 「我有一个问题.....」" with dissolve
    nvl clear
    show bg3_17 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator " 「怎么了？啊，学年的话，和你一样是二年级生哦，性格也很沉稳，是那种很听话的人，反过来也可以认为他是毫无锐气吧，但这样就更容易相处了吧？" with dissolve
    narrator " 虽然和苍崎同学不同班，但是你们一定可以成为--------」" with dissolve
    hide nvx
    nvl clear
    show bg3_18 with dissolve
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "「这种事我会直接去问他本人，自己也会观察" with dissolve
    narrator " 我想问的不是这个，而是：为什么要找我」" with dissolve
    hide nvx
    show bg3_11 with dissolve
    show nvx with dissolve
    narrator "在发出话里带刺的问题的同时，也接下了给转学生介绍学校的工作。" with dissolve
    nvl clear
    hide nvx
    show bg3_19 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "虽然感到不满，但先将自己的感情放在一边，开始着手自己要负责的工作。" with dissolve
    narrator "虽然气质上极度的以自我为中心，但却依然尽力保持公正，这正是她的特长。" with dissolve
    narrator "虽然感觉有点本末倒置，但这种坚定的意志让山城等人觉得十分可靠。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "……不过呢。" with dissolve
    narrator "虽然有时这样的而坚定会超出预料，但一码归一码，将它当做天灾来对待就好了" with dissolve
    narrator "――这是这一年来山城老师所学到的应付她的对策。" with dissolve
    hide nvx with dissolve
    nvl clear
##################################################################################
    narrator ""
    narrator ""
    show bg3_20 with dissolve
    show nvx with dissolve
    narrator "「我再问一遍，山城老师。" with dissolve
    narrator "为什么要找我？」"  with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_19 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "对这不容分说的追问，山城老师虽然稍稍有些被气势所压倒，但还是回答道。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_21 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「嗯，这个嘛。" with dissolve
    narrator "这绝不是因为，苍崎同学是个既被老师们敬而远之同时又深受信赖，只要是为了学校好，能将老师和学生一视同仁一脚踢开的铁之学生会长哦。」" with dissolve
    hide nvx with dissolve
    show bg3_9 with dissolve
    show nvx with dissolve
    narrator "―「……我倒觉得除此之外不会有其他理由接受这种工作」" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "她半眯着眼盯着学生会顾问，表现着自己的怀疑。" with dissolve
    narrator "不像一个十七岁少女的迫力，" with dissolve
    narrator "正像一个十七岁少女的可爱。" with dissolve
    narrator "面对着两者如奇迹一般达成了平衡的目光，山城老师仿佛看入迷一般，用安稳的笑脸承受住了洗礼。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_1 with dissolve
    show nvx with dissolve
    narrator ""
    narrator "「哎呀，如果只是职责的问题我就自己来了。在人选上的选择，和老师或者学生会长的头衔毫无关系哦。" with dissolve
    narrator "怎么说呢，能不计得失地接下这种工作的，我认为只有你了。因为你能胜任，所以就强烈的推荐了你。」" with dissolve
    narrator "总之，他的意思就是“不管怎么说，你在骨子里就是个老好人”。" with dissolve
    hide nvx with dissolve
####################################################################################################################
    nvl clear
    scene black with  dissolve
    show bg3_22 with dissolve
    show nvx with dissolve
    narrator ""
    narrator "「―――山城老师。」" with dissolve
    narrator "「哇，好可怕。不要这么瞪着我嘛。我说过的吧，你对我是无所谓，对他可要露出笑脸啊。" with dissolve
    narrator "总之，你理解了的话就快去吧。已经让他等了很久了。" with dissolve
    narrator "另外，下雨天赶来学校辛苦你了。回去的话我肯定会开车送你。」”。" with dissolve
    hide nvx with dissolve
    nvl clear
######################################################################################################################
    scene black with  dissolve
    show bg3_23 with dissolve
    show nvx with dissolve
    narrator ""
    narrator "山城老师潇洒地站了起来。" with dissolve
    narrator "而她只说了一句“不必了”，就走出了职员室。" with dissolve
    hide nvx with dissolve
    nvl clear
    stop music
###########################################################################################################
    play music "sound/se01004b.ogg" fadein 1.0 fadeout 2.0
    show bg3_24 at move_from_right
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "已经等了一个小时。" with dissolve
    narrator "天气在不知不觉中变成了小雨。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_25 at move_from_right
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "他茫然地听着雨滴的声音。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_26 at move_from_bottom
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "这个房间里只是例行公事一般地放置着长方形的桌子。" with dissolve
    narrator "有一个人影。除了他之外再无他人。" with dissolve
    narrator "在被请到这个房间，要他坐在这里等待之后，已经过了很久。" with dissolve
    narrator "如果是普通的学生，此时应该开始发泄不满与不安了，但少年就像是田里的稻草人一样，遵守着叮嘱。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "寒气仿佛浸透了整个身体。" with dissolve
    narrator "室温只比外面高了几度。" with dissolve
    narrator "不知道是不是没听见老师说的那句“可以开暖炉”，还是因为没见过这种类型的暖炉，他并没有打开暖气。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "他一边轻轻的对指尖哈气，一边茫然地观察着周围。" with dissolve
    narrator "这个单调的房间似乎叫做会议室。" with dissolve
    narrator "在本校学生来看的话算是个非常大气的会议室，但就他来看的话，就只是个朴实的大房间罢了。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_27 with dissolve
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "因为没有生活的味道，不禁让他联想到单调的岩洞。" with dissolve
    narrator "因为无事可做，于是他认真地开始考虑起来，在这种寒冷的地方一般会进行什么对话。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_28 with dissolve
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "「…………………………唔……」" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_29 at move_from_bottom
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "无论怎么想都得不到答案，所以他的意识又回到了雨声上。" with dissolve
    narrator "下雨的天空，和在山里看到的有一点像。" with dissolve
    narrator "不，应该说勉强还保持着原样。" with dissolve
    narrator "虽然气味和声音都变得生硬，但基本是同一种东西。" with dissolve
    narrator "这样的异界竟然也有和山里共通的东西啊―――" with dissolve
    narrator "他对这件小事由衷地感到开心。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_30 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "他喜欢被雨浸透的小镇。" with dissolve
    narrator "的确大晴天更让人感到惬意，但他更喜欢雨天是处于和这种惬意不同的视角。" with dissolve
    narrator "烟雨朦胧的小镇多了一丝泥土的气味，让他不由得想起了家乡。" with dissolve
    narrator "感觉只有在这种时候，来到都市的不安才会有所减弱。" with dissolve
    hide nvx with dissolve
    nvl clear
    scene black with  dissolve
    show nvx with dissolve
    narrator ""
    narrator "「――――――」"
    narrator "　……他马上气馁地叹了口气。" with dissolve
    narrator "真是没出息。" with dissolve
    narrator "明明已经搬来两周了，依然一不小心就会恋恋不舍地想起故乡，让他对自己很失望。" with dissolve
    narrator "这样不就对不起这来之不易的新生活了吗？他再次打起精神，端端正正地继续等待下去。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_31 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "在茫然中，他专心地听着雨声。"
    narrator "对于他来说，这样的等待似乎是小菜一碟。"
    narrator "他有着能将那让人麻木的寒冷，以及长达一小时的置之不理，都伴着深呼吸一起吞下去的平常心。" with dissolve
    narrator "不是常说功夫不负有心人，或者精诚所至、金石为开么。" with dissolve
    narrator "先不管这是不是优点吧，反正他有着让人目瞠口呆的忍耐力。" with dissolve
    narrator "这是这个少年现在的特长。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_32 with Dissolve(3)
    pause
    show bg3_33 with Dissolve(3)
    pause
    play music "sound/se01022b.ogg" fadein 1.0 fadeout 2.0
    show bg3_34 with Dissolve(2)
    show bg3_35 with Dissolve(2)
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "另一方面，她则是极度愤怒。" with dissolve
    narrator "因为在职员室走向会议室的这段时间里，她听了接下来要见的那个人的个人资料。" with dissolve
    narrator "据说，那个人从出生到至今为止，都生活在连电都没有的深山里。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_36 with dissolve
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "没有电就意味着，现在这个文明社会里有大半对他来说都是陌生的。" with dissolve
    narrator "『这种隔绝根本就让人绝望了，别说战后了，他根本是战前那个时代的人。" with dissolve
    narrator "鲁滨逊也不是这么当的！』" with dissolve
    narrator "她会如此愤怒也是事出有因的。" with dissolve
    hide nvx with dissolve
    nvl clear
    stop music
    scene  bg3_37 with dissolve
    play music "sound/se01004b.ogg" fadein 1.0 fadeout 2.0
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "据说，那个深山的村子在漫长的时间里，都只是一个孤立的群落。" with dissolve
    narrator "甚至和山脚下的村子都只有每个月一次的信件联络，简直看不出这是在现代的日本。" with dissolve
    narrator "然而，即使是在高速公路和JR――也就是原国有铁道――如血管一般遍布全国的现在，依然不能说就不存在这样的村子，这也是事实。" with dissolve
    nvl clear
    stop music
    pause
    play  music "sound/se01001b.ogg" fadein 1.0 fadeout 2.0
    scene bg3_38 with Dissolve(3)
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "现在能确定的，就是她根本无法想象在这种状况下生活的人会有这什么样的想法。" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_39 with Dissolve(3)
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「没有电……就只是村里没有通电吧，公共电话什么的应该有吧？」" with dissolve
    scene bg3_40 with Dissolve(3)
    show nvx with dissolve
    narrator "「据说没有哦。似乎在搬来这里之后，第一个让他惊讶的就是电话。" with dissolve
    narrator "他一脸认真地对我说‘电话真是方便啊’，甚至让我也重新感觉到电话还真的是很方便的东西。」" with dissolve
    narrator "她侧眼瞪着哈哈笑着的老师。" with dissolve
    narrator "也不知道是在开心什么，山城老师为淳朴的乡下少年露出了笑容。" with dissolve
    hide nvx with dissolve
    stop music
    nvl clear
    scene bg3_1 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    play music "sound/se01004b.ogg" fadein 1.0 fadeout 2.0
    narrator "「也就是说连派出所都没有吗……我老家也在深山，所以倒也不能说没通电是不可能的事情。" with dissolve
    narrator " ―――我说，他不会连学校也---不知道吧？」" with dissolve
    narrator "「嗯。据说知道是什么东西，但似乎今天是第一次来。可能是因此而紧张起来了吧，感觉聊起来没什么话题。" with dissolve
    narrator "嗯，这应该算是野孩子吧？　就像被狼养大的狼孩之类的？ 不对，这是探险队的事了吧！」" with dissolve
    hide nvx with dissolve
    stop music
    nvl clear
    scene bg3_41 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    play music "sound/se01001b.ogg" fadein 1.0 fadeout 2.0
    narrator "「………………」" with dissolve
    narrator " 「好、好可怕啊苍崎同学。玩笑、玩笑啦。不要这么瞪着我嘛。" with dissolve
    narrator "放心吧，跟他聊过之后，感觉是个很乖的孩子！" with dissolve
    narrator "怎么说呢，就像是听不懂人话的小动物一样。」" with dissolve
    narrator "「山城老师。这个比喻可不能让人安心啊」" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_33 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "她一边冷淡地回话，一边开始想象起没有电的生活，原本就已经不高兴的表情变得更加乌云密布。" with dissolve
    narrator " 因为，那是她所不知道的世界。" with dissolve
    narrator "她也明白了老师们为什么都举手投降。" with dissolve
    narrator "其实她也想投降后回到温暖的床上去，但那一文不值的自尊心却不允许她这么做。" with dissolve
    narrator "既然大家寄望于她能做到，自己也做出了“能行”的判断而接受了下来，那么不论经过如何内容怎样，都不能轻易放弃。" with dissolve
    hide nvx with dissolve
    nvl clear
    stop music
    scene bg3_42 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    play music "sound/se01022a.ogg" fadein 1.0 fadeout 2.0
    narrator "她将雨声甩在身后，走在冰冷的走廊上。" with dissolve
    narrator " 会议室已经近在眼前。" with dissolve
    narrator "她皱着眉头，摇曳着长发，向着未曾谋面的异邦人走去。" with dissolve
    narrator "脚下迈着优雅的步伐，仿佛在向战场发动突击。" with dissolve
    hide nvx with dissolve
    nvl clear
    stop music
    scene bg3_40 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「……呃，苍崎同学？" with dissolve
    narrator " 虽然我很信赖你，但以防万一我再确认一下。怎么说呢，你一定要温柔点哦。可以的话，露出笑脸比较好。」" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_43 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「我不擅长假笑。不过会试着努力一下。」" with dissolve
    narrator "「啊。是么，那就好。" with dissolve
    narrator "　……哎呀，真是太好了。苍崎同学也有不擅长的事呢……」" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_44 with dissolve
    play sound "sound/se01022a.ogg"
    play sound "sound/se01025.ogg"
    pause
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "在山城老师耸拉下肩膀的时候，她正好到达会议室的门口。" with dissolve
    narrator "　山城老师用眼神诉说着“温柔点，温柔点”，把手放在门把上。" with dissolve
    narrator "　这种态度让她变得更加急躁。" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_45 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "『……我知道我不苟言笑啦。但是笑脸这种东西又不是有意挤得出来的……" with dissolve
    narrator "　再说，这种速成的交际的话鸢丸比较擅长吧。』" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_46 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "她对自己的冷淡叹了口气，但转念一想，睡眠不足的休息日被叫到学校，怎么还可能一副笑脸呢。……" with dissolve
    narrator "　而且，这个元凶还是个与其上高中不如从小学开始的人。" with dissolve
    narrator "　……虽然这个人没有什么责任，但她也没有被学校强加工作的责任和义务。" with dissolve
    narrator "　至少，嗯，怎么说呢。" with dissolve
    narrator "“要是能稍微看看场合，在非节假日来就好了”――她真想这么抱怨几句。" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_45 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "『……不。应该说就是敌人。不管怎样都是敌人。" with dissolve
    narrator "　虽然很抱歉，但在考虑如何酌情减刑之前就是敌人！" with dissolve
    narrator "该说我们彼此都时运不济么，真是的，为什么偏偏选在这么忙的时候―――』" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_47 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "因为睡眠不足而产生的头痛，让她的攻击性增加了一成。" with dissolve
    narrator "　无论这扇门对面的人是多么的无害，只要是打扰我睡眠的家伙都是敌人。" with dissolve
    pause
    play sound "sound/se01017.ogg"
    narrator "　正在她的急躁快要达到顶点的时候，山城老师打开了会议室的门。" with dissolve
    hide nvx with dissolve
    stop music
    play music "sound/se01001b.ogg" fadein 1.0 fadeout 2.0
    nvl clear
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "……风景慢慢横向展开。" with dissolve
    narrator "　她不再顾及自己的情绪了。" with dissolve
    narrator "　直视前方，向会议室突击行进" with dissolve
    narrator "与这个与众不同的敌人见面。" with dissolve
    pause
    stop music
    nvl clear
    pause
    scene black with  dissolve
    narrator ""
    narrator ""
    narrator "镜头再次切换。" with dissolve
    narrator "时间稍稍回溯。" with dissolve
    nvl clear
    scene bg3_25 with  dissolve
    play music "sound/se01004a.ogg" fadein 1.0 fadeout 2.0
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "『什么都别干』这样的命令，" with dissolve
    narrator "对某种人来说是无可替代的奢侈，" with dissolve
    narrator "对某种人来说是无法忍耐的折磨。" with dissolve
    hide nvx with dissolve
    stop music
    nvl clear
    scene bg3_31 with  dissolve
    play music "sound/se01001a.ogg" fadein 1.0 fadeout 2.0
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "对主动的她来说，这是一种虽然令她羡慕，却是会因为过于可疑而不肯接受的奢侈品。" with dissolve
    pause
    narrator "而对于被动的他来说，这本应是虽然感到亲切，却是会勾起乡愁的苦涩荆棘……但目前已经被搁置了许久的他脸上没有丝毫不满。" with dissolve
    nvl clear
    pause
    narrator ""
    narrator ""
    narrator "他只是自然地，姿势端正地遥望着灰色的天空。" with dissolve
    narrator "虽然已经等了快一个小时，嗯，对方也有自己的事吧，反正也不要花钱。" with dissolve
    narrator "感觉只要有雨声就能一直等待下去。" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_48 with  dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "『但是，快过九点了吧……" with dissolve
    narrator "嗯，到底如何了呢……』" with dissolve
    narrator "即使如此还是漠然的，一边稍微地注意着时间，一边呆呆地听着雨声。" with dissolve
    nvl clear
#####################################################
    scene bg3_4 at move_from_right
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "节假日的校舍没有杂音 对话" with dissolve
    scene bg3_29 at move_from_bottom
    show nvx with dissolve
    narrator "只有滴滴答答敲击着窗的雨。" with dissolve
    scene bg3_49 with dissolve
    show nvx with dissolve
    narrator "静静沉淀的空气的声响。" with dissolve
    scene bg3_28 with dissolve
    show nvx with dissolve
    narrator "以及" with dissolve
    play sound "sound/se01022a.ogg" fadein 1.0 fadeout 2.0
    narrator "向这边径直走来的响亮脚步声。" with dissolve
    pause
    nvl clear
    narrator ""
    narrator ""
    narrator "『太好了，还以为被遗忘了。』" with dissolve
    scene bg3_50 with dissolve
    show nvx with dissolve
    narrator "能听到一个比较轻的脚步声，和稍重的成年人的脚步声。" with dissolve
    scene bg3_31 with dissolve
    show nvx with dissolve
    play sound "sound/se01025.ogg"
    pause
    play sound "sound/se01017.ogg"
    narrator "在他松了一口气的同时，会议室的门被拉开了。" with dissolve
    hide nvx with dissolve
    stop music
    nvl clear
    scene bg3_51 with dissolve
    play music "sound/se01004a.ogg" fadein 1.0 fadeout 2.0
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「抱歉，让你久等了。" with dissolve
    narrator "首先映入眼帘的，是一脸歉意、戴着眼镜的男性。" with dissolve
    narrator "记得是叫山城和树老师，带自己来这里的就是他。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "「呃，咦？　里中老师不在吗？" with dissolve
    narrator "……真过分啊，明明叫他陪你聊天的。」" with dissolve
    narrator "山城老师脸上的歉意更浓了，伸手挠了挠头。在他身后。" with dissolve
    nvl clear
###############################################################################
    pause
    scene black with  dissolve
    pause
    play sound "sound/se01022a.ogg"
    show screen my_scr
    $ renpy.movie_cutscene("audio/chapter1/xuqu.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/chapter1/xuqu_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    show bg3_51_4
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "走出来一个满脸不快地紧闭着嘴，" with dissolve
    narrator "有着坚定的眼神以及黑色长发的少女。" with dissolve
    pause
    nvl clear
    stop music
#############################################################################
    pause
    play music "music/M04.ogg" fadein 1.0 fadeout 2.0
    show screen my_scr
    $ renpy.movie_cutscene("audio/chapter1/chapter1_1_5.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/chapter1/chapter1_1_5_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    show bg3_52
    narrator ""
    narrator ""
    show bg3_52_1 with dissolve
    narrator "「――――――」" with dissolve
    narrator "他愕然地屏住了呼吸。" with dissolve
    narrator "打在窗户上的雨声从听觉世界中消失了。" with dissolve
    narrator "……此时。" with dissolve
    narrator "他第一次体会到，尽管是错觉，但真的可能会察觉不到时间的经过。" with dissolve
    nvl clear
#################################################################################
    pause
    show screen my_scr
    $ renpy.movie_cutscene("audio/chapter1/chapter1_1_6.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/chapter1/chapter1_1_6_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    show bg3_53
    narrator ""
    narrator ""
    show bg3_53_1 with dissolve
    narrator "「………………」" with dissolve
    narrator "她似乎是有些惊讶地眨了下眼。" with dissolve
    narrator "原因不明。" with dissolve
    narrator "明明就跟之前听说的一样，少年给人一种纯朴乡村少年的感觉，但直觉上却在反驳着“无法接受”。" with dissolve
    nvl clear
#######################################################################
    pause
    show screen my_scr
    $ renpy.movie_cutscene("audio/chapter1/chapter1_1_7.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/chapter1/chapter1_1_7_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    show bg3_54
    show bg3_54_1 with dissolve
    narrator ""
    narrator ""
    narrator "「………………」" with dissolve
    narrator "他似乎是有些惊讶地睁大了眼。" with dissolve
    narrator "原因明确。" with dissolve
    narrator "……只是，因为不知用什么样的言辞来表达，最后也只能交了白卷。" with dissolve
    narrator "在这个瞬间。" with dissolve
    narrator "少年感觉自己真的是邂逅了某种命运。" with dissolve
    nvl clear
#################################################################################
    scene bg3_55 at move_from_bottom_fast
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "在这个瞬间。" with dissolve
    narrator "少年感觉自己真的是邂逅了某种命运。" with dissolve
    nvl clear
    scene bg3_56 with  dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「我介绍一下。他是转学生静希草十郎同学。" with dissolve
    pause
    hide nvx with dissolve
    pause
    scene bg3_57 with  dissolve
    show nvx with dissolve
    narrator "然后，这位就是负责带静希同学参观学校的人。" with dissolve
    narrator "我校的学生会长，不惜抛弃假日来带领新同学参观学校的苍崎青子同学。」" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_58 with  dissolve
    scene bg3_59 with  dissolve
    play sound "sound/se01003.ogg" loop fadein 1.0 fadeout 2.0
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "―――感觉人声和雨声都渐渐远去。" with dissolve
    narrator "两个人的邂逅就是这种感觉。" with dissolve
    narrator ""
    narrator "不管是好是坏，总之就是这种火花四溅，无比寻常的开局。" with dissolve
    hide nvx with dissolve
    nvl clear
    pause
    scene bg3_60 with  Dissolve(1.5)
    pause
    scene black with  Dissolve(3)
    stop music
    stop sound
    narrator ""
    narrator ""
    narrator "根据学生们的一般说法。" with dissolve
    narrator "苍崎青子，总是一脸不快。" with dissolve
    nvl clear
    scene bg3_61 with  Dissolve(3)
    play music "music/M29.ogg" loop fadein 1.0 fadeout 2.0
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "这其中九成都是偏见，就算是青子，也没空一天到晚都烦躁不已。" with dissolve
    narrator "她纯粹只是那种不喜欢找借口的性格，" with dissolve
    narrator "只是看起来常常微妙地、偶尔明显地对某种无形的东西发火罢了。" with dissolve
    narrator "因此那九成，只不过是在抱有偏见的谣言上添油加醋而成的校园七威胁之一罢了。"
    hide nvx with dissolve
    nvl clear
    scene bg3_62 with  Dissolve(3)
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "但是，剩下的一成却是真实。" with dissolve
    narrator "青子时而会对无害的东西觉得反感，这甚至让她怀疑自己是不是患有慢性头痛症，" with dissolve
    narrator "今天就属于那一成。" with dissolve
    narrator "但只有这种时候，她的愤怒才是纯粹的、" with dissolve
    narrator "与同龄人相似的任性。" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_27 with  Dissolve(3)
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "会议室很昏暗，如同染上了雨的颜色。" with dissolve
    narrator "学校规定为了节约电费，白天不得开灯。" with dissolve
    narrator "而那个人就站在会议室里。" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_63 with  Dissolve(3)
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "第一印象是让人联想到野花般的沉稳。" with dissolve
    narrator "明明挺直了背脊，但全身放松，给人一种文静的感觉。" with dissolve
    narrator "不能算弱不禁风，却还是显得文弱。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_64 at move_from_bottom_fast
    show nvx with dissolve
    narrator ""
    narrator "体格比起普通水准略显纤细，就算隔着制服也能看出。" with dissolve
    narrator "这就是个有着一头并未用心打理的黑发，没有什么特点的典型少年。" with dissolve
    narrator "不。如果要善意地解释这份平庸的话，该说他比起少年更像是个青年吧。" with dissolve
    narrator "　沉稳的感觉中透着一股成熟。" with dissolve
    narrator "……就是这种地方让青子感到“毫无理由的反感”么。" with dissolve
    narrator "少年实在过于自然，没有任何异常地融入了会议室的风景中。在学校里明明他才是异端分子，但却给青子一种自己才是客人的错觉。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_65 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「――――――」" with dissolve
    narrator ""
    narrator "这种莫名的烦躁，简直像是自己与生俱来的正当性遭到了批判似地。" with dissolve
    narrator "　青子感觉自己心中的警戒心开关啪地一声打开了。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_66 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "『―――难以置信。" with dissolve
    narrator ""
    narrator "我，现在毫无意--理---义----地在生气？』" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_59 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "搞不清的事情让人烦躁，如果是自己的事情那就更是如此。" with dissolve
    narrator "对身为完美主义者的她来说，这虽然不疼，却依然是心中的一根刺， "  with dissolve
    narrator ""
    narrator "「哎呀，哈哈哈。好了，苍崎同学来打个招呼吧。」" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_67 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "山城圆场的声音，反而让她更是烦躁。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_68 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「―――打招呼？」" with dissolve
    narrator ""
    narrator ""
    narrator "侧眼瞪了下山城后，青子直直地看着少年。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_69 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "以第三者的眼光来看的话，她是在怒瞪着他。" with dissolve
    narrator ""
    narrator "在这个瞬间。 " with dissolve
    narrator "她感情的枪尖刺向了初次见面的无辜少年，这简直是个悲剧。" with dissolve
    hide nvx with dissolve
    nvl clear
    stop music
    show bg3_70 with dissolve
    play sound "sound/se01001a.ogg" loop fadein 1.0 fadeout 2.0
    narrator ""
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "「哎呀，让你久等了静希同学」" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_71 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "被叫到名字的少年……草十郎回过神来。" with dissolve
    narrator ""
    narrator "他转开看呆了的双眼，" with dissolve
    narrator "像是为了止住头昏眼花一般吸了口气。" with dissolve
    narrator "大概是从此举中看出他在紧张，山城老师温和地一笑，对着旁边的少女说：" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_72 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「我介绍一下。他是转学生静希草十郎同学。" with dissolve
    narrator ""
    narrator "然后，这位就是负责带静希同学参观学校的人。我校的学生会长，不惜抛弃假日来带领新同学参观学校的苍崎青子同学。」" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_73 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "被山城老师介绍后，少女上前一步。" with dissolve
    narrator "视线里毫不留情。 " with dissolve
    narrator "那是近乎暴力，像是在评价他的凝视。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_75 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "两人之间的交锋，从第三者的视角来看显得无比强悍。" with dissolve
    narrator "一方面是极度想找茬的暴力分子，" with dissolve
    narrator ""
    narrator "不论当事人怎样，但对周围的人来说，这简直是折磨。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_76 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "　比如说，站在青子身后的山城老师。" with dissolve
    narrator ""
    narrator "出于好心才选择让一个好学生来负责介绍学校，但不知为何这位好学生心情不好。现在都能感觉出空气中一股剑拔弩张的味道。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_77 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "事已至此，山城只能接受自己的失败。" with dissolve
    narrator "　虽然此时才说这个有点太迟，" with dissolve
    narrator "但在这个任何事都能完美解决的女学生面前，你只要说错一句话，她就会一变成为震撼学校的暴风雨。" with dissolve
    narrator "就像扑克牌中最强的牌是恶魔-小丑一样，这种时候，正好在场的老师大都要背上黑锅。" with dissolve
    hide nvx with dissolve
    nvl clear
    stop sound
    play music "music/M39.OGG" fadein 1.0 fadeout 2.0
    show bg3_78 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「啊，嗯。不错嘛，你们两位似乎一见如故嘛！" with dissolve
    narrator "　……那么，我就先告辞了？」" with dissolve
    narrator ""
    narrator "山城老师一边发出苍白的笑声，一边慢慢向门口退去。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_79 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「我留在职员室，参观完了以后来找我。" with dissolve
    narrator "知道了吗，苍崎同学，千万注意，千万注意啊？" with dissolve
    hide nvx with dissolve
    show bg3_68 with dissolve
    show nvx with dissolve
    narrator "怎么说呢，此刻正是考验你这个学生会长是否心胸宽广的时候啊！」" with dissolve
    hide nvx with dissolve
    nvl clear
    pause
    show bg3_80 with dissolve
    play sound "sound/se01018.ogg"
    pause
    show bg3_81 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "山城老师将那正在对视的――正确来说是一方瞪着一方的――两人丢在那里迅速离开了" with dissolve
    narrator "留下的是已经变成了“木讷”词条代言人的少年，" with dissolve
    narrator "以及凝重地将手叉在胸前的少女。" with dissolve
    nvl clear
    show bg3_82 with dissolve
    hide bg3_82 with dissolve
    pause
    scene bg3_83 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "一阵短暂的沉默。" with dissolve
    narrator "两人就如同在下将棋时烦恼着如何下第一步，但青子察觉到，实际上在思索的只有她一个人罢了。" with dissolve
    narrator "总之，先把烦躁放在一边。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_84 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "说起来，本来就没理由对他产生反感" with dissolve
    narrator "这让青子大大叹了一口气，重新看向草十郎。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_85 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「算了，山城老师犯傻也不是第一天的事了。" with dissolve
    narrator "―――那么，你的名字是？」" with dissolve
    hide nvx with dissolve
    show bg3_86 with dissolve
    show nvx with dissolve
    narrator "如此严厉的语气，是在指责不主动开口的少年。" with dissolve
    narrator "但是，少年却没有察觉到语气中包含的挖苦。" with dissolve
    hide nvx with dissolve
    nvl clear
    show bg3_87 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "他的表情似乎和这种挖苦一生无缘，" with dissolve
    hide nvx with dissolve
    show bg3_88 with dissolve
    show nvx with dissolve
    narrator "「嗯，我叫静希草十郎。你是苍崎小姐吧。」" with dissolve
    narrator "不知为何，还显得有些开心地一字一句回答道。" with dissolve
    hide nvx with dissolve
    nvl clear
    pause
    show bg3_89 with dissolve
    pause
    show bg3_90 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「小姐就免了，我担当不起。我就叫你静希君怎么样？」" with dissolve
    narrator "「什么怎么样？」" with dissolve
    hide nvx with dissolve
    show bg3_91 with dissolve
    show nvx with dissolve
    narrator "「说称呼啊。我在问用‘君’好不好啊」" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_92 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「――――――」" with dissolve
    hide nvx with dissolve
    scene bg3_93 with dissolve
    show nvx with dissolve
    narrator "「怎么，我说了什么奇怪的话吗？」" with dissolve
    narrator "「嗯，很怪。」" with dissolve
    narrator "少年像是觉得很理所当然似地迅速回答，但又自言自语地说“嗯，好像也不是。”" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_94 with dissolve
    narrator ""
    narrator ""
    show nvx with dissolve
    narrator "「不，就这样吧，这是一般的叫法吧。" with dissolve
    hide nvx with dissolve
    pause
    scene bg3_95 with dissolve
    show nvx with dissolve
    narrator "就叫我静希君吧。我就叫你苍崎怎么样？」" with dissolve
    hide nvx with dissolve
    pause
    scene bg3_96 with dissolve
    show nvx with dissolve
    narrator "「嗯，多多指教。」" with dissolve
    hide nvx with dissolve
    pause
    scene bg3_97 with dissolve
    play sound "sound/se01024.ogg"
    show nvx with dissolve
    narrator "青子冷淡地应了一声，转过身去。" with dissolve
    narrator "虽然没有干劲，但被拜托的工作就要好好完成，这是她的原则。" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_98 with dissolve
    narrator ""
    narrator ""
    narrator ""
    narrator "「很抱歉，我可懒得好声好气地和你说话。" with dissolve
    narrator "别浪费时间了，赶快开始吧。」 " with dissolve
    scene bg3_99 with dissolve
    show nvx with dissolve
    narrator "「那真是帮大忙了。果然时间宝贵啊。」" with dissolve
    narrator "青子的直率挖苦又没有任何效果地被无视。 " with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_100 with dissolve
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「――――――」" with dissolve
    narrator "无论是什么行为，被无视的话就会更加在意，人类就是这样子。 " with dissolve
    narrator "从刚才开始所有攻击都落空，这让青子很是懊恼，但她还是努力地以公事公办的口气催促他来到走廊。" with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_101 with dissolve
    play sound "sound/se01017.ogg"
    narrator ""
    narrator ""
    narrator "没有窗口的通道里既没有来自外界的日光，也没有人的气息。" with dissolve
    narrator "如果说会议室是天然的洞窟，那这里就令人联想到人工的监狱。 " with dissolve
    narrator "这个走廊实在是与现在的心情太相衬了――青子不由得叹息道。" with dissolve
    nvl clear
    scene bg3_102 with dissolve
    narrator ""
    narrator ""
    narrator "「我先问一下，山城老师跟你说的东西你都明白了吗？」" with dissolve
    scene bg3_103 with dissolve
    narrator "「嗯，关于学校的构造我已经知道了。 " with dissolve
    narrator "　不过我还是难以想象，这座建筑物里面全是同龄人的景象。」" with dissolve
    nvl clear
    scene bg3_104 with dissolve
    narrator ""
    narrator ""
    narrator "「……哦，那还真不错。」" with dissolve
    narrator ""
    narrator "青子用手指抵住额头。 " with dissolve
    narrator "这个叫草十郎的少年连学校是什么都不知道。 " with dissolve
    narrator "看来只是含糊地听说这是许多人共同学习的场所。" with dissolve
    nvl clear
    scene bg3_105 with dissolve
    narrator ""
    narrator ""
    narrator "高中老师会将各个领域的知识与见识，机构与创造性传授给学生。" with dissolve
    narrator "但，恐怕他们根本没想过，会有必须要和人讲述“学校到底是什么”这种根本性理念的时候吧。 " with dissolve
    narrator "虽然基础是很重要的，但这基础过头了。 " with dissolve
    narrator "青子不由得对他这样是否能跟得上高中课程而感到疑惑，但山城老师说过船到桥头自然直。" with dissolve
    narrator "怎么说他也好歹是勉强通过了转学考试的。" with dissolve
    nvl clear
    scene bg3_106 with dissolve
    narrator ""
    narrator ""
    narrator "『算了，反正跟我没关系』" with dissolve
    narrator "青子内心里一边嘀咕一边行走在走廊上。 " with dissolve
    narrator "不管怎样，和这个时空错乱的男生恐怕也只有今天会有交谈了。不，是最好只有今天――她对自己说道。 " with dissolve
    nvl clear
    scene bg3_107 with dissolve
    narrator ""
    narrator ""
    narrator "「苍崎……」" with dissolve
    narrator "少年则是坦然地和青子搭话。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "「怎么了？」" with dissolve
    narrator "「我也问个问题，可以吗。」" with dissolve
    scene bg3_108 with dissolve
    narrator "「所以了，是什么事？」" with dissolve
    narrator "「不知道是不是我的错觉，你看上去就像是在瞪着什么东西。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "难道是今天早上身体不舒服吗？」" with dissolve
    narrator "看草十郎的眼神，似乎是认真地在担心她吃错了什么东西。" with dissolve
    stop music
    nvl clear
    scene bg3_109 with dissolve
    play sound "sound/se01004a.ogg" loop fadein 1.0 fadeout 2.0
    scene bg3_104 with dissolve
    narrator ""
    narrator ""
    narrator "「――――――」" with dissolve
    narrator "青子再次感觉到脑袋被锤子砸了一下。" with dissolve
    stop sound
    scene bg3_110 with dissolve
    play music "music/M39.OGG" fadein 1.0 fadeout 2.0
    narrator "的确青子从刚才开始就在瞪着草十郎。" with dissolve
    narrator "或者说已经是认真地开始瞪着了。" with dissolve
    narrator "应该说她对所有事物都是用瞪的。" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "就连平时都被同居人告诫道：" with dissolve
    scene bg3_111 with dissolve
    narrator "『青子的视线对普通人来说太严厉了。" with dissolve
    narrator "应该对更多的事情宽大一点。』" with dissolve
    narrator "这样的视线，明确地表示出“如果再增加负荷就要发飙了”。但这个少年却能迟钝到把这个当做错觉？" with dissolve
    nvl clear
    scene bg3_112 with dissolve
    narrator ""
    narrator ""
    narrator "『把我当白痴吗……应该不会这样吧，在这种情况下的话。』" with dissolve
    scene bg3_113 with dissolve
    narrator "「？」" with dissolve
    narrator "青子想要说服自己，但却又无法确定。" with dissolve
    nvl clear
    scene black with  dissolve
    narrator ""
    narrator ""
    narrator "青子直到现在才直觉似地感受到了。" with dissolve
    narrator "这个呆呆的转学生，对于自己来说等同于未知生物。" with dissolve
    nvl clear
    scene bg3_114 with  dissolve
    narrator ""
    narrator ""
    narrator "「算了。看样子不说出来你就不会明白，不是“就像”，坦白说就是这样。" with dissolve
    narrator "并不是你的错觉，我只是在用视线来婉转地表现感情罢了。什么事都要用靠嘴说的话太麻烦了。」" with dissolve
    narrator ""
    narrator "外星人听了青子的话，恍然大悟地锤了下手。" with dissolve
    nvl clear
    scene bg3_115 with  dissolve
    narrator ""
    narrator ""
    narrator "「原来如此。虽然不知道你为什么想这么做，但这的确能更加直接地表现想法。」" with dissolve
    narrator "草十郎老实地接受了。" with dissolve
    narrator "但是，他不明白青子这是在表现哪种感情。" with dissolve
    narrator "虽然能读文字，但却没法读懂意思。" with dissolve
    narrator "感觉就像是本应联系在一起考虑的事，被他分割成了许多区块。" with dissolve
    nvl clear
    scene bg3_116 with  dissolve
    narrator ""
    narrator ""
    narrator "『原来如此。的确很脱节呢，这人……』" with dissolve
    narrator ""
    narrator "青子才理解了山城老师的话。" with dissolve
    narrator "这个少年的奇怪，已经不是能用迟钝这种标准来衡量的了。" with dissolve
    narrator "……即使如此。对他来说，这里如同异国他乡，如果是文明人的话，就该包容一下他这种对时差的不适应" with dissolve
    nvl clear
    scene bg3_117 with  dissolve
    narrator ""
    narrator ""
    narrator "「那么，总之先去你的教室吧。」" with dissolve
    narrator "再次打起精神的青子这么说道。" with dissolve
    narrator "但却被草十郎举起一只手阻止了。" with dissolve
    nvl clear
    scene bg3_118 with  dissolve
    narrator ""
    narrator ""
    narrator "「哦，还有一件事。」" with dissolve
    scene bg3_119 with  dissolve
    narrator "草十郎很自然地说道，青子则是沉默地催促他继续说下去。" with dissolve
    narrator "她的手指按住额头上，隐隐地感觉到不安。" with dissolve
    nvl clear
    scene bg3_120 with  dissolve
    narrator ""
    narrator ""
    narrator "「这也是个小问题，为什么你在发怒呢？" with dissolve
    narrator "难道你家里是那种靠生气来做买卖的人？」" with dissolve
    stop music
    scene bg3_121 with  dissolve
    narrator "“―――――――――”" with dissolve
    nvl clear
    pause
    scene bg3_104 with  dissolve
    play sound "sound/se01004a.ogg" loop fadein 1.0 fadeout 2.0
    narrator ""
    narrator ""
    narrator "漫长的沉默。" with dissolve
    narrator "虽然现在来说已是马后炮，但是青子开始对今早拿起电话的事感觉到强烈的后悔。" with dissolve
    narrator "对方是没有恶意的。" with dissolve
    narrator "这是天然呆，只是天然呆罢了――青子在心中反复如此念叨着，压抑住了自己的真实感情。" with dissolve
    nvl clear
    stop sound
    scene bg3_122 with  dissolve
    narrator ""
    narrator ""
    narrator "「这并不是你的错，你不用在意。" with dissolve
    narrator "只是将这一瞬间和一觉睡到中午的情况拿来衡量的话，会发现所得相差实在太大，让我感觉头疼。」" with dissolve
    narrator "在拐弯抹角地回答后，青子这次终于迈出了脚步。" with dissolve
    narrator "将静希草十郎这个失礼的异邦人彻底地摆脱出自己的视野。" with dissolve
    nvl clear
    scene black with  dissolve
    narrator ""
    narrator ""
    narrator "虽然以什么为基准来判断普通还是个疑问，但他的性格确实非常普通。朴素的老好人。印象色勉强算是白色。性別男。外表呆笨。" with dissolve
    scene bg3_123 with  dissolve
    play music "music/M28a.ogg" fadein 1.0 fadeout 2.0
    narrator "而在草十郎看来，苍崎青子这个人动作利落精力充沛。" with dissolve
    narrator "就连一些下意识的动作也没有多余，干脆地行动，利落地停止。" with dissolve
    narrator "像是指东西的时候抬起的手指，" with dissolve
    scene bg3_124 with  dissolve
    pause
    scene bg3_125 with  dissolve
    narrator "这种一举一动都给人留下很深印象，让人无法将视线从她身上移开。" with dissolve
    nvl clear
    pause
    scene bg3_126 at move_from_right
    narrator ""
    narrator ""
    show nvx with dissolve
    play sound "sound/se01024.ogg" loop fadein 1.0 fadeout 2.0
    narrator "青子首先带他去了二年Ｃ班的教室。" with dissolve
    hide nvx with dissolve
    pause
    scene bg3_127 at move_from_right
    pause
    show nvx with dissolve
    narrator "尽管草十郎觉得这里比起刚才的会议室，人的气息要浓烈了一些，但还是没搞懂这里是干什么的地方。" with dissolve
    narrator "听了青子短暂的说明后，在分为好几类的特别教室，体育馆，食堂，更衣室，保健室这些地方都转了一圈。" with dissolve
    narrator "因为草十郎每去一个地方都请青子进行说明，所以离开二楼视听教室的时候已经过了相当长的时间。" with dissolve
    stop sound
    nvl clear
    scene black with dissolve
    narrator ""
    narrator ""
    narrator "「……糟糕了。」" with dissolve
    scene bg3_128 with dissolve
    narrator "草十郎一副严肃的表情停下脚步。" with dissolve
    narrator "「再过二十分钟就到一点了。」" with dissolve
    scene bg3_129 with dissolve
    narrator "「咦？　不是吧，我们的校舍才没这么大啊？」" with dissolve
    narrator "记得是从早上十点开始带他参观，一点就意味着花了三个小时。" with dissolve
    pause
    scene bg3_130 with dissolve
    narrator "不过就是参观个学校应该用不了这么久啊……" with dissolve
    nvl clear
    pause
    scene bg3_131 with dissolve
    narrator ""
    narrator ""
    narrator "「……也是啊。每个地方都要刨根问底地问个不停，当然要花上几个小时了。就算现在天黑了也没什么稀奇。」" with dissolve
    scene bg3_132 with dissolve
    narrator "青子瞪了草十郎一眼。" with dissolve
    narrator "因为知道他听不懂这样的挖苦，她才会这么发牢骚。" with dissolve
    nvl clear
    scene bg3_133 with dissolve
    narrator ""
    narrator ""
    narrator "『………咦？』" with dissolve
    narrator ""
    narrator "但是，" with dissolve
    narrator "也不知道草十郎的心情发生了什么变化，他一脸歉意地垂下了眼睛。" with dissolve
    nvl clear
    scene bg3_134 with dissolve
    narrator ""
    narrator ""
    narrator "『什么嘛，这家伙―――还是挺正常的啊。』" with dissolve
    narrator ""
    narrator "陷入烦恼的草十郎简直和之前判若两人。" with dissolve
    narrator "与之前无论青子说什么都毫无反应的面无表情不同，此时的他让青子的心中涌现出难以言喻的亲近感。" with dissolve
    scene bg3_135 with dissolve
    narrator "然后不知为何，青子还是毫无理由地烦躁起来。" with dissolve
    nvl clear
    scene bg3_136 with dissolve
    narrator ""
    narrator ""
    narrator "「然后呢，什么事情糟糕了？" with dissolve
    narrator "你可别说是要记的事情太多脑子快炸开了啊。」 " with dissolve
    scene bg3_137 with dissolve
    narrator "「不，虽然这个原因也有一点。但和学校的事情无关，到了一点就糟糕了。」" with dissolve
    scene bg3_138 with dissolve
    narrator "草十郎忧心忡忡地移开视线。" with dissolve
    narrator "是在意外面的情况吗？不巧的是，这个走廊里没有窗户。" with dissolve
    nvl clear
    scene bg3_51 with dissolve
    play sound "sound/se01004a.ogg" loop fadein 1.0 fadeout 2.0
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「……哦。在意时间，是因为你有什么重要的事要做吧。" with dissolve
    narrator "你可别说是要记的事情太多脑子快炸开了啊。」 " with dissolve
    hide nvx with dissolve
    stop sound
    nvl clear
    scene bg3_139 with dissolve
    narrator ""
    narrator ""
    narrator "哼，是这样啊。将别人的计划搞得一团乱，自己却想要为所欲为。" with dissolve
    narrator "什么嘛，你还真是人不可貌相。」 " with dissolve
    nvl clear
    scene bg3_140 with dissolve
    narrator ""
    narrator ""
    scene bg3_141 with dissolve
    narrator "「？　呃，就算夸我也得不到什么好处哦。」" with dissolve
    pause
    play sound "sound/se01023mix.ogg"
    scene bg3_142 with dissolve
    narrator "「谁在夸你啊！」" with dissolve
    narrator "青子忍不住怒吼。" with dissolve
    nvl clear
    scene bg3_143 with dissolve
    scene bg3_143 with dissolve
    narrator ""
    narrator ""
    narrator "「然后呢？」" with dissolve
    scene bg3_145 with dissolve
    narrator "「然后？」" with dissolve
    scene bg3_146 with dissolve
    narrator "「我问的是你到底有什么事啊。」" with dissolve
    narrator "草十郎似乎是明白了青子要说的话，用平静的表情点了点头，" with dissolve
    narrator "「这件事我想保密。」" with dissolve
    scene bg3_147 with dissolve
    narrator "然后一脸认真地说出了玩笑般的回答。" with dissolve
    nvl clear
    scene bg3_148 with dissolve
    narrator ""
    narrator ""
    narrator "『……我还以为已经快习惯了，但这家伙的这种步调还是经常会让人差点晕过去啊……』" with dissolve
    narrator "" with dissolve
    narrator "　至于原因自然是愤怒了。" with dissolve
    narrator "青子努力忍住这种心情，憋出了一张灿烂的笑脸。" with dissolve
    nvl clear
    play sound "sound/se01023mix.ogg"
    scene bg3_149 with dissolve
    narrator ""
    narrator "「静希君？」" with dissolve
    narrator "青子猛地往前踏出一步。" with dissolve
    scene bg3_150 with dissolve
    narrator "「说了是秘密了。」" with dissolve
    narrator "草十郎感觉到了一种类似杀气的东西，猛地往后退了一步。" with dissolve
    scene bg3_151 at move_from_right_fast
    narrator "一进，一退。" with dissolve
    narrator "有如磁铁一般，无论他怎么退，青子都会靠过来。" with dissolve
    narrator "她的脸上带着笑容，太阳穴轻轻颤动。" with dissolve
    nvl clear
    scene bg3_152 with dissolve
    narrator ""
    narrator ""
    narrator "「这是最后一个问题了。" with dissolve
    narrator "―――你觉得耍我好玩吗？」" with dissolve
    narrator "尽管草十郎想对天发誓说绝没有这种想法，但就算证明了自己的清白，也没法让青子这僵硬的笑容消失吧。" with dissolve
    narrator "「……知道了，我说。」" with dissolve
    scene bg3_153 with dissolve
    narrator "他举起双手投降。" with dissolve
    narrator "青子也停止前进，收起了这别扭的笑容。" with dissolve
    nvl clear
    scene bg3_154 with dissolve
    narrator ""
    narrator ""
    narrator "「其实一点开始我要打工。但是，这里禁止打工吧？」" with dissolve
    narrator "「这倒是……啊，因为被禁止所以想要保密？　真笨啊，去申请个许可就没问题了啊。」" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "「我知道。考试的时候已经拿到许可了。」" with dissolve
    scene bg3_155 with dissolve
    narrator "「哦。」" with dissolve
    narrator "青子那开心的脸上似乎在表示“真看不出来你这么机灵”。" with dissolve
    narrator "不过，" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "「只获得了一个许可。」" with dissolve
    scene bg3_156 with dissolve
    narrator "「？　一个……你打多份工啊？」" with dissolve
    scene bg3_157 with dissolve
    narrator "「……已经减少了两份工了。" with dissolve
    narrator "光是生活费就已经够呛，我连学费也得自己赚。但是即使如此，却只允许打一份工，你不觉得这很过分吗？」" with dissolve
    scene bg3_158 with dissolve
    narrator "「……不，我觉得过分的是你。」" with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "青子尽管有些无奈，但也稍稍对草十郎刮目相看了。" with dissolve
    scene bg3_159 with dissolve
    narrator "不但是学费，连生活费都自力更生，真是很能干。" with dissolve
    narrator "对这种正经的要事，苍崎青子反而强硬不起来。甚至连刚才的愤怒也渐渐消散。" with dissolve
    narrator "……但是她却没想到，让她的怒火平息的，仅仅是这个不谙世事的少年口中居然说出了『打工』这个词。" with dissolve
    nvl clear
    scene bg3_160 with dissolve
    narrator ""
    narrator ""
    narrator "「……这样的话就没办法了。" with dissolve
    narrator "行了，你去吧。情况我都了解了。」" with dissolve
    narrator "「苍崎你没问题吗？」" with dissolve
    scene bg3_161 with dissolve
    narrator "虽然不知道是问什么没问题，但青子起码听得出这是草十郎在担心她。" with dissolve
    narrator "……这也让青子有些许意外。" with dissolve
    narrator "她本以为，这个少年对人心会更加迟钝一些。" with dissolve
    nvl clear
    scene bg3_162 with dissolve
    narrator ""
    narrator ""
    narrator "「……这样的话就没办法了。" with dissolve
    narrator ""
    nvl clear
    scene bg3_163 with dissolve
    narrator ""
    narrator ""
    narrator "「没什么。我直接回家就是了。」" with dissolve
    narrator ""
    narrator "顺便一提，先去一趟职员室再走的这个选项从来不曾出现在她心中。" with dissolve
    narrator "据山城说，转入手续已经完成了，之后就剩下社交性质老套的问候了吧。" with dissolve
    nvl clear
    scene bg3_164 with dissolve
    narrator ""
    narrator ""
    narrator "“老师，参观结束了。”" with dissolve
    narrator "“真是辛苦了。静希同学也辛苦了，那么，看了一圈校舍后感觉如何？”" with dissolve
    narrator "“非常感谢。怎么说呢，很像一所学校啊！”" with dissolve
    narrator "“哈哈哈，是吗是吗。嗯，明天开始加油吧！”" with dissolve
    narrator ""
    scene bg3_163 with dissolve
    narrator "这种毫无意义的总结，与她没有任何关系。" with dissolve
    nvl clear
    scene bg3_165 with dissolve
    narrator ""
    narrator ""
    narrator "「不用在意山城老师。 " with dissolve
    narrator " 既然如此喜欢职员室，不惜把麻烦事推给学生就直接走掉，要他等几个小时也没问题吧。" with dissolve
    narrator " 　不对，是必须等吧？」" with dissolve
    nvl clear
    scene bg3_166 with dissolve
    narrator ""
    narrator ""
    narrator "「是吗。苍崎没问题的话，那就没问题了吧。」 " with dissolve
    scene bg3_167 with dissolve
    narrator "「？」 " with dissolve
    narrator "所以说，到底哪里没问题啊？ " with dissolve
    narrator "青子还是完全不知道草十郎想说什么。" with dissolve
    nvl clear
    scene bg3_168 with dissolve
    narrator ""
    narrator ""
    narrator "「那么我走了。今天真是谢谢你。」 " with dissolve
    narrator "「只限今天哦，只限今天。」 " with dissolve
    narrator "青子举起一只手甩了甩，示意他赶快滚蛋。 " with dissolve
    scene bg3_169 with dissolve
    narrator "不知草十郎是不是喜欢这个动作，开心地笑了。" with dissolve
    nvl clear
    scene bg3_170 with dissolve
    narrator ""
    narrator ""
    narrator "似乎是因为平时一直都是表情呆滞，现在他的这种表情显得无比地温和。 " with dissolve
    narrator "温和到让人会不自觉的用笑容回应。 " with dissolve
    narrator "但是， " with dissolve
    narrator "苍崎青子依然对这类表情没有任何反应。 " with dissolve
    stop music
    nvl clear
    scene bg3_171 with dissolve
    narrator ""
    narrator ""
    narrator "「那么，再见了」 " with dissolve
    pause
    play sound "sound/se01017.ogg"
    scene bg3_172 with dissolve
    pause
    narrator "「啊？」 "
    narrator "草十郎留下像是老朋友告别一般的话语，向走廊尽头……" with dissolve
    narrator "不对，是隔壁的教室走了进去。 "
    nvl clear
    play sound "sound/se01001a.ogg" loop
    show screen my_scr
    $ renpy.movie_cutscene("audio/chapter1/chapter1_1_8.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/chapter1/chapter1_1_8_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    show bg3_173
    show bg3_174 with dissolve
    narrator ""
    narrator ""
    narrator "「等―――」 " with dissolve
    narrator "背影径直走向窗口。 " with dissolve
    scene bg3_175 with dissolve
    pause
    play sound "sound/se01029.ogg"
    pause
    play sound "sound/se03002.ogg" loop fadein 1.0 fadeout 2.0
    pause
    stop sound
    narrator "他慢慢打开教室的窗。 " with dissolve
    play music "sound/se01004a.ogg" fadein 1.0 fadeout 2.0
    narrator "十一月的寒风与朦胧的雨声变得鲜明起来。 " with dissolve
    narrator "苍崎青子瞬间察觉到那意味着什么。恍然大悟。 " with dissolve
    nvl clear
    scene bg3_4 at move_from_right_superfast
    pause
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator "「不行，等等等等等等——————！」" with dissolve
    narrator ""
    narrator "青子拼命地阻止一只脚已经跨在窗框上的草十郎。 " with dissolve
    hide nvx with dissolve
    nvl clear
    scene bg3_176 with dissolve
    narrator ""
    narrator ""
    narrator "「你，你要干什么！」 " with dissolve
    narrator "「什么干什么，当然是去打工啦。」 " with dissolve
    scene bg3_177 with dissolve
    narrator "「这个窗户不是供人进出用的！ " with dissolve
    narrator "而且你以为这是几楼！？」 " with dissolve
    scene bg3_178 with dissolve
    narrator "经她这么一说，草十郎才想起了什么。 " with dissolve
    nvl clear
    scene bg3_104 with dissolve
    narrator ""
    narrator ""
    narrator "「……差点没命。从二楼下去太危险了。」 " with dissolve
    narrator "「危险的是你的脑袋……」 " with dissolve
    narrator "青子无力地嘟哝着粗暴的话语，但幸好草十郎没有听到。" with dissolve
    nvl clear
    scene bg3_179 with dissolve
    narrator ""
    narrator ""
    narrator "「我说啊，这里的人都不从窗户进出的。 " with dissolve
    narrator " 早知道就先跟你说了。」" with dissolve
    scene bg3_180 with dissolve
    narrator "「我知道，不过因为没时间了所以有点急。 " with dissolve
    narrator "谢谢，以后我会注意的。」 "
    pause
    stop music
    nvl clear
    scene bg3_181 with dissolve
    play music "sound/se01001a.ogg" fadein 1.0 fadeout 2.0
    narrator ""
    narrator ""
    narrator "草十郎将那只脚从窗框上放下，把窗关了起来。 " with dissolve
    narrator "那件明显是刚发下来的制服已经在刚才那次乌龙事件里被雨淋湿了。 " with dissolve
    nvl clear
    scene bg3_182 with dissolve
    narrator ""
    narrator ""
    narrator "「……算了，我不介意。 " with dissolve
    narrator "你爱从哪儿出去就从哪儿出去吧。只不过，可以的话我希望你至少不要在我眼前这么做。 " with dissolve
    scene bg3_183 with dissolve
    narrator "话说……你真的从明天开始来学校吗？」 " with dissolve
    scene bg3_184 with dissolve
    narrator "「会来的。虽然有些不安，但毕竟你今天给我介绍过了。」 " with dissolve
    nvl clear
    scene bg3_185 with dissolve
    play sound "sound/se01026.ogg" fadein 1.0 fadeout 2.0
    narrator ""
    narrator ""
    narrator "少年在道别之后跑向走廊。 " with dissolve
    narrator "他这次应该会正常地走下楼梯从门口出去吧。 " with dissolve
    nvl clear
    scene bg3_186 with dissolve
    narrator ""
    narrator ""
    narrator "「……唉。这人真的没问题吗。」 " with dissolve
    scene bg3_187 with dissolve
    narrator "在无奈的同时，青子回想起了他临走时的背影。 " with dissolve
    narrator "明明不想再跟那种乡下人扯上关系，但莫名地觉得有些在意。 " with dissolve
    narrator "是因为担心他，还是因为他让人火大？青子无法给出一个能让自己满意的答案。 " with dissolve
    nvl clear
    scene bg3_188 with dissolve
    narrator ""
    narrator ""
    narrator "而且为什么明明没有什么像样的理由，却会对那种和自己无关的转学生发火呢。 " with dissolve
    narrator "怪异的一天，怪异的转学生，怪异的感情。 " with dissolve
    narrator "　她不由得有些疑惑:其实这样想来，似乎这没有什么好生气的，反而应该觉得开心才对？ " with dissolve
    nvl clear
    scene bg3_189 with dissolve
    narrator ""
    narrator ""
    narrator "「―――唉，算了。 " with dissolve
    narrator " 反正也就这么一次。」" with dissolve
    nvl clear
    scene bg3_190 with dissolve
    narrator ""
    narrator ""
    narrator "雨声安静地响起。 " with dissolve
    narrator "灰色的天空让人对时间感到麻痹。 " with dissolve
    narrator "甚至分不清此时是早上还是傍晚。 " with dissolve
    narrator "校舍里估计只剩自己和山城了吧。 "with dissolve
    narrator "关了灯的教室非常昏暗，尤其是只有自己一个人的时候就变得更加阴森。 " with dissolve
    nvl clear
    narrator ""
    narrator ""
    narrator "青子拉下左手的袖子。 " with dissolve
    scene bg3_191 with dissolve
    narrator "朴素的小手表显示此时已经快到下午一点。 " with dissolve
    narrator ""
    narrator "「……还有点时间。」 " with dissolve
    nvl clear
    scene bg3_192 with Dissolve(3)
    pause
    show nvx with dissolve
    narrator ""
    narrator ""
    narrator ""
    narrator "说完，青子透过窗户俯视地面。 " with dissolve
    narrator ""
    narrator ""
    narrator "小雨之中，穿着制服的男生没有撑伞，冒雨奔跑着。这本应司空见惯的光景，却给她留下了很深的印象。 " with dissolve
    stop music
    hide nvx with dissolve
    hide screen xyz with  dissolve
    pause
    return
label story_1_4:
    stop music
    scene black with  dissolve
    nvl clear
    stop music
    show screen xyz with  dissolve



















































































    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    return

label story_1_5:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    return

label story_1_5_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    return

label story_1_5_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    "您已创建一12312个新的 Ren'Py 游戏。"
    return

label story_1_5_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    return

label story_1_5_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_2_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_2_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_2_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_3_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_4_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_4_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_4_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_4_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_5_1_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_1_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_1_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_1_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_1_5:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return



label story_5_2_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_2_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_2_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_2_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_2_5:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_2_6:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_2_7:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_2_8:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_5_2_9:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_6_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_6_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_6_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_6_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_6_5:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_6_6:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_7_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_7_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_7_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_7_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_8_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_8_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_8_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_8_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_8_5:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_8_5_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_9_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_9_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_9_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_9_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return



label story_9_5:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return



label story_fanwai1_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_10_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_10_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_10_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_10_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_11_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_11_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_11_3:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_11_4:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_12_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_12_2:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return


label story_13_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return



label story_fanwai2_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_fanwai3_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return

label story_16_1:
    stop music
    scene black with  dissolve
    "您已创2131建一个新的 Ren'Py 游戏。"
    "您已21312创建一个321新的 Ren'Py 游戏。"
    "您已创建一个新212的 Ren'Py 游戏。"
    return
































label splashscreen:
    show screen my_scr
    $ renpy.movie_cutscene("audio/logo.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/logo_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    return
