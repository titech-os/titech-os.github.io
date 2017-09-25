# オペレーティングシステム

## お知らせ

* 期末試験を2/10(金)・5-6限に行います．
* 第10回目（**12月6日(火)・9-10限**）は**情報工学科計算機室**で行います．
* 第4回目（**10月18日(火)・9-10限**）は**情報工学科計算機室**で行います．講義資料は前回のものを使います．
* 第2回目（**10月4日(火)・9-10限**）は**情報工学科計算機室**で行います．
* 初回（9月30日(金)・5-6限）はW611講義室で行います．
* 9/23(金)は出張のため休講とします．

## 担当
* 渡部卓雄 (計算工学専攻)

## 講義時間・講義室
* 金曜5-6限，W611
* 今年度はE,Oのクラス別ではなく合同で行います．

## 講義概要
オペレーティングシステム(OS)に関する基本的概念と基本的アルゴリズムを習得する．
OSの基本構造，プロセス管理，メモリ管理，ファイルシステム，デバイス管理などOSに関係する諸理論と実装技術をバランスよく学習する．

## 関連講義等
* プログラミング第1（Cプログラミング）
* プログラミング第3（システムコール）
* アセンブリ言語（X86アセンブラ）
* 計算機アーキテクチャ第一
* 数理論理学
* その他必要事項：Unixの（コマンドラインによる）操作

## 成績評価（詳細は第1回スライドを参照）
* 期末試験(50)
* 小課題(10)×3，中課題(20)×1

## 予定
1. 導入・OSの役割と機能
2. xv6の使い方（演習・計算機室）
3. 割り込みとシステムコール
4. xv6におけるシステムコール（演習・計算機室）
5. プロセス管理
6. プロセスのスケジューリング
7. 同期と排他制御
8. メモリ管理
9. 仮想記憶
10. xv6におけるプロセス・メモリ管理（演習・計算機室）
11. ファイルシステム(1)
12. ファイルシステム(2)
13. I/Oシステム
14. 保護機構とセキュリティメカニズム(1)
15. 保護機構とセキュリティメカニズム(2)，まとめ

## 期末試験
* 日時
  - 2017年2月10日(金) 5-6限
  - 試験室，試験範囲等については後ほどアナウンスします．
* 過去の問題とその解答・解説
  - 2015年度: [問題](https://titech-os.github.io/ex/2015.pdf)・[解答と解説](https://titech-os.github.io/ex/2015a.pdf)
  - 2014年度: [問題](https://titech-os.github.io/ex/2014.pdf)・[解答と解説](https://titech-os.github.io/ex/2014a.pdf)
  - 2013年度: [問題](https://titech-os.github.io/ex/2013.pdf)・[解答と解説](https://titech-os.github.io/ex/2013a.pdf)
  - 2012年度: [問題](https://titech-os.github.io/ex/2012.pdf)・[解答と解説](https://titech-os.github.io/ex/2012a.pdf)
  - 2011年度: [問題](https://titech-os.github.io/ex/2011.pdf)・[解答と解説](https://titech-os.github.io/ex/2011a.pdf)
  - 2010年度: [問題](https://titech-os.github.io/ex/2010.pdf)・[解答と解説](https://titech-os.github.io/ex/2010a.pdf)

## 講義資料
一部の資料や例題などを本Githubグループ(titech-os)を通して配布することがあります．
その際gitおよびGithubの簡単な使い方については説明しますが，gitを使う機会は今後も多いと思いますので，各自参考書やサイトで学んでおいてください．

## 関連・参考サイト
* 本演習のGithubアカウント: http://github.com/titech-os/
  * xv6の講義用Githubリポジトリ: http://github.com/titech-os/xv6-public/
  * GNU GlobalでHTML化したxv6のソースコード: https://titech-os.github.io/xv6-html/
* xv6のオフィシャルサイト: https://pdos.csail.mit.edu/6.828/2016/xv6.html
  * ブックレット https://pdos.csail.mit.edu/6.828/2016/xv6/book-rev9.pdf
  * xv6のオフィシャルGithubリポジトリ: https://github.com/mit-pdos/xv6-public/
* インテル64およびIA-32アーキテクチャー・ソフトウェア・デベロッパーズ・マニュアル: http://www.intel.co.jp/content/www/jp/ja/processors/architectures-software-developer-manuals.html
* git: https://git-scm.com
  * 解説書（日本語版）: https://git-scm.com/book/ja/v2