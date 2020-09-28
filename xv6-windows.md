# xv6開発用ツールのインストール（Windowsの場合）

Windowsにクロスコンパイラ等のツールをインストールして，xv6のビルドと実行を行う方法について説明します．

xv6の開発用ツールはUnix系のOSを前提に作られているため，これらを直接インストールするのは難しそうです．
ここでは仮想マシンやWSLを使った間接的な方法を紹介しています．
開発用ツールをインストールせずに[Dockerを使って開発用ツールを実行する方法](xv6-docker.html)も検討してください．

私は普段Windowsは使っていないので，いろいろと間違いやスマートでないことをしているかもしれません．
よりよい方法があったらぜひ教えてください.

対象とするPCのアーキテクチャは64ビット版x86(X86_64)です．
以下はWindows10(バージョン2004)でテストしています．

## 仮想マシンを使う方法

[VirtualBox](https://www.virtualbox.org)や[VMware Workstation Player](https://www.vmware.com/jp/products/workstation-player.html)などの仮想機械アプリケーションを用いてUbuntu等のLinuxをゲストOSとして実行し，その上に[開発用ツールをインストール](xv6-linux.html)します．

## WSL/WSL2を使う方法

[WSL (Windows Subsystem for Linux)](https://docs.microsoft.com/ja-jp/windows/wsl/install-win10)をインストールします．
そしてUbuntu等のLinuxディクトリビューションをインストールして，[開発用ツールをインストール](xv6-linux.html)します．
Ubuntu 20.04で問題なく動作することは確認しています．
