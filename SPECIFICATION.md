# FlashLearn システム仕様書

## 1. アプリケーション概要
* **名称:** FlashLearn (フラッシュ・ラーン)
* **目的:** ユーザーが自作の問題集を作成し、学習・暗記を行うためのWebアプリケーション。
* **ターゲット:** 試験勉強や知識の整理を行いたいユーザー。

## 2. 技術スタック
* **Frontend:** Vue.js 3 (Composition API), Vite, TailwindCSS
* **Backend:** Python 3.10+, FastAPI
* **Package Manager:** uv (推奨)
* **Linter/Formatter:** Ruff
* **Database:** SQLite (開発用), SQLAlchemy (ORM)
* **通信:** REST API (Axios)

## 3. 機能要件

### 管理機能
| 機能名 | 詳細 | 優先度 |
| :--- | :--- | :--- |
| **問題セット(デッキ)作成** | 複数の問題をまとめる「単語帳/章」の単位を作成する | ★必須 |
| **問題の追加** | 問題文、回答、解説を登録する | ★必須 |
| **問題の一覧・編集** | 登録した問題を確認し、内容を修正する | ★必須 |
| **問題の削除** | 不要な問題を削除する | ★必須 |

### 学習機能
| 機能名 | 詳細 | 優先度 |
| :--- | :--- | :--- |
| **出題モード（順次）** | デッキ内の問題を順番に表示する | ★必須 |
| **正誤判定・解説表示** | 「答えを見る」ボタンで回答と解説を表示。「正解/不正解」を自己記録 | ★必須 |
| **ランダム出題** | 出題順序をシャッフルする | ☆推奨 |

### 拡張機能（Future）
| 機能名 | 詳細 | 優先度 |
| :--- | :--- | :--- |
| **Markdown対応** | 問題文や解説で太字や数式を使えるようにする | ☆推奨 |
| **苦手重点モード** | 過去に「不正解」だった問題だけを抽出して出題する | ☆推奨 |

## 4. データモデル (Schema)

### Decks (問題集)
* `id`: PK
* `title`: String (問題集のタイトル)
* `created_at`: Datetime

### Cards (問題)
* `id`: PK
* `deck_id`: FK (Decks.id)
* `question`: Text (問題文)
* `answer`: Text (正解)
* `explanation`: Text (解説)
* `status`: Enum (未学習 / 覚えた / 苦手)

## 5. ディレクトリ構造想定
```text
project-root/
├── SPECIFICATION.md
├── README.md
├── .gitignore
├── backend/
│   ├── pyproject.toml     # uv管理用設定 & ruff設定
│   ├── .python-version    # Pythonバージョン指定
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       ├── decks.py
│       └── cards.py
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.js
        ├── App.vue
        ├── api/
        ├── components/
        ├── views/
        └── router/