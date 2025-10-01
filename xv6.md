# xv6のビルドと実行のしかた

本講義で教材として用いる教育用オペレーティングシステム[xv6](https://pdos.csail.mit.edu/6.828/2025/xv6.html)を，各自のパーソナルコンピュータ(PC)上でビルドし実行する方法について説明します．

間違いやスマートでないやり方を含んでいる可能性がありますので，間違いの指摘やコメント等を歓迎します．

---
## xv6のソースコード取得

xv6にはRISC-V版とx86版がありますが，本講義ではRISC-V版を使用します．

ソースコードの取得や更新を行うために，版管理システム[git](https://git-scm.com)を使用します．
以下gitに関する用語が頻出しますが，gitは現在のソフトウェア開発において必須のツールで，解説書（例えば[Pro Git](https://git-scm.com/book/ja/)）も多いので各自勉強しておいてください．

RISC-V版xv6のソースコードを取得するには以下のコマンドを実行します．
```console
$ git clone https://github.com/titech-os/xv6-riscv.git
```

ここでは[xv6のオリジナルのリポジトリ](https://github.com/mit-pdos/xv6-riscv)ではなく，[講義用に作成したリポジトリ](https://github.com/titech-os/xv6-riscv)から取得しています．
演習に使うファイルをこのリポジトリを経由して配布しますので，オリジナルではなく講義用のリポジトリを使ってください．

## ビルド・実行用ツールの準備

xv6をソースコードからビルドするためには，各自のPCで動作しRISC-V用のコードを生成するクロスコンパイラおよび関連ツールが必要です．
ここではRISC-Vの開発元が提供している[RISC-V GNU Compiler Toolchain](https://github.com/riscv/riscv-gnu-toolchain)を使用します．

また，xv6を実行するために，RISC-Vをエミュレートする仮想機械(VM)を使用します．
ここでは様々なアーキテクチャに対応したVMである[QEMU](https://www.qemu.org)を用います．

これらの開発用ツールは情報工学系計算機室のMacにはインストールされているので，xv6のソースコードを取得すればすぐにビルド・実行が可能です．
各自のPCでこれら開発用ツールを実行する方法として，ここでは以下の2通りについて説明します．

* [Dockerを使って開発用ツールを実行する](xv6-docker.html)
* PCに開発用ツールをインストールする
  - [Macの場合](xv6-mac.html)
  - [Linuxの場合](xv6-linux.html)
  - [Windowsの場合](xv6-windows.html)

いずれか好きな方法を選んで各自のPCで開発用ツールを使えるようにしてください．
