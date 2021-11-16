# 課題2-2：ディスクイメージ操作プログラムmyopfsの作成

以下で説明するツール opfs の機能をもつプログラム myopfs をC/C++以外の自分の得意な言語で作成せよ．
ただし作成するコマンドは最低限 `ls`, `get`, `put`, `rm` でよいが，これ以外のコマンドを実装してもよい．
また，opfsにない便利なコマンドを考案・実装した場合は加点の対象となる．
macOSあるいはLinuxで動作すること．

## opfsについて
xv6-riscvディレクトリで `make qemu` を実行すると fs.img というファイルが作られる．
これは本来ハードディスク等の二次記憶上に展開されるxv6のファイルシステム全体を（ホストOSの）ファイルとしたもので，ディスクイメージと呼ばれる．
Makefileをみるとわかるが，fs.imgはmkfsという（ホストOS上で動作する）プログラムによって作成されている．
mkfsの機能はfs.imgの作成だけでそれ以外のことはできない．
ホストOS上でディスクイメージを操作し，ファイルシステムのブラウズや変更ができるツールがあると便利だと考え，渡部は以前opfsというツールを作成した．

### opfsの使用方法
opfsはホストOSのシェルで以下のようにして起動する．
```
opfs img_file command
```
ここで `img_file` はイメージファイル（fs.img等），`command` は以下のいずれかである．

* `diskinfo` : ディスクイメージ上のxv6ファイルシステムの情報を表示する．
* `info path` : `path` で指定される（xv6ファイルシステム内の）ファイルやディレクトリの情報を表示する．
* `ls path` : `path` で指定される（xv6ファイルシステム内の）ディレクトリの内容をリストアップする．
`path` で指定されるものが（xv6ファイルシステム内の）ディレクトリ以外のファイルのときはそのファイルのみをリストアップする．
* `get path` : `path` で指定される（xv6ファイルシステム内の）ファイルの内容を標準出力に出力する．
* `put path` : 標準入力に与えられた内容を`path` で指定される（xv6ファイルシステム内の）ファイルに上書きコピーする．
当該ファイルがないときは新たに作成する．
* `rm path` : `path` で指定される（xv6ファイルシステム内の）ファイルを削除する．
* `cp spath dpath` : `spath` で指定されるファイルの内容を `dpath` で指定されるファイルに上書きコピーする．
`dpath` で指定されるファイルがないときは新たに作成する．
`dpath` で指定されるものがディレクトリの場合はそのディレクトリの下にファイルが作られる．
* `mv spath dpath` : `spath` で指定されるファイルを `dpath` 
* `ln spath dpath` : `spath` で指定されるファイルへのリンクを `dpath` で指定されるディレクトリに作成する．
* `mkdir path` : `path` で指定される空のディレクトリを作成する．
すでに存在する場合はエラーとする．
* `rmdir path` : `path` で指定される空のディレクトリを削除する．
当該ディレクトリが空でない場合はエラーとする．

### opfsの利用例
ディスクイメージfs.img内のファイルシステムのルートディレクトリにあるファイルをリストアップする．
```
% opfs fs.img ls /
. 1 1 1024
.. 1 1 1024
README 2 2 2226
cat 2 3 24488
echo 2 4 23312
forktest 2 5 13464
grep 2 6 27784
init 2 7 23952
kill 2 8 23272
ln 2 9 23112
ls 2 10 26680
mkdir 2 11 23400
rm 2 12 23392
sh 2 13 42112
stressfs 2 14 24264
usertests 2 15 157192
grind 2 16 38344
wc 2 17 25592
zombie 2 18 22648
console 3 19 0
```

ディスクイメージfs.img内のファイルREADMEの内容を標準出力に出力する．
この実行例ではリダイレクション（`>`）を使ってopfsの出力をホストOSのファイルREADME_xv6.txtに書き込んでいる．その後headコマンドで最初の3行だけを表示している．
```
% opfs fs.img get README > README_xv6.txt
% head -3 README_xv6.txt
xv6 is a re-implementation of Dennis Ritchie's and Ken Thompson's Unix
Version 6 (v6).  xv6 loosely follows the structure and style of v6,
but is implemented for a modern RISC-V multiprocessor using ANSI C.
```

ディスクイメージfs.img内のファイルシステムに関する諸情報を出力する．
```
% opfs fs.img diskinfo
magic: 10203040
total blocks: 1000 (1024000 bytes)
log blocks: #2-#31 (30 blocks)
inode blocks: #32-#44 (13 blocks, 200 inodes)
bitmap blocks: #45-#45 (1 blocks)
data blocks: #46-#999 (954 blocks)
maximum file size (bytes): 274432
# of used blocks: 604
# of used inodes: 19 (dirs: 1, files: 17, devs: 1)
```

### opfsのソースコード
opfsはCで実装されている．ソースコードは以下にある．
* https://github.com/wtakuo/opfs

上記リポジトリにはopfsのソースコード以外に，好きなパラメタでディスクイメージを作ることのできるnewfsおよびファイルシステムの各パラメタを任意に変更できるmodfsのソースコードが含まれている．

講義で提供しているDockerイメージにはこれらのコマンドの実行形式が含まれているので，すぐに試してみることができる．

## 提出物
以下の提出物を 学籍番号_名前（苗字のローマ字）という名前のディレクトリ（フォルダ）に入れること．このディレクトリをzip等で圧縮してT2SCHOLAで提出すること．
* レポート：PDFあるいはプレインテキスト（markdown等も可）とする．ファイル名（拡張子除く）は上位フォルダ名と同じとする．
* 作成したプログラムのソースコード：srcというサブディレクトリを作り，作成したプログラムのソースコードおよびビルドに必要なファイル(Makefile等)一式を入れること．ビルドと実行に必要な情報（使用した言語，言語処理系とそのバージョンおよび入手方法，ビルドに必要なツール，ライブラリ等のバージョンと入手方法およびビルド・実行方法，開発・テストに使用した環境等）をテキストファイルREADME.txtに明記すること．

提出するフォルダの構成例を示す．ビルドツールの都合でsrc下にサブディレクトリを作るのは構わない．
```
19B99999_Watanabe
├── 19B99999_Watanabe.pdf
└── src
    ├── Makefile
    ├── myopfs.ml
    └── README.txt
```

