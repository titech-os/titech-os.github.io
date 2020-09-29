# xv6開発用ツールのインストール（Windowsの場合）

Windowsにクロスコンパイラ等のツールをインストールして，xv6のビルドと実行を行う方法について説明します．

xv6のビルドに必要な
[RISC-V GNU Compiler Toolchain](https://github.com/riscv/riscv-gnu-toolchain)をWindowsに直接インストールするのは難しそうです（Unix系のOSを前提に作られているため）．
一方xv6の実行に必要な[QEMU](https://www.qemu.org)はWindows用のバイナリも公式に配布されています．

もしRISC-Vのツールチェーンを[Cygwin](https://www.cygwin.com)や[MinGW](http://www.mingw.org)用にビルドすることができれば，これをxv6のビルドに使い，Windows用のQEMUを用いることでWindowsネイティブ(?)なxv6のビルド・実行環境ができるかも知れません（どなたかチャレンジしてみてください）．
ここでは仮想マシンやWSLを使った間接的な方法を紹介します．
開発用ツールをインストールせずに[Dockerを使って開発用ツールを実行する方法](xv6-docker.html)も検討してください．

対象とするPCのアーキテクチャは64ビット版x86(X86_64)です．
以下はWindows10(バージョン2004)でテストしています．

## WSL/WSL2を使う方法

[WSL (Windows Subsystem for Linux)](https://docs.microsoft.com/ja-jp/windows/wsl/install-win10)をインストールします．
そしてUbuntu等のLinuxディクトリビューションをインストールして，[開発用ツールをインストール](xv6-linux.html)します．
現在，WSL2上のUbuntu 20.04に開発用ツールをインストールし，問題なくxv6をビルド・実行できることは確認しています．

## WSL仮想マシンを使う方法

[VirtualBox](https://www.virtualbox.org)や[VMware Workstation Player](https://www.vmware.com/jp/products/workstation-player.html)などの仮想機械アプリケーションを用いてUbuntu等のLinuxをゲストOSとして実行し，その上に[開発用ツールをインストール](xv6-linux.html)します．

