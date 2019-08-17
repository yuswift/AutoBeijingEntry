# AutoBeijingEntry
自动办理进京证服务
### Before

Python3  

Charles

A mobilephone

### Background

对于在北京的外地车主来说，每周一次的进京证办理过程可谓是十分恶心，点开App的强制广告，一开始不能跳过的30s阅读，以及恶心的各种证件的上传，上传过程中的闪退等，实在是受不了，正好最近在做一些爬虫方面的事情，遂决定用Charles抓包试试，没想到这种zf级的应用实在太过安全了，签名没有验证，传输数据没有加密，那自动化当然不在话下，实测办理没问题~稳定性有待验证。 

### Feature

自动办理进京证 再也无需点点点啦  无需上传照片 支持进京时间定制 进京时长等定制

## Usage

#### 自动化原理

通过Charles这类抓包软件获取到办理进京证的api，然后模拟这次http请求，修改其中的参数即可。

先装一个Charles抓包软件 附上 Mac破解版链接 https://juejin.im/post/5c0a430f51882516207d205d

#### 使用过程

装好以后再配置一下代理 由于北京交警用的是https协议 因此需要在手机装一个证书 链接里都有

装好以后 打开APP 在Charles上清掉所有的请求 手动办理一次进京证 最终复制一下两个url的curl请求 分别是

https://enterbj.zhongchebaolian.com/enterbj/platform/enterbj/entercarlist 获取进京证有效期接口

https://enterbj.zhongchebaolian.com/enterbj-img/platform/enterbj/submitpaper_03 上传进京证接口

然后把headers cookie 参数等填到配置文件中即可 以后就可以自动化啦

**下一次自动化的关键参数 进入北京时长 进入北京时间 时间戳最好也改一下~**

**所有参数说明都在配置文件中有备注**

git clone git@github.com:yuswift/AutoBeijingEntry.git

cd AutoBeijingEntry

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

python main.py

### Todo

目前这版未对签名进行破解(实测这款zf app在服务端未对签名进行校验 因此可以签名可以固定) 后期可能需要App 逆向破解

定时任务可以考虑加上 目前的计划是py+crontab 或者第二版用golang+https://github.com/rfyiamcool/cronlib



### Warning

2019.8.16

一年没更新的北京交警App更新啦 暂时不知道是否会封禁这个api 上次验证是在20-19.8.12  等我下周一再试试

### Config

参见config.yaml

