# xv6開発用ツールのインストール（Macの場合）

macOSにクロスコンパイラ等の開発用ツールをインストールして，xv6のビルドと実行を行う方法について説明します．

以下は macOS Big Sur (11.1) および Catalina (10.15.7) でテストしていますが，Mojave (10.14.x)やHigh Sierra (10.13.x)でもおそらく同様に作業できると思います．

## Homebrewの準備

開発用ツールのインストールには，Mac用に広く用いられているパッケージ管理システム[Homebrew](https://brew.sh)を使います．
この節ではHomebrewのインストールについて説明しますので，すでに使っている人は飛ばしても構いません．

まず，Appleが提供しているMac用の各種開発用コマンドラインツールが必要ですので，以下のようにしてインストールしておきます（XCodeをすでにインストールしてある場合はこの作業は不要です）．
```console
$ xcode-select --install
```
次に以下のコマンドを実行してHomebrewをインストールします．．
```console
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

## 開発用ツールのインストール

Homebrewがあれば比較的容易です．
最初にHomebrewでRISC-V関連ツールのインストールができるように設定します．
```console
$ brew tap riscv/riscv
```

次にRISC-V用各種ツールとQEMUをインストールします．
```console
$ brew install riscv-tools qemu
```
以上でxv6の開発用ツールのインストールは完了です．

次にコマンドサーチパスの設定の確認をします．
Homebrewでインストールされるプログラムは多くの場合 `/usr/local/bin` という場所にインストールされます（正確にはリンクが作られる）．その場合特にこれ以上設定することはありません．
ただし今回インストールするRISC-V関連のツールの場合，少なくとも私のところでは `/usr/local/bin` に入っているのですが，そうならなかったケースが講義Slackで報告されています．もし
```
which riscv64-unknown-elf-gcc
```
を実行して何も出力されない場合は，シェルの設定ファイル（`~/.zshrc`, `~/.bashrc` 等）に以下のような行を追加してください．
```
PATH=$PATH:/usr/local/opt/riscv-gnu-toolchain/bin
```

## インストール後の作業

以下のようにしてxv6のビルドと実行ができることを確認してください．
カレントディレクトリ直下にgitで取得したRISC-V版xv6のソースコードのディレクトリ`xv6-riscv`があるものとします．

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
最後の`$`はxv6のプロンプトです．
macOS上（RISC-Vをエミュレートする）仮想マシンアプリケーションQEMUが動作し，その上でxv6が
動作しています．
xv6上でいくつかプログラムを動かして動作を確認してみてください．
`usertests`というプログラムを実行すると，多少時間はかかりますがxv6カーネル全体のテストを行うことができます．
このプログラムの実行後は，いったんxv6から抜けて`fs.img`というファイルを削除しておいてください．

xv6から抜けるには，`ctrl-A`に続けて`x`をタイプします．

## 問題点
2020年12月29日時点で上記の方法でインストールされるRISC-V用ツールのうち，デバッガ(`riscv64-unknown-elf-gdb`)の設定にやや問題があることがわかっています．
具体的には，Python用のGDBライブラリがインストールされないため，（Pythonによる支援が必要な）一部のコマンドの実行に問題が生じます．
これを回避するには，まずHomebrewでgdbをインストールします．
```console
$ brew install gdb
```
そしてRISC-V用のgdbを起動する際に `--data-directory` オプションでPythonライブラリの位置を指定します．
```console
$ riscv64-unknown-elf-gdb --data-directory=/usr/local/Cellar/gdb/10.1/share/gdb/python
```
これでxv6-riscvカーネルのデバッグはできるようになります．

面倒な場合はDockerによる方法に切り替えるとよいかもしれません．
