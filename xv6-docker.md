# Dockerによるxv6開発用ツールの実行方法

コンテナ仮想化ツール[Docker](https://www.docker.com)を使ったxv6開発用ツールの実行方法について説明します．
この方法では，各自のPCにクロスコンパイラなどの開発用ツールを個別にインストールする必要はありません．
xv6にしか使わない開発用ツールを自分のPCに直接インストールしたくない場合はこちらの方法を選んでください．

この方法を用いるためには各自のPCにDockerをインストールする必要がありますが，Docker自体は汎用性の高いツールなので，今後も利用する機会は多いと考えられます．
Dockerのインストール方法および使用方法については各自調べてください（MacやWindowsの場合はDocker Desktopのインストーラをダウンロードして実行するだけです）．
Docker Desktopは教育用途では無償で使えます．
以下，Docker Desktopがインストールされているとして説明します．

## Dockerイメージの取得とコンテナの起動

本講義のために，xv6開発用ツールを含んだDockerイメージ([wtakuo/xv6-env](https://hub.docker.com/r/wtakuo/xv6-env))を用意しました．
まず以下のコマンドでこのDockerイメージをDocker Hubより取得してください．
```console
% docker pull wtakuo/xv6-env
```
このイメージはマルチアーキテクチャ（現在はARM64とAMD64）に対応していますので，M1 Macを含む多くの環境でそのまま使うことができます．

これで開発用ツールの実行に必要なものが揃いました．
あとは以下のようにしてコンテナ（ホストOSから隔離された実行環境）を起動してください．
```console
% docker run -it --rm -v path-to-xv6:/home/xv6/xv6-riscv wtakuo/xv6-env
```
ここで`path-to-xv6`はRISC-V版xv6のソースコードのディレクトリへのパス名に置き換えてください．
このようにしてコンテナを起動することで，
ホストOS（PCで実行しているOS）上の`path-to-xv6`で表されるディレクトリが，コンテナ内部で`/home/xv6/xv6-riscv`というディレクトリとしてアクセスできるようになります．

コンテナ起動時にパスを指定する代わりに以下のようにすると簡単です．
```console
% cd path-to-xv6
% docker run -it --rm -v $(pwd):/home/xv6/xv6-riscv wtakuo/xv6-env
```

**Macの場合の注意**: xv6のソースコードの場所（`path-to-xv6`）がiCloud Driveに含まれないようにしてください（下記の**Macの場合の注意事項**を参照のこと）．

コンテナが無事起動すると以下のようにシェル(bash)のプロンプトが現れます（プロンプトに含まれる`0c765f60374a`は起動したコンテナのIDで，実際にはコンテナ毎に違う値となります）．
```console
xv6@0c765f60374a:~/xv6-riscv$ 
```
### 具体例

以下のように，ホストOS（PCで実行しているOS）のホームディレクトリ直下に`class/os`というサブディレクトリを作成し，そこにxv6のソースコードを取得したとします．
```console
% cd
% mkdir -p class/os
% cd class/os
% git clone https://github.com/titech-os/xv6-riscv.git
```
この場合，コンテナの起動は以下のようにして行います．
```console
% cd ~/class/os/xv6-riscv
% docker run -it --rm -v $(pwd):/home/xv6/xv6-riscv wtakuo/xv6-env
```
上で述べたように，ホストOS上のディレクトリ`~/class/os/xv6-riscv`は，コンテナ内部で`/home/xv6/xv6-riscv`というディレクトリとしてアクセスできるようになります．

## コンテナ内での作業

コンテナ内ではxv6開発用ツールがインストールされたLinux(Ubuntu)が動いています．
コンテナ起動時の作業ディレクトリは `/home/xv6/xv6-riscv` に設定されていますので，すぐに作業を開始することができます．
以下のようにしてxv6のビルドと実行ができることを確認してください．
```console
xv6@0c765f60374a:~/xv6-riscv$ make
xv6@0c765f60374a:~/xv6-riscv$ make qemu
...
xv6 kernel is booting

hart 2 starting
hart 1 starting
init: starting sh
$ 
```
最後の`$`はxv6のプロンプトです．
コンテナ内で（RISC-Vをエミュレートする）仮想マシンアプリケーションQEMUが動作し，その上でxv6が動作しています．
xv6上でいくつかプログラムを動かして動作を確認してみてください．
`usertests`というプログラムを実行すると，多少時間はかかりますがxv6カーネル全体のテストを行うことができます．
このプログラムの実行後は，いったんxv6から抜けて`make clean`を実行し，続けて`make`を実行しておいてください．

xv6から抜けるには，`ctrl-A`に続けて`x`をタイプします．

## その他

ここで提供しているDockerイメージにはEmacsなどのエディタは含まれていません（イメージサイズをなるべく小さくしたかったので）．
コンテナ内ではxv6のビルドと実行・デバッグのみを行うことを前提としています．
上記のようにしてコンテナを起動した場合，xv6のソースファイルを含むディレクトリ(`/home/xv6/xv6-riscv`)の実体はホストOS側にあります．
したがって，課題などでxv6のソースコードを変更する際は（コンテナを起動したまま）ホストOS側で慣れたエディタを使って作業することができます．

もしコンテナ内にエディタ等をインストールしたい場合は，まず
`sudo apt-get update`
を実行したのち，
`sudo apt-get install -y vim`
のようにしてインストールしてください．

コンテナを起動したときのシェル(bash)は`xv6`というユーザで実行されています．
このユーザのパスワードは`xv6`です．
sudoコマンドを実行する際はこのパスワードを使ってください．


## Macの場合の注意事項
xv6のソースコードのディレクトリ(`xv6-riscv`)は，iCloud Drive以外の場所に作るようにしてください．
iCloud Drive中にあると，Dockerコンテナ内からのアクセス中にエラーが生じるケースがあることが講義Slackで報告されています．
特に，よく使う `~/Documents` や `~/Desktop` がiCloud Driveに含まれる設定になっていることがあるので注意してください．
システム環境設定のApple IDでiCloud Driveのオプションを開くと，これらのディレクトリがiCloud Driveに入っているかどうか確認できます．


## Windowsの場合

Windows用のDocker Desktopをインストールしてください．
WSLで動作するLinux（Ubuntu等）を用いる場合，上で述べた方法で問題なく作業できます．

また，WSL内ではなくWindowsのファイルシステム
内にxv6のソースコードを置いた場合（例えば`C:\Users\takuo\Documents\xv6-riscv`），コマンドプロンプトから以下のようにしてコンテナを起動できます．
```
docker run -it --rm -v C:\\Users\\takuo\\Documents\\xv6-riscv:/home/xv6/xv6-riscv wtakuo/xv6-env
```
実際に作業する場合は，上の`takuo`は各自のユーザ名に置き換えてください．

