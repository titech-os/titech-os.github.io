# Dockerによるxv6開発用ツールの実行方法

コンテナ仮想化ツール[Docker](https://www.docker.com)を使ったxv6開発用ツールの実行方法について説明します．
この方法では，各自のPCにクロスコンパイラなどの開発用ツールを個別にインストールする必要はありません．
xv6にしか使わない開発用ツールを自分のPCに直接インストールしたくない場合はこちらの方法を選んでください．

この方法を用いるためには各自のPCにDockerをインストールする必要がありますが，Docker自体は汎用性の高いツールなので，今後も利用する機会は多いと考えられます．
Dockerのインストール方法および使用方法については各自調べてください（MacやWindowsの場合はインストーラをダウンロードして実行するだけです）．
以下，Dockerがインストールされているとして説明します．

## Dockerイメージの取得とコンテナの起動

本講義のために，xv6開発用ツールを含んだDockerイメージ([wtakuo/xv6-env](https://hub.docker.com/r/wtakuo/xv6-env))を用意しました．
まず以下のコマンドでこのDockerイメージを取得してください．
```console
$ docker pull wtakuo/xv6-env
```

これで開発用ツールの実行に必要なものが揃いました．
あとは以下のようにしてコンテナ（ホストOSから隔離された実行環境）を起動してください．
```console
$ docker run -it --rm -v full-path-to-xv6:/home/xv6/xv6-riscv wtakuo/xv6-env
```
ここで`full-path-to-xv6`はRISC-V版xv6のソースコードのディレクトリへのフルパス名に置き換えてください．
このようにしてコンテナを起動することで，
ホストOS（PCで実行しているOS）上の`full-path-to-xv6`で表されるディレクトリが，コンテナ内部で`/home/xv6/xv6-riscv`というディレクトリとしてアクセスできるようになります．

コンテナが無事起動すると以下のようにシェル(bash)のプロンプトが現れます（プロンプトに含まれる`0c765f60374a`は起動したコンテナのIDで，実際にはコンテナ毎に違う値となります）．
```console
xv6@0c765f60374a:~$ 
```
### 具体例

以下のように，ホストOS（PCで実行しているOS）のホームディレクトリ直下に`class/os`というサブディレクトリを作成し，そこにxv6のソースコードを取得したとします．
```console
$ cd
$ mkdir -p class/os
$ cd class/os
$ git clone https://github.com/titech-os/xv6-riscv.git
```
この場合，コンテナの起動は以下のようにして行います．
```console
$ docker run -it --rm -v ~/class/os/xv6-riscv:/home/xv6/xv6-riscv wtakuo/xv6-env
```
上で述べたように，ホストOS上のディレクトリ`~/class/os/xv6-riscv`は，コンテナ内部で`/home/xv6/xv6-riscv`というディレクトリとしてアクセスできるようになります．

## コンテナ内での作業

コンテナ内ではxv6開発用ツールがインストールされたLinux(Ubuntu)が動いています．
以下のようにしてxv6のビルドと実行ができることを確認してください．
```console
xv6@0c765f60374a:~$ cd xv6-riscv
xv6@0c765f60374a:~$ make
xv6@0c765f60374a:~$ make qemu
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
このプログラムの実行後は，いったんxv6から抜けて`fs.img`というファイルを削除しておいてください．

xv6から抜けるには，`ctrl-A`に続けて`x`をタイプします．

## その他

ここで提供しているDockerイメージにはEmacsなどのエディタは含まれていません（イメージサイズをなるべく小さくしたかったので）．
コンテナ内ではxv6のビルドと実行・デバッグのみを行うことを前提としています．
上記のようにしてコンテナを起動した場合，xv6のソースファイルを含むディレクトリ(`xv6-riscv`)の実体はホストOS側にあります．
したがって，課題などでxv6のソースコードを変更する際は（コンテナを起動したまま）ホストOS側で慣れたエディタを使って作業することができます．

もしコンテナ内にエディタ等をインストールしたい場合は，まず
`sudo apt-get update`
を実行したのち，
`sudo apt-get install -y vim`
のようにしてインストールしてください．

コンテナを起動したときのシェル(bash)は`xv6`というユーザで実行されています．
このユーザのパスワードは`xv6`です．
sudoコマンドを実行する際はこのパスワードを使ってください．

## Windowsの場合

Windows用のDocker Desktopをインストールしてください．
WSLで動作するLinux（Ubuntu等）を用いる場合，上で述べた方法で問題なく作業できます．

また，WSL内ではなくWindowsのファイルシステム
内にxv6のソースコードを置いた場合（例えば`C:\Users\takuo\Documents\xv6-riscv`），コマンドプロンプトから以下のようにしてコンテナを起動できます．
```
docker run -it --rm -v C:\\Users\\takuo\\Documents\\xv6-riscv:/home/xv6/xv6-riscv wtakuo/xv6-env
```
実際に作業する場合は，上の`takuo`は各自のユーザ名に置き換えてください．

