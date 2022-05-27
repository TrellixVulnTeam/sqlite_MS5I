
import win32com.client
import PySimpleGUI as sg

#ユーザーセッティング
settings = sg.UserSettings(filename="email_list", path=r"C:\Users\60837\Desktop\outlook")
settings.load()
settings["(有)エヌ・ピー(岡崎工場)"]="np.okazaki@sky.plala.or.jp"
settings["(有)エヌ・ピー(豊橋工場)"]="np.2005@rainbow.plala.or.jp"
settings["ケミカル工業㈱"]="kemikaru@aqua.ocn.ne.jp"
settings["サンホウ化成㈱"]="sanhou@gamma.ocn.ne.jp"
settings["ツチヒラ合成㈱"]="tsuchihira-gosei@gol.com"
settings["ツツミ化成工業㈲"]="katou2855@clock.ocn.ne.jp"
settings["マルアイ㈱"]="maruai@amitaj.or.jp"
settings["㈱アイデン"]="ad4096@aiden-jp.com; ta_hoshino@aiden-jp.com; ken_suzuki@aiden-jp.com; ko_yoshida@aiden-jp.com"
settings["㈱サンコー技研"]="sanko_g@sanko-gi.jp; shinwaseiki@bloom.ocn.ne.jp"
settings["㈱シンテック"]="fukatu@sintec-dream.com"
settings["㈱フレックスキャンパス"]="tak-oda@kojima-tns.co.jp; yuusuke-kuroyanagi@kojima-tns.co.jp; eiji-sano@kojima-tns.co.jp"
settings["㈱丸重"]="maruju@gol.com"
settings["㈱三宏技研"]="sankougiken@joy.ocn.ne.jp"
settings["岩津化成㈱"]="ka-iwazu@abeam.ocn.ne.jp"
settings["研精化工㈱"]="k-hara@ons.ne.jp; y-mizuno@ons.ne.jp"
settings["光和工業㈱"]="s-torii@kowa-kg.com"
settings["三洲化学工業㈱"]="t-ishikawa@sansyu-kk.jp"
settings["小島ｷｬﾝﾊﾟｽ"]="n-kakiuchi@kojima-tns.co.jp; yuhei-suzuki-aa@kojima-tns.co.jp"
settings["㈲アサヒ工業"]="asahi1@aichinet.ne.jp"
settings["㈲エヌ・ピー"]="main@np-2018.jp"
settings["㈲ダイモ化成"]="daimo@gamma.ocn.ne.jp"
settings["㈲宮本合成"]="smg@y2.dion.ne.jp"
settings["㈲鍵山製作所"]="kagiyamass@violin.ocn.ne.jp"
settings["㈲三福製作所"]="sanpuku@hm7.aitai.ne.jp"
settings["㈲小栗化成"]="y-ogrksi@hm8.aitai.ne.jp"
settings["㈲上郷樹脂"]="kami-tuzuki@oboe.ocn.ne.jp; n-suzuki@silk.ocn.ne.jp"
settings["㈲星川技研"]="hoshikawa-g@hoshi-g.co.jp; hinkan@hoshi-g.co.jp; suzuki-c@hoshi-g.co.jp; gyoumu@hoshi-g.co.jp"
settings["㈲青木製作所"]="aokiss@hm9.aitai.ne.jp"
settings["㈲大島金型産業"]="u_oks@citrus.ocn.ne.jp"
settings["㈲藤原樹脂"]="jyusi-f@f7.dion.ne.jp"
settings["㈲豊和化成"]="houwa-k@mis.ne.jp"
settings["㈱広和化成"]="m-harada@kowa-jp.com"
settings["遠州樹脂工業㈱"]="shin@eric.ne.jp"
settings["㈱サンワクリエイト"]="tomita_takayuki@s2-sanwa.co.jp"
settings["ヒロハマ合成㈱"]="hirohamagosei@ybb.ne.jp"
settings["㈱沖田化成"]="s-nakayama@okita-kasei.co.jp"
settings["㈲アイエードゥー"]="odai-seiki@nifty.com"
settings["㈱浅野"]="okazaki-takao@asano-japan.com; morinishi-takuro@asano-japan.com"
settings["㈲荒木金型"]="arakin@abeam.ocn.ne.jp"
settings["㈱エスケイモールド"]="info@skmold.co.jp"
settings["㈲加藤製作所"]="katou-s@katoseisakusho.com"
settings["㈱ケーツー"]="kasugai2@k2-net.co.jp"
settings["㈱坂本金型工作所"]="㈱坂本金型工作所"
settings["㈱サンコー技研"]="sanko_g@sanko-gi.jp"
settings["㈲三和精工"]="ssanwa@rose.ocn.ne.jp"
settings["㈲杉田精機"]="t-sugita@sugita-seiki.co.jp"
settings["㈱セントラルファインツール"]="yamaguchi@cft.jp"
settings["㈲高木金型製作"]="n.negita@takaki-kanagata.jp; h.takaki@takaki-kanagata.jp"
settings["トーカイモールド㈱"]="tokai@gol.com"
settings["トクサン金型㈱"]="sano@hm3.aitai.ne.jp"
settings["㈲友恵製作所"]="itokororyouji36900@h4.dion.ne.jp"
settings["㈱永野金型"]="nagano-k@m2.catvmics.ne.jp"
settings["㈱バリアス・ワークス"]="mase@various-works.com"
settings["㈲ハヤマ金型"]="yohdai@tees.jp"
settings["㈱プラム精工"]="plam@ruby.ocn.ne.jp"
settings["㈲山本金型製作所"]="shinji@yk-mold.co.jp"
settings["㈱有加工業"]="info@yuuka-kougyou.com"
settings["㈱ファインカット富山"]="fine-cut@nice-tv.jp"
settings["テクノハマ㈱"]="kazuma-kumagai@kojima-tns.co.jp"
settings["内製"]="k-naruse@kojima-tns.co.jp; h-tomita@kojima-tns.co.jp; hiroa-suzuki@kojima-tns.co.jp; y-takasu@kojima-tns.co.jp; yuuk-itou@kojima-tns.co.jp; kanahori@kojima-tns.co.jp ; yukiya-iwai@kojima-tns.co.jp; taisei-suzuki@kojima-tns.co.jp"
settings["金型保全課"]=" kouji-okamura@kojima-tns.co.jp;  ryouta-iwamoto@kojima-tns.co.jp; min-suzuki@kojima-tns.co.jp; t-takemura@kojima-tns.co.jp ;  tak-nagai@kojima-tns.co.jp"
settings["矢野"]="t-yano@kojima-tns.co.jp"


print(settings)

#受信メール取得
def mail_get():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)

    folders = inbox.Folders



    for folder in folders:
        print('Name: ' + folder.name)
        Folder = folders(folder.name)
        print('Message: ' + str(len(Folder.Items)))
        
        
    sonota = folders("その他").Items
    for i in sonota:
        #print(i.Subject)#件名取得(.Subject)
        #print(i.Sender)#宛先取得(.Sender)
        #print(i.body)#本文取得(.body)
        pass
    
#メール送信
def mail_send(To,CC,Bcc,Title,Body,Add):
    outlook = win32com.client.Dispatch("Outlook.Application")
    objMail = outlook.CreateItem(0) #MailItemオブジェクトのID
    
    #メール設定
    objMail.To = f"{To}" #宛先
    objMail.cc = f"{CC}" #CC
    objMail.Bcc = f"{Bcc}" #BCC
    objMail.Subject = f"{Title}" #Mailタイトル
    objMail.BodyFormat = 1 #(テキスト形式, リッチテキスト形式, HTML形式)
    objMail.Body = f"{Body}" #本文
    #objMail.Attachments.Add(r"{}".format(Add)) #添付ファイル
    objMail.Display(True) #MailItemオブジェクトを画面表示で確認する
    #objMail.Send() #メール即時送信

sg.set_options()
sg.theme("LightGray2")

lay = [
    [sg.Text("宛先"),sg.InputText(key="To")],
    [sg.Text("CC"),sg.InputText(key="CC")],
    [sg.Text("BCC"),sg.InputText(key="BCC")],
    [sg.Text("件名"),sg.InputText(key="Title")],
    [sg.Text("添付ファイル"),sg.Radio("有り",group_id="A",key="radio_1"),sg.Radio("無し",group_id="A",key="radio_2")],
    [sg.Text("本文"),sg.Multiline(key="Body",size=(30,10))],
    [sg.Button("GO",key="GO")]
]

window = sg.Window("",lay)

while True:
    event,value = window.read()
    if event == None:
        break
    if event == "GO":
        mail_send(To=value["To"], CC=value["CC"], Bcc=value["BCC"], Title=value["Title"], Body=value["Body"],Add="aa")