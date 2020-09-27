# xv6のビルドと実行

本講義で教材として用いる教育用オペレーティングシステム[xv6](https://pdos.csail.mit.edu/6.828/2020/xv6.html)を，各自のパーソナルコンピュータ(PC)上でビルドし実行する方法について説明する．

対象とするPCではmacOSあるいはLinuxが動作するものとする．
Windowsの場合は本文書末尾の「Windowsの場合」を参考に各自努力されたい．

---
## 1. xv6のソースコード取得

xv6にはRISC-V版とx86版があるが，本講義ではRISC-V版を扱う．

ここでは版管理システム[git](https://git-scm.com)を使用する．
以下gitに関する用語が頻出する．
gitは現在のソフトウェア開発において必須のツールであり，解説書（例えば[Pro Git](https://git-scm.com/book/ja/)）も多いので各自勉強しておいて欲しい．

RISC-V版xv6のソースコード取得であるが，以下のようにgitを使ってワークツリーを各自のPC上に作成する．
```console
$ git clone https://github.com/titech-os/xv6-riscv.git
```

ここでは[xv6のオリジナルのリポジトリ](https://github.com/mit-pdos/xv6-riscv)ではなく，[講義用に作成したリポジトリ](https://github.com/titech-os/xv6-riscv)から取得している．
演習に使うファイルをこのリポジトリを経由して配布することもあるので，オリジナルではなく講義用のリポジトリを使って欲しい．

---
## 2. ビルド・実行用ツールの準備

xv6をソースコードからビルドするためには，各自のPCで動作しRISC-V用のコードを生成するクロスコンパイラおよび関連ツールが必要である．
ここではRISC-Vの開発元が提供している[RISC-V GNU Compiler Toolchain](https://github.com/riscv/riscv-gnu-toolchain)を使用する．

また，xv6の実行には，RISC-Vをエミュレートする仮想機械(VM)が必要になる．
ここでは様々なアーキテクチャに対応したVMである[QEMU](https://www.qemu.org)を用いる．

情報工学系計算機室のMacにはいずれもインストール済みなので，xv6のソースコードを取得すればすぐにビルド・実行が可能である．
各自のPCにこれらのツールを導入する方法として，ここでは以下の2通りについて説明する．

* Dockerを用いる方法
* 直接インストールする方法

いずれか好きな方を選んでツールを用意しておいてほしい．

---
### 2.1 Dockerを用いる方法

本節ではコンテナ仮想化ツール[Docker](https://www.docker.com)を用いてxv6のビルド・実行用ツールを準備する方法について説明する．
ツールを各自のPCに直接インストールしたい場合はこの節は飛ばしてよい．

この方法を用いるためには各自のPCにDockerをインストールする必要があるが，ツールを個別にインストールするよりも簡単であり，xv6にしか使わない各種ツールを自分のPCに直接インストールしたくない場合はこちらの方法を選ぶとよい．
Docker自体は汎用性の高いツールであり，今後も利用する機会は多いと考えられる．
Dockerのインストール方法および使用方法については各自調べておくこと．
MacやWindowsの場合はインストーラをダウンロードして実行するだけである．

本講義のために，必要なツールを含んだDockerイメージをDocker Hubより取得できるようにしてある．
以下のコマンドでDockerイメージ(`wtakuo/xv6-env`)を取得する．

```console
$ docker pull wtakuo/xv6-env
```

これでxv6のビルド・実行準備に必要なものは揃ったことになる．
あとは以下のようにしてコンテナを起動すればよい．
```console
$ docker run -it --rm -v path-to-xv6:/home/xv6/xv6-riscv wtakuo/xv6-env
```
ここで`path-to-xv6`はRISC-V版xv6のソースコードのディレクトリへのフルパス名である．

例えば以下のようにしてホームディレクトリ直下に`class/os`というサブディレクトリを作成し，そこにxv6のソースコードを取得したとする．
```console
$ cd
$ mkdir -p class/os
$ cd class/os
$ git clone https://github.com/titech-os/xv6-riscv.git
```
この場合，コンテナの起動は以下のようにして行う．
```console
$ docker run -it --rm -v ~/class/os/xv6-riscv:/home/xv6/xv6-riscv wtakuo/xv6-env
```

このようにしてコンテナを起動することで，ホストOS（PCで実行しているOS）上のディレクトリ`~/class/os/xv6-riscv`は，コンテナ内部で`/home/xv6/xv6-riscv`というディレクトリとしてアクセスできるようになる．

コンテナ内ではLinux (Ubuntu)が動作する．
コンテナが無事起動すると，以下のようにシェル(bash)のプロンプトが出る．
ここでプロンプトに含まれる`0c765f60374a`は起動したコンテナのIDであり，実際にはコンテナ毎に違う値となる．
```console
xv6@0c765f60374a:~$ 
```

コンテナ内にはxv6のビルドと実行に必要なツールが揃っているので，以下のようにしてビルド・実行が可能である．
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
最後の`$`はxv6のプロンプトである．
コンテナ内で（RISC-Vをエミュレートする）QEMUが動作し，その上でxv6が動作している．
xv6から抜けるには，`ctrl-A`に続けて`x`をタイプすればよい．

---
### 2.2 直接インストールする方法

ここでは各自のPC上にクロスコンパイラやQEMU等，xv6のビルド・実行に必要なツールをインストールする方法について説明する．
Dockerを用いる方法にくらべるとやや面倒であるが，コンテナを介さない分コンパイル速度や実行速度の点で有利である．
特に，WindowsやMacの上にVMWare等の仮想機械アプリケーションを用いてLinuxを動かし，その上でxv6のビルド・実行をしたい場合は，Dockerを用いる方法ではゲストOSの上でさらにコンテナを動かすことになり，実行速度がかなり低下する．

macOSやLinux上にビルド・実行用ツールをインストールする方法については，xv6の開発元である[MITのサイト](https://pdos.csail.mit.edu/6.828/2020/tools.html)に説明されているので，基本的にはこれに従えばよい．
ただし現時点（2020年9月27日）におけるこのサイトの記述にはやや古いものが含まれている．

#### 2.2.1 macOSの場合

##### 2.2.1.1 Homebrewの準備
Mac用に広く用いられているパッケージ管理ツール[Homebrew](https://brew.sh)を用いる．

まず，Mac用の各種開発用ツール（コマンドラインツール）を以下のようにしてインストールしておく（XCodeをすでにインストールしてある場合は不要）．
```console
$ xcode-select --install
```
次に以下のコマンドを実行してHomebrewをインストールする．
```console
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

##### 2.2.1.2 ツールのインストール
HomebrewでRISC-V関連ツールをインストールできるように設定する．
```console
$ brew tap riscv/riscv
```

RISC-V用各種ツールをインストールする．
```console
$ brew install riscv-tools
```
[MITのサイト](https://pdos.csail.mit.edu/6.828/2020/tools.html)にはコマンドサーチパスを設定するように述べられているが，現在は不要である．

最後にQEMUをインストールする．
```console
$ brew install qemu
```

以上でxv6のビルド・実行用ツールのインストールは完了である．
以下のようにしてxv6のビルドと実行ができることを確認すること．

```console
$ cd xv6-riscv
$ make
$ make qemu
...
xv6 kernel is booting

hart 2 starting
hart 1 starting
init: starting sh
$ 
```
最後の`$`はxv6のプロンプトである．
macOS上で（RISC-Vをエミュレートする）QEMUが動作し，その上でxv6が動作している．
xv6から抜けるには，`ctrl-A`に続けて`x`をタイプすればよい．

#### 2.2.2 Linuxの場合（X86_64, apt使用）

ここではDebianやUbuntu等，aptコマンドを使ってパッケージ管理をしているLinuxディストリビューションを使う場合について説明する．
他のディストリビューションについては[MITのサイト](https://pdos.csail.mit.edu/6.828/2020/tools.html)を参考にしてほしい．
対象とするアーキテクチャは64ビット版x86(X86_64)である．

以下のコマンドで必要なツールをインストールする．

```console
$ sudo apt-get install git build-essential gdb-multiarch qemu-system-misc gcc-riscv64-linux-gnu binutils-riscv64-linux-gnu 
```

以上でxv6のビルド・実行用ツールのインストールは完了である．
以下のようにしてxv6のビルドと実行ができることを確認すること．

```console
$ cd xv6-riscv
$ make
$ make qemu
...
xv6 kernel is booting

hart 2 starting
hart 1 starting
init: starting sh
$ 
```
最後の`$`はxv6のプロンプトである．
Linux上で（RISC-Vをエミュレートする）QEMUが動作し，その上でxv6が動作している．
xv6から抜けるには，`ctrl-A`に続けて`x`をタイプすればよい．

---
## 3. Windowsの場合

おそらくもっとも簡単な方法は，[VirtualBox](https://www.virtualbox.org)や[VMware Workstation Player](https://www.vmware.com/jp/products/workstation-player.html)などの仮想機械アプリケーションを用いてUbuntu等のLinuxをゲストOSとして実行し，その上で上述のLinuxを対象とした方法を行うことである．

または，Windows版のDocker Desktopをインストールして，上述のDockerを利用する方法を行うことも可能と思われる．

あるいは，WSL2で動作するLinuxに各種ツールを直接インストールすることも可能かもしれない．

申し訳ないが講義担当者は普段Windowsを使っていないので，インストール方法やノウハウを講義のSlackで共有してもらえると助かる．
