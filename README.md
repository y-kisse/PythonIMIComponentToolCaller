# IMI コンポーネントツールを Python スクリプトから動かす

Python スクリプトから経済産業省が公開している [IMI コンポーネントツール](https://info.gbiz.go.jp/tools/imi_tools/index.html) を動かすための構成について検討する.  

## 準備

1. [IMI コンポーネントツール 公開リソースページ](https://info.gbiz.go.jp/tools/imi_tools/index.html) へアクセスする.
2. 住所変換コンポーネントツールの `imi-enrichment-address-2.0.0.tgz` ファイルをダウンロードし, `utils/dummpy_node_project/` 以下に配置する.
3. `npm install imi-enrichment-address-2.0.0.tgz` を行う.  

## 実行

`python3 main.py`  
