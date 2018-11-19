# システムソフトウェア(CSC.T371)

## お知らせ
* 課題提出状況: [小課題1](https://titech-os.github.io/misc/hw1.txt), [小課題2](https://titech-os.github.io/misc/hw2.txt)
* 小課題2レポートのための[LaTeXテンプレート](https://titech-os.github.io/misc/reptemp2.zip)を用意しました．
* 休講：10月18日(木)
* 第7回（**10月15日(月)・9-10限**）は**情報工学系計算機室**で行います．
* 第3回（**10月1日(月)・9-10限**）は**情報工学系計算機室**で行います．
* 初回（9月27日(木)・7-8限）および第2回（10月1日(月)・7-8限）はスケジュール通りW641講義室で行います．

## 担当
* [渡部卓雄 (情報工学系)](http://www.psg.c.titech.ac.jp/~takuo/)

## 講義時間・講義室
* 月曜7-8限・木曜7-8限
* W641講義室

## 講義概要
オペレーティングシステムの役割，オペレーティングシステムカーネルの構成と実現方式，およびオペレーティングシステムカーネルにおいて用いられるアルゴリズムを理解する．

オペレーティングシステムの中心概念であるカーネルの役割とそこで用いられるアルゴリズムを学ぶ．具体的には，割り込みによるカーネルの実現手法，プロセス管理，同期と排他制御，メモリ管理，ファイルシステム，I/Oシステムなどについて学ぶ，また，Unixを簡素化した教育用オペレーティングシステムxv6を教材として，これらの諸機構がどのように実現されるかについて理解する．

## 関連講義等
* CSC.T243: 手続き型プログラミング基礎
* CSC.T253: 手続き型プログラミング発展
* CSC.T344: システムプログラミング
* CSC.T262: アセンブリ言語
* CSC.T363: コンピュータアーキテクチャ
* その他必要事項：Unixの（コマンドラインによる）操作

## 成績評価（詳細は第1回スライドを参照）
* 期末試験(50)
* 小課題(10)×2，中課題(30)×1

## 予定
1. 導入・オペレーティングシステムの役割と機能
2. 割り込みとシステムコール
3. Unixオペレーティングシステムの概要とxv6（計算機室）
4. プロセスとスレッド(1): 基本概念，マルチプロセス
5. プロセスとスレッド(2): 同期と排他制御アルゴリズム
6. プロセスとスレッド(3): プロセスのスケジューリング
7. プロセスとスレッド(4): プロセス管理機構の実現方式（計算機室）
8. メモリ管理(1)：メモリ管理の目的と基本概念
9. メモリ管理(2): 仮想記憶システムの概要とアルゴリズム
10. メモリ管理(3): 仮想記憶システムの実現方式
11. ファイルシステム(1): ファイルシステムの目的と基本概念
12. ファイルシステム(2): ファイル管理アルゴリズム
13. ファイルシステム(3): ファイルシステムの実現方式
14. I/Oシステムとその実現方式
15. 保護機構とセキュリティ

## 休講予定
11/5(月)と11/8(木)は出張のため休講とします．

## 期末試験

* 日時: 2018年11月26日(月) 7-8限 (15:05-16:35)
* 試験会場: W641
* 試験範囲: 講義で扱った内容
  - プロセス管理，同期機構，メモリ管理，ファイルシステムおよびこれらのxv6における実装
* 持ち込みについて
  - カンニング用紙（A4一枚・手書き）持ち込み可
  - 配布資料とノート，図書，PC等は**持ち込み不可**
* 期末試験については[教務課サイト](https://www.titech.ac.jp/enrolled/life/undergraduate_exam.html)を必ず参照すること．

### 過去の期末試験問題とその解答・解説
* 2017年度: [問題](ex/2017.pdf) / [解答・解説](ex/2017a.pdf)
* 2016年度: [問題](ex/2016.pdf) / [解答・解説](ex/2016a.pdf)
* 2015年度: [問題](ex/2015.pdf) / [解答・解説](ex/2015a.pdf)
* 2014年度: [問題](ex/2014.pdf) / [解答・解説](ex/2014a.pdf)
* 2013年度: [問題](ex/2013.pdf) / [解答・解説](ex/2013a.pdf)
* 2012年度: [問題](ex/2012.pdf) / [解答・解説](ex/2012a.pdf)
* 2011年度: [問題](ex/2011.pdf) / [解答・解説](ex/2011a.pdf)
* 2010年度: [問題](ex/2010.pdf) / [解答・解説](ex/2010a.pdf)

## 講義資料
OCW-iで配布する予定ですが，一部の資料や例題などは本Githubグループ(titech-os)を通して配布することがあります．
その際gitおよびGithubの簡単な使い方については説明しますが，gitを使う機会は今後も多いと思いますので，各自参考書やサイトで学んでおいてください．

## 関連・参考サイト
* 本演習のGithubアカウント: [http://github.com/titech-os/](http://github.com/titech-os/)
  - xv6の講義用Githubリポジトリ: [http://github.com/titech-os/xv6-public/](http://github.com/titech-os/xv6-public/)
  - GNU GlobalでHTML化したxv6のソースコード: [https://titech-os.github.io/xv6-html/](https://titech-os.github.io/xv6-html/)
* xv6のオフィシャルサイト: [https://pdos.csail.mit.edu/6.828/2018/xv6.html](https://pdos.csail.mit.edu/6.828/2018/xv6.html)
  - ブックレット [https://pdos.csail.mit.edu/6.828/2018/xv6/book-rev11.pdf](https://pdos.csail.mit.edu/6.828/2018/xv6/book-rev11.pdf)
  - xv6のオフィシャルGithubリポジトリ: [https://github.com/mit-pdos/xv6-public/](https://github.com/mit-pdos/xv6-public/)
* インテルIA-32アーキテクチャー・ソフトウェア・デベロッパーズ・マニュアル(PDF)
  - [IA-32 インテル ® アーキテクチャ ソフトウェア・デベロッパーズ・ マニュアル（上巻：基本アーキテクチャ）](https://www.intel.co.jp/content/dam/www/public/ijkk/jp/ja/documents/developer/IA32_Arh_Dev_Man_Vol1_Online_i.pdf)
  - [IA-32 インテル ® アーキテクチャ ソフトウェア・デベロッパーズ・ マニュアル（中巻A：命令セット・リファレンス A-M）](https://www.intel.co.jp/content/dam/www/public/ijkk/jp/ja/documents/developer/IA32_Arh_Dev_Man_Vol2A_i.pdf)
  - [IA-32 インテル ® アーキテクチャ ソフトウェア・デベロッパーズ・ マニュアル（中巻B：命令セット・リファレンス N-Z）](https://www.intel.co.jp/content/dam/www/public/ijkk/jp/ja/documents/developer/IA32_Arh_Dev_Man_Vol2B_i.pdf)
  - [IA-32 インテル ® アーキテクチャ ソフトウェア・デベロッパーズ・ マニュアル（下巻：システム・プログラミング・ガイド）](https://www.intel.co.jp/content/dam/www/public/ijkk/jp/ja/documents/developer/IA32_Arh_Dev_Man_Vol3_i.pdf)
* git: [https://git-scm.com](https://git-scm.com)
  - 解説書（日本語版）: [https://git-scm.com/book/ja/v2](https://git-scm.com/book/ja/v2)
