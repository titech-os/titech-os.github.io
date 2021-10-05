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

### Apple Silicon搭載のMac (M1 Mac)を使う場合

現在HomebrewはM1 Macに対応していますが，Homebrewでインストールされるソフトウェアには，まだApple Siliconに対応していないものもあります．そういったソフトウェアを使いたい場合，x86用のHomebrewもインストールして併用します．x86用のバイナリはRosetta2によってApple Silicon上で実行可能になります．本講義で使うツールのいくつかはx86用Homebrewが必要です．以下のようにして問題なく動作することを確認しています．

まず，x86用のHomebrewをインストールします．ターミナルで以下のコマンドを実行してください．
```console
$ arch -x86_64 -e PATH= /bin/zsh --login
```
zshではなくbashを使っている場合は以下のようにします．
```console
$ arch -x86_64 -e PATH= /bin/bash --login
```
ここで `PATH=` と `/bin/zsh`（あるいは`/bin/bash`の間に空白が入っていることに注意してください．

以上のようにすることで，シェルがx86のプロセスとして（Rosetta2を使って）動作します．
この状態で上に述べた方法と同様にしてHomebrewをインストールします．
あとは下の「開発用ツールのインストール」で述べているようにして必要なツール （`riscv-tools` と `qemu`）をインストールしてください．

Apple Silicon搭載のMacでは，普通にHomebrewをインストールするとHomebrew関連のファイルは `/opt/homebrew` に格納されますが，上記のようにしてx86用にインストールした場合は `/usr/local/` に格納されます．これらは併用できますので，普段はApple Silicon用を使い，x86のみに対応したプログラムのみx86用Homebrewを使ってインストールするとよいでしょう．

x86用Homebrewでインストールしたプログラム（実行可能形式）は `/usr/local/bin` に入ります．通常このディレクトリは `PATH` に含まれているので，特になにもしなくてもシェルから実行可能になります．シェルがApple Siliconのプロセスとして動いている場合（普通にターミナルを起動した場合）も，Rosetta2により問題なく実行できます．

`PATH`については以下に注意してください．
* シェルがApple Siliconのプロセスとして動いている場合（通常の場合）：`PATH`内で`/opt/homebrew/bin` は `/usr/local/bin` より前にあること．
* シェルがx86のプロセスとして動いている場合： `PATH` 内に `/opt/homebrew/bin` がないこと．

`~/.zshrc`（あるいは `~/.bashrc`）等で `PATH` を設定する際に以下のようにするとよいでしょう．

```sh
if [ "$(uname -m)" = "arm64" ]; then
    export PATH="/opt/homebrew/bin:$PATH"
fi
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

xv6から抜けるには`ctrl-A`に続けて`x`をタイプします．

## 問題点
2021年10月5日時点で上記の方法でインストールされるRISC-V用ツールのうち，デバッガ(`riscv64-unknown-elf-gdb`)の設定にやや問題があることがわかっています．
具体的には，Python用のGDBライブラリがインストールされないため，（Pythonによる支援が必要な）一部のコマンドの実行に問題が生じます．
これを簡単に回避するには，まずHomebrewでgdbをインストールします．
```console
$ brew install gdb
```
そしてRISC-V用のgdbを起動する際に `--data-directory` オプションでPythonライブラリの位置を指定します．
```console
$ riscv64-unknown-elf-gdb --data-directory=/usr/local/Cellar/gdb/11.1/share/gdb
```
これでxv6-riscvカーネルのデバッグができるようになります．
