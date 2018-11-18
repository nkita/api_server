# coding:utf-8

# ログのライブラリ
import logging
from logging import getLogger, StreamHandler, Formatter

# --------------------------------
# 1.loggerの設定
# --------------------------------
# loggerオブジェクトの宣言
logger = getLogger(__name__)

# loggerのログレベル設定(ハンドラに渡すエラーメッセージのレベル)
# ERRORを設定したためDEBUGは表示されない
logger.setLevel(logging.ERROR)

# --------------------------------
# 2.handlerの設定
# --------------------------------
# handlerの生成
stream_handler = StreamHandler()

# handlerのログレベル設定(ハンドラが出力するエラーメッセージのレベル)
stream_handler.setLevel(logging.DEBUG)

# ログ出力フォーマット設定
handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(handler_format)

# --------------------------------
# 3.loggerにhandlerをセット
# --------------------------------
logger.addHandler(stream_handler)

# --------------------------------
# ログ出力テスト
# --------------------------------

# こちらDEBUGなため表示されない
logger.debug("Hello World!")

# こちらはERRORなので表示される
logger.error("こんにちは 世界！")
