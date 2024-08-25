"""
@Project   : zh_TW
@Author    : abudu & Deepseek
@Blog      : https://www.oplog.cn
"""

from ..core import Language


class Main(Language):
    name = 'zh_TW'
    name_local = "中文(繁體)"
    default = {
        "name": name,
        "data": {
            "ADD": "添加",
            "ADD_CATEGORY": "添加分類",
            "ADD_SUCCESS": "添加成功！",
            "ADD_TAG": "添加標籤",
            "ADVANCED": "高級設置",
            "ADVANCED_SETTINGS": "高級設置",
            "ADVANCED_SETTINGS_LABEL": "高級設置",
            "API_VERIFY_FAILED": "API鑒權失敗, 訪問IP: {}",
            "AUTHOR": "作者",
            "AUTO_PROVIDER_FAILED": "自動生成PROVIDER錯誤，請檢查配置並提交",
            "BACKUP": "備份文件",
            "BOTTOM_PH": "若有多級, 請使用JSON格式",
            "CACHE": "緩存",
            "CACHE_CLEAN_REQUEST": "確定清除所有緩存嗎",
            "CANCEL": "取消",
            "CAPTCHA_FAILED": "人機驗證失敗!",
            "CAPTCHA_GET_FAILED": "獲取失敗",
            "CAPTCHA_NO": "未收到人機驗證信息",
            "CAPTCHA_RESULT": "reCaptcha{}結果: {}",
            "CATEGORY_EXITS": "分類已存在!",
            "CHANGE_LANGUAGE": "切換語言",
            "CLEAN_FLINKS_FAILED": "無隱藏的友鏈",
            "CLEAN_FLINKS_SUCCESS": "成功清理了{}條友鏈",
            "CLEAR_ALL": "清除全部",
            "CLOSE": "關閉",
            "CLOUD_SCRIPTS": "雲端命令庫",
            "COMMAND": "命令",
            "CONFIG": "配置",
            "CONFIGS_LIST": "配置列表",
            "CONFIG_LABEL": "全部配置",
            "CONFIG_NAME": "配置名",
            "CONFIRM": "確定",
            "CONFIRM_CLEAN_FLINK": "確認要清理隱藏的鏈接嗎？該操作不可回退",
            "CONFIRM_DEL_CUSTOM": "確認要刪除 {0} 字段嗎？該操作不可回退",
            "CONFIRM_FIX": "確認要嘗試自動修復程序嗎？這會檢查並創建/刪除相應字段",
            "CONFIRM_RUN": "確認要執行 {0} 嗎？此操作不可中止",
            "CONSOLE": "管理面板",
            "CONTENT": "內容",
            "CURRENT_ENV": "當前環境",
            "CUSTOM": "自定",
            "CUSTOMIZE": "個性化",
            "CUSTOMIZE_LABEL": "儀表盤樣式配置項",
            "CUSTOM_LABEL": "自定義字段",
            "CUSTOM_LIST": "自定義字段",
            "DARKMODE": "淺色 / 深色",
            "DASHBOARD": "控制台",
            "DELETING": "正在刪除中...",
            "DEL_CONFIRM_1": "確認要刪除",
            "DEL_CONFIRM_2": "嗎？此操作不可撤回",
            "DEL_FAILED": "刪除失敗",
            "DEL_POST_INDEX": "刪除文章詳情索引",
            "DEL_REMOTE": "刪除遠程文件",
            "DEL_SUCCESS": "刪除成功!",
            "DEL_SUCCESS_AND_DEPLOY": "刪除成功並提交部署!",
            "DEL_TMP": "刪除臨時目錄",
            "DEL_VALUE": "刪除字段",
            "DESCRIPTION": "簡介",
            "DOC": "文檔",
            "DRAFT": "草稿",
            "DRAFT_SAVE_SUCCESS": "草稿保存成功!",
            "DRAFT_SAVE_SUCCESS_AND_DEPLOY": "草稿保存成功並提交部署!",
            "EDIT": "編輯",
            "EDIT_CONFIG": "編輯配置",
            "EDIT_FLINK": "編輯友鏈",
            "EDIT_PAGE": "編輯頁面",
            "EDIT_PAGE_LABEL": "編輯頁面",
            "EDIT_POST": "編輯文章",
            "EDIT_POST_LABEL": "編輯文章",
            "EDIT_SIDEBAR": "編輯側邊欄",
            "EDIT_SUCCESS": "修改成功！",
            "EDIT_TALK": "編輯說說",
            "EDIT_TALK_LABEL": "編輯說說",
            "EDIT_TALK_PH": "在這裡書寫說說...",
            "ELEVATOR_ERROR": "自動更新遷移程序出錯: {}",
            "ELEVATOR_START": "開始運行自動更新遷移程序...來自{}",
            "ERROR": "錯誤",
            "ERROR_GETTING_PROVIDER": "獲取PROVIDER時出錯",
            "EXCERPT_FAILED": "摘要獲取失敗: ",
            "EXCERPT_LOADING": "摘要獲取中...",
            "EXCERPT_LOCAL_LENGTH": "摘要長度",
            "EXCERPT_LOCAL_LENGTH_PH": "截取的長度",
            "EXCERPT_TIANLI_KEY": "用戶密鑰",
            "EXCERPT_TIANLI_KEY_PH": "在愛發電獲得的用戶密鑰",
            "EXCERPT_TIANLI_LENGTH": "發送長度",
            "EXCERPT_TIANLI_LENGTH_PH": "發送到服務端的內容長度",
            "EXPORT": "導出",
            "FIND_INDEX_FAILED": "'更新失敗: 未找到Index目錄",
            "FIND_INDEX_SUCCESS": "找到Index目錄",
            "FIND_UPDATE_INDEX": "解壓完成, 尋找Index目錄",
            "FINISH": "完成",
            "FIXING": "嘗試修復中...請耐心等待",
            "FIX_DISPLAY": "嘗試自動修復了 {} 個字段，請在稍後檢查和修改配置",
            "FIX_SUCCESS": "已修復{}個設置",
            "FIX_VALUE": "修正字段",
            "FLINK": "友鏈",
            "FLINKS_LIST": "友情鏈接",
            "FLINK_LABEL": "友情鏈接",
            "FORCE_MSG": "確定要強制提交嗎？",
            "FORCE_SUBMIT": "強制提交",
            "FRONT_MATTER_GET_ERROR": "FrontMatter解析失敗: {}",
            "GET_ADVANCED_SETTINGS_FAILED": "高級設置獲取錯誤: {}",
            "GET_CUSTOM_FAILED": "自定義字段獲取錯誤: {}",
            "GET_PAGE_SCAFFOLD_FAILED": "獲取頁面模板失敗, 錯誤信息: {}",
            "GET_POST_SCAFFOLD_FAILED": "獲取文章模板失敗, 錯誤信息: {}",
            "GET_SCRIPTS_FAILED": "在線函數庫獲取錯誤: {}",
            "GET_SETTINGS_FAILED": "配置獲取錯誤, 轉跳至配置更新頁面",
            "GET_UPDATE_FAILED": "獲取更新失敗",
            "GET_UPDATE_SUCCESS": "獲取更新成功",
            "HAS_MSG_TIP_1": "你有",
            "HAS_MSG_TIP_2": "則未讀消息",
            "HEADER": "標頭",
            "HELP": "幫助",
            "HELP_LABEL": "需要幫助?",
            "HELP_TIP": "點擊這裡查找文檔",
            "HEXO_CONFIG": "\n檢測到Hexo配置文件",
            "HEXO_CONFIG_FAILED": "\n未檢測到Hexo配置文件",
            "HEXO_CONFIG_UPDATE": "\nHexo配置文件更新成功",
            "HEXO_CONFIG_UPDATE_FAILED": "\n配置校驗失敗",
            "HEXO_INDEX_FAILED": "\n檢測到index.html, 這可能不是正確的倉庫",
            "HEXO_PACKAGE": "\n檢測到package.json",
            "HEXO_PACKAGE_FAILED": "\n未檢測到package.json",
            "HEXO_SOURCE": "\n檢測到source目錄",
            "HEXO_SOURCE_FAILED": "\n未檢測到source目錄",
            "HEXO_THEME": "\n檢測到主題目錄",
            "HEXO_THEME_FAILED": "\n未檢測到主題目錄",
            "HEXO_TOKEN_FAILED": "遠程連接錯誤!請檢查Token",
            "HEXO_VERSION": "檢測到Hexo版本: {}",
            "HEXO_VERSION_FAILED": "未檢測到Hexo",
            "HOME": "主頁",
            "ICON": "圖標",
            "ID_CODE": "識別代號",
            "IMAGE": "圖片",
            "IMAGES_LIST": "圖片列表",
            "IMAGE_DEL_SUCCESS": "已刪除本地記錄",
            "IMAGE_LABEL": "全部圖片",
            "IMAGE_LINK": "圖片鏈接",
            "IMAGE_NAME": "圖片名",
            "IMPORT": "導入",
            "IMPORT_WARN": "導入後, 您將會丟失現有的全部信息, 請確認!",
            "INDEX_GITHUB_TIP": "支持作者",
            "INDEX_GUIDE_LABEL": "現在要做點什麼？",
            "INDEX_GUIDE_LABEL_1": "新文章",
            "INDEX_GUIDE_LABEL_2": "新頁面",
            "INDEX_GUIDE_LABEL_3": "新友鏈",
            "INDEX_GUIDE_LABEL_4": "新說說",
            "INDEX_GUIDE_TIP_1_P1": "寫下你的",
            "INDEX_GUIDE_TIP_1_P2": "新構思",
            "INDEX_GUIDE_TIP_2_P1": "創建你的",
            "INDEX_GUIDE_TIP_2_P2": "新頁面",
            "INDEX_GUIDE_TIP_3_P1": "添加你的",
            "INDEX_GUIDE_TIP_3_P2": "新朋友",
            "INDEX_GUIDE_TIP_4_P1": "分享你的",
            "INDEX_GUIDE_TIP_4_P2": "新動態",
            "INDEX_IMAGE_LABEL": "總圖片",
            "INDEX_IMAGE_TIP": "嘗試圖片管理",
            "INDEX_POST_LABEL": "總文章",
            "INDEX_POST_TIP": "今天你寫文章了嗎",
            "INDEX_RANDOM_POSTS": "隨機文章",
            "INDEX_RECENT_IMAGES": "最近圖片",
            "INDEX_RECENT_POSTS": "最近文章",
            "INDEX_VERSION_HASNEW": "檢測到更新",
            "INDEX_VERSION_LABEL": "當前版本",
            "INDEX_VERSION_TIP": "是最新版哦",
            "INIT": "初始化",
            "INIT_2_1": "API 密鑰",
            "INIT_2_1_PH": "留空即自動生成",
            "INIT_2_2": "用戶名",
            "INIT_2_2_PH": "設置用戶名",
            "INIT_2_3": "密碼",
            "INIT_2_3_PH": "設置密碼",
            "INIT_2_4": "確認密碼",
            "INIT_2_4_PH": "再次輸入以確認密碼",
            "INIT_3_1": "服務商",
            "INIT_3_2": "使用配置",
            "INIT_4_1": "Vercel 密鑰",
            "INIT_4_2": "項目 ID",
            "INIT_BLOG": "博客配置",
            "INIT_FINISH": "恭喜您初始化完畢",
            "INIT_IMAGE": "圖床配置",
            "INIT_LOGIN_MSG_1": "請牢記您的登錄信息：",
            "INIT_LOGIN_MSG_2": "用戶名: ",
            "INIT_LOGIN_MSG_3": "密碼: 您設定的值",
            "INIT_LOGIN_MSG_4": "登錄控制台",
            "INIT_PROVIDER_FAILED": "初始化PROVIDER錯誤: {}",
            "INIT_SUCCESS": "已完成初始化, 轉跳至首頁",
            "INIT_USER": "用戶配置",
            "INIT_USER_FAILED": "初始化用戶名密碼錯誤: {}",
            "INIT_VERCEL": "Vercel 配置",
            "INIT_VERCEL_FAILED": "初始化Vercel錯誤: {}",
            "INIT_WELCOME": "歡迎！請選擇語言以開始初始化",
            "INPUT_ARGV": "請輸入參數",
            "JUMPED": "跳過",
            "JUMP_UPDATE": "檢測到更新配置, 轉跳至配置更新頁面",
            "JUMP_UPDATE_FAILED": "檢測配置更新失敗, 轉跳至更新頁面",
            "LEAVE_CONFIRM": "確定要離開嗎?",
            "LINK": "鏈接",
            "LOADING": "正在加載中...",
            "LOCAL": "本地",
            "LOCAL_UPDATE_SUCCESS": "更新完成，五秒後重啟線程",
            "LOGIN": "登錄",
            "LOGIN_FAILED": "登錄信息錯誤",
            "LOGIN_FAILED_1": "用戶名不能為空! ",
            "LOGIN_FAILED_2": "密碼不能為空! ",
            "LOGIN_FAILED_3": "請完成驗證! ",
            "LOGIN_SUCCESS": "登錄成功，等待轉跳",
            "LOGOUT": "註銷",
            "LOGOUT_SUCCESS": "註銷成功",
            "LOVE": "點贊",
            "MEASURE_IMAGE": "張",
            "MEASURE_LINK": "條",
            "MEASURE_POST": "篇",
            "MIGRATE": "遷移",
            "MIGRATE_CONFIG_SUCCESS": "遷移配置完成！",
            "MIGRATE_CUSTOM_SUCCESS": "遷移自定義字段完成！",
            "MIGRATE_DB": "開始遷移數據庫",
            "MIGRATE_FAILED": "遷移{}失敗: {}",
            "MIGRATE_FLINKS_SUCCESS": "遷移友鏈完成！",
            "MIGRATE_IMAGE_SUCCESS": "遷移圖片完成！",
            "MIGRATE_LABEL": "遷移配置",
            "MIGRATE_MSG_SUCCESS": "遷移消息完成！",
            "MIGRATE_POST_SUCCESS": "遷移文章索引完成！",
            "MIGRATE_PV_SUCCESS": "遷移PV完成！",
            "MIGRATE_SUCCESS": "全部遷移完成!",
            "MIGRATE_TALKS_SUCCESS": "遷移說說完成！",
            "MIGRATE_UV_SUCCESS": "遷移UV完成！",
            "MSG_LOADING": "消息獲取中...",
            "MSG_LOAD_ERROR": "消息加載失敗",
            "NAME": "名稱",
            "NAVBAR_FIX": "頂欄固定",
            "NETWORK_ERROR": "網絡錯誤!",
            "NEW_FLINK": "新增友鏈",
            "NEW_NAME": "新名稱",
            "NEW_PAGE": "新建頁面",
            "NEW_PAGE_LABEL": "新建頁面",
            "NEW_POST": "新建文章",
            "NEW_POST_LABEL": "新建文章",
            "NEW_VALUE": "新建字段",
            "NEXT": "下一步",
            "NEXT_PAGE": "下一頁",
            "NEW": "新建",
            "NEW_PH": "檔案將被保存為",
            "NOT_INIT": "未完成初始化配置, 轉跳到初始化頁面",
            "NO_MSG_TIP": "你當前沒有消息喲~",
            "NO_NEXT_PAGE": "已是最後一頁",
            "NO_OTHER_ARGV": "暫無其他參數",
            "NO_PAGE_NAME": "請在頂欄輸入正確的頁面名！",
            "NO_PERMISSION": "子用戶不支持此操作！",
            "NO_POST_NAME": "請在頂欄輸入正確的文章名！",
            "NO_PREV_PAGE": "已是第一頁",
            "ONEKEY_UPDATE": "一鍵更新",
            "OPERATION": "操作",
            "OPERATION_SUCCESS": "操作成功!",
            "OTHER_ARGV": "其他參數",
            "PAGE": "頁面",
            "PAGES_LIST": "頁面列表",
            "PAGE_403_LABEL": "錯誤! Error 403",
            "PAGE_403_TIP": "驗證錯誤 - 請確認是否擁有權限",
            "PAGE_404": "頁面不存在: {}",
            "PAGE_404_LABEL": "錯誤! Error 404",
            "PAGE_404_TIP": "找不到頁面 - ",
            "PAGE_500": "服務端錯誤: {}",
            "PAGE_500_LABEL": "錯誤! Error 500",
            "PAGE_500_TIP": "報錯信息：",
            "PAGE_ARGV_LABEL": "頁面參數",
            "PAGE_EXIST": "頁面已存在!",
            "PAGE_LABEL": "全部頁面",
            "PAGE_NAME": "頁面名",
            "PASSWORD": "密碼",
            "POST": "文章",
            "POSTS_LIST": "文章列表",
            "POST_ARGV_LABEL": "文章參數",
            "POST_EXIST": "文章已存在!",
            "POST_LABEL": "全部文章",
            "POST_NAME": "文章名",
            "PREV_PAGE": "上一頁",
            "PROJECT_PAGE": "項目頁面",
            "PROVIDER_NO_SUPPORT": "服務商不支持！",
            "PROVIDER_VERIFY_ERROR": "校驗配置出錯",
            "PROVIDER_VERIFY_SUCCESS": "Provider校驗結果: {}",
            "PUBLISHED": "已發布",
            "PUBLISH_SUCCESS": "發布成功!",
            "PURGE_ALL_CACHE_SUCCESS": "清除全部緩存成功",
            "PURGE_CACHE": "清除緩存",
            "QEXO_MSG": "Qexo消息",
            "READ_FILE": "讀取文件",
            "REBUILD_CACHE_SUCCESS": "重建{}緩存成功",
            "RENAME": "重命名",
            "RENAME_SUCCESS": "重命名成功!",
            "RENAME_SUCCESS_AND_DEPLOY": "重命名成功並提交部署!",
            "REQUIRED": "必填",
            "RESET": "重置",
            "RESET_PASSWORD_NO": "請輸入正確的密碼！",
            "RESET_PASSWORD_NO_MATCH": "兩次密碼不一致!",
            "RESET_PASSWORD_NO_OLD": "原密碼錯誤!",
            "RESET_PASSWORD_NO_PASSWORD": "密碼不能為空！",
            "RESET_PASSWORD_NO_USERNAME": "請輸入正確的用戶名！",
            "RESULT": "結果",
            "RETRY": "重試",
            "RUNNING": "正在運行中...",
            "SAVE_CUSTOM": "保存自定義字段",
            "SAVE_FAILED": "保存失敗!",
            "SAVE_SETTING": "保存設置",
            "SAVE_SUCCESS": "保存成功!",
            "SAVE_SUCCESS_AND_DEPLOY": "保存成功並提交部署!",
            "SAVE_SUCCESS_REDIRECT": "保存成功, 轉跳中...",
            "SAVING": "正在保存中...",
            "SCRIPTS_LABEL": "雲端命令",
            "SCRIPTS_LIST": "在線函數庫",
            "SCRIPT_ARGV_FAILED": "請輸入正確的參數！",
            "SCRIPT_RUN": "執行雲端命令: {}",
            "SCRIPT_RUN_SUCCESS": "運行成功",
            "SCRIPT_RUN_SUCCESS_LOG": "執行{}成功: {}",
            "SEARCH": "搜索",
            "SEARCH_CONFIG": "搜索配置",
            "SEARCH_CUSTOM": "搜索字段",
            "SEARCH_FLINK": "搜索友鏈",
            "SEARCH_IMAGE": "搜索圖片",
            "SEARCH_ITEM": "搜索項",
            "SEARCH_PAGE": "搜索頁面",
            "SEARCH_POST": "搜索文章",
            "SEARCH_SCRIPT": "搜索命令",
            "SEARCH_SETTINGS": "搜索設置",
            "SEARCH_TALK": "搜索說說",
            "SETTINGS": "設置",
            "SETTINGS_LABEL": "修改配置",
            "SET_ABBRLINK": "短鏈接設置",
            "SET_ABBRLINK_1": "短鏈接算法",
            "SET_ABBRLINK_2": "短鏈接進制",
            "SET_API": "API配置",
            "SET_API_1": "API密鑰",
            "SET_API_1_PH": "留空將保持不變",
            "SET_API_2": "啟用友鏈申請API",
            "SET_API_3": "使用 reCaptcha 驗證友鏈申請",
            "SET_API_4": "reCaptcha 密鑰",
            "SET_API_4_PH": "reCaptchaV3 服務器端 Token",
            "SET_BLOG": "博客配置",
            "SET_BLOG_1": "服務商",
            "SET_BLOG_2": "使用配置",
            "SET_CDN": "CDN 配置",
            "SET_CDN_1": "CDN 提供商",
            "SET_CUSTOM": "自定義配置",
            "SET_CUSTOM_1": "站點名稱",
            "SET_CUSTOM_1_PH": "默認為 Hexo管理面板",
            "SET_CUSTOM_2": "站點連接符",
            "SET_CUSTOM_2_PH": "默認為“ - ”",
            "SET_CUSTOM_3": "默認為 images 下的 qexo.png",
            "SET_CUSTOM_4": "站點 ICON",
            "SET_CUSTOM_4_PH": "默認為 images 下的 icon.png",
            "SET_CUSTOM_5": "暗色 LOGO",
            "SET_CUSTOM_5_PH": "默認為 images 下的 qexo-dark.png",
            "SET_EXCERPT": "摘要配置",
            "SET_EXCERPT_1": "截取方法",
            "SET_EXCERPT_2": "自動截取",
            "SET_EXCERPT_3": "保存字段",
            "SET_EXCERPT_3_PH": "一般為 excerpt",
            "SET_IMAGE": "圖床配置",
            "SET_IMAGE_1": "圖床類型",
            "SET_NOTIFY": "消息配置",
            "SET_NOTIFY_1": "服務商",
            "SET_SECURE": "安全配置",
            "SET_SECURE_1": "登錄頁 reCaptchaV3 用戶端密鑰",
            "SET_SECURE_1_PH": "留空即關閉該功能",
            "SET_SECURE_2": "登錄頁 reCaptchaV3 服務器端密鑰",
            "SET_SECURE_2_PH": "留空即關閉該功能",
            "SET_SECURE_3": "登錄頁 reCaptchaV2 用戶端密鑰",
            "SET_SECURE_3_PH": "留空即關閉該功能",
            "SET_SECURE_4": "登錄頁 reCaptchaV2 服務器端密鑰",
            "SET_SECURE_4_PH": "留空即關閉該功能",
            "SET_STATISTICS": "統計配置",
            "SET_STATISTICS_1": "啟用統計API",
            "SET_STATISTICS_2": "統計安全域名",
            "SET_STATISTICS_2_PH": "輸入域名包含的關鍵字, 英文半角逗號間隔",
            "SET_USER": "用戶配置",
            "SET_USER_1": "原密碼",
            "SET_USER_1_PH": "請輸入原密碼",
            "SET_USER_2": "新用戶名",
            "SET_USER_2_PH": "請輸入新用戶名",
            "SET_USER_3": "新密碼",
            "SET_USER_3_PH": "請輸入新密碼",
            "SET_USER_4": "確認密碼",
            "SET_USER_4_PH": "再次輸入以確認密碼",
            "SET_WEBHOOK": "一鍵設置WEBHOOK",
            "SIDEBAR_COLOR": "側邊欄顏色",
            "SIDEBAR_EDIT_1": "冒號前的內容",
            "SIDEBAR_EDIT_2": "描述標題",
            "SIDEBAR_EDIT_3": "使用的圖標",
            "SIDEBAR_TYPE": "側欄類型",
            "SIDEBAR_TYPE_LABEL": "在以下兩種樣式中選擇",
            "SIDEBAR_TYPE_TIP": "你只能在桌面端修改樣式",
            "SIZE": "大小",
            "SKIP": "跳過",
            "START": "開始",
            "START_COPY": "刪除完成, 正在拷貝文件...",
            "START_DEL": "開始刪除文件...",
            "START_EXTRACT_UPDATE": "下載更新完成, 開始解壓",
            "START_LOCAL_UPDATE": "開始更新, 使用本地方案, 準備臨時目錄",
            "START_VERCEL_UPDATE": "開始更新, 使用Vercel方案",
            "STATUS": "狀態",
            "STILL_IMPORT": "仍然繼續",
            "SUBMIT": "提交",
            "SUPPORT": "支持",
            "SYSTEM_ERROR": "程序遇到了錯誤！",
            "TAGS": "標籤",
            "TAG_EXITS": "標籤已存在!",
            "TALK": "說說",
            "TALKS_LIST": "說說列表",
            "TALK_ARGV_LABEL": "說說參數",
            "TALK_LABEL": "全部說說",
            "TEST": "測試",
            "TEST_MESSAGE": "如果你收到了這則消息, 那麼代表您的消息配置成功了",
            "THANK_LABEL": "感謝您的Star!",
            "TIME": "時間",
            "TIPS": "提示",
            "UNKNOWN_SIDEBAR": "未知側邊欄",
            "UNTITLED": "未命名",
            "UPDATE": "更新",
            "UPDATED_AT": "更新於",
            "UPDATED_AT_PH": "更新時間",
            "UPDATE_CHANNEL": "更新通道",
            "UPDATE_CONFIG": "配置更新",
            "UPDATE_CONTENT": "檢測到更新: {}<br>{}<p>可前往 <object><a href=\"/settings.html\">設置</a></object> 在線更新</p>",
            "UPDATE_LABEL": "程序更新",
            "UPDATE_LIB": "開始更新庫...",
            "UPDATE_NO_CHANNEL": "無此更新渠道",
            "UPDATE_POST_INDEX": "更新文章詳情索引",
            "UPDATE_QUEUING": "更新失敗: 當前有部署正在進行",
            "UPDATE_SUCCESS": "更新成功",
            "UPDATE_SUCCESS_DISPLAY": "更新成功，請等待自動部署!",
            "UPDATING": "正在更新中...",
            "UPLOAD": "上傳",
            "UPLOAD_FAILED": "上傳失敗！",
            "UPLOAD_SUCCESS": "上傳成功！",
            "UPLOAD_TIP": "上傳圖片",
            "USERNAME": "用戶名",
            "USER_IS_NOT_STAFF": "子用戶{}嘗試訪問{}被拒絕",
            "USER_IS_NOT_STAFF_DEL": "子用戶{}嘗試刪除{}被拒絕",
            "USER_IS_NOT_STAFF_MODIFY": "子用戶{}嘗試修改{}被拒絕",
            "USER_IS_NOT_STAFF_RENAME": "子用戶{}嘗試重命名{}被拒絕",
            "VALUE": "字段",
            "VALUE_NAME": "字段名",
            "VERIFY_FAILED": "校驗失敗",
            "WARN": "警告",
            "WARN_RESET": "確定要重置自定義配置嗎？該操作不可回退",
            "WARN_WEBHOOK": "確定要自動創建Webhook事件嗎？這會清除您原倉庫的所有Webhook事件",
            "WELCOME": "歡迎",
            "WIKI_LABEL": "查看文檔"
        }
    }
