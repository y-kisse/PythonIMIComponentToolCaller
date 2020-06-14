import os
import subprocess
import json
from shlex import quote

class AddressFormatter:
    """
    IMI コンポーネントツールに含まれる, imi-enrichment-address コマンドを呼び, その結果を返す.
    """

    @classmethod
    def call_enrichment_tool(cls, target):
        """

        Args:
            target (string): 対象住所文字列
        Return:
            IMIFormattedAddress
        """

        cmdstr = "npx imi-enrichment-address -s {}".format(quote(target))
        node_directory = os.path.join(os.path.dirname(__file__), "dummy_node_project")
        response = subprocess.run(cmdstr, stdout=subprocess.PIPE, shell=True, cwd=node_directory)

        return IMIFormattedAddress(response.stdout.decode("utf8"))

class IMIFormattedAddress:
    """
    IMI コンポーネントツールの imi-enrichment-address コマンドのレスポンスを格納し, アクセス方法を提供するクラス.
    """

    def __init__(self, cmdresponse):
        """
        CLI のテキストレスポンスを受け取り, json オブジェクトとしてインスタンス変数として格納する.
        """
        self.cmdresponse = json.loads(cmdresponse)
        
    def __str__(self):
        return json.dumps(self.cmdresponse, indent=2, ensure_ascii=False)