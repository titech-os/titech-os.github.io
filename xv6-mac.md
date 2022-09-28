# xv6開発用ツールのインストール（Macの場合）

macOSにクロスコンパイラ等の開発用ツールをインストールして，xv6のビルドと実行を行う方法について説明します．

以下は macOS Big Monterey (12.6) および Big Sur (11.7) でテストしていますが，それ以前のバージョンでもHomebrewが対応していれば問題ないと思います．

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

x86用Homebrewでインストールしたプログラム（実行可能形式）は `/usr/local/bin` に入ります．通常このディレクトリは `PATH` に含まれているので，特になにもしなくてもシェルから実行可能になります．
Apple Silicon搭載のMacの場合，Homebrew関連のプログラム（実行可能形式）は `/opt/homebrew/bin` に格納されます．ターミナルで `which brew` を実行して以下のように出力されれば問題ありません．
```
/opt/homebrew/bin/brew
```
何も出力されないか，`brew not found` のように出力された場合は，`/opt/homebrew/bin` を `PATH` に追加してください．このとき `PATH`内で`/opt/homebrew/bin` は `/usr/local/bin` より前に置くようにしてください．

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
