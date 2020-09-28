# xv6開発用ツールのインストール（Linuxの場合）

Linuxにクロスコンパイラ等の開発用ツールをインストールして，xv6のビルドと実行を行う方法について説明します．

対象とするPCのアーキテクチャは64ビット版x86(X86_64)です．
以下では[Ubuntu Desktop](https://ubuntu.com/download/desktop)20.04LTSでテストしていますが，18.04.5LTS等の他のバージョンや，
Debian等のaptコマンドを使ってパッケージ管理をしているLinuxディストリビューションでもおそらく同様に作業できると思います．
それ以外のディストリビューションについては[MITのサイト](https://pdos.csail.mit.edu/6.828/2020/tools.html)を参考にしてください．

## 開発用ツールのインストール

aptコマンドで容易にインストールできます．
以下のコマンドを実行してください．

```console
$ sudo apt-get install git build-essential gdb-multiarch qemu-system-misc gcc-riscv64-linux-gnu binutils-riscv64-linux-gnu 
```

以上でxv6の開発用ツールのインストールは完了です．

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

