# 開発ワークフロー

## 1. 役割分担（Phase 1）
* **Backend:** Aさん (Python / FastAPI / uv / SQLAlchemy)
* **Frontend:** Bさん (Vue.js / Vite / TailwindCSS)

## 2. 基本サイクル
このプロジェクトでは **GitHub Flow** を採用します。
原則として `main` ブランチへの直接 Push は禁止です（初期設定時を除く）。

1. **Issue 作成:** やることを明確にする（Assigneeを自分にする）。
2. **Branch 作成:** `main` から作業用ブランチを切る。
   * 命名: `feature/機能名` または `fix/バグ内容`
   * 例: `feature/add-deck-api`
3. **開発 & Commit:**
   * バックエンドは `uv run ruff check . --fix` で整形してからコミットする。
4. **Pull Request (PR):**
   * `main` に対して PR を作成。
   * フロントエンドの変更はスクリーンショットを貼る。
5. **Merge:** お互いに確認してマージ。

## 3. タスクリスト（Issue候補）

### Phase 1: 基盤 & 単語帳機能
- [ ] **Infra:** DB接続設定 (backend/database.py) & モデル定義 (backend/models.py)
- [ ] **API:** デッキ作成・一覧取得 (POST/GET /decks)
- [ ] **API:** カード追加・一覧取得 (POST/GET /decks/{id}/cards)
- [ ] **UI:** 基本レイアウト & ルーティング設定
- [ ] **UI:** デッキ一覧・作成画面
- [ ] **UI:** カード編集画面

### Phase 2: 学習機能
- [ ] **API:** 出題用データ取得API
- [ ] **UI:** 学習(クイズ)画面の実装