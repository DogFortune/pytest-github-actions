# pytest-github-actions
LocalStackを使ってAWSサービスを使ったPyTestを動かすサンプルリポジトリです。  
ぜひ参考にしてください。

## 導入しているワークフロー
- mainブランチへのPushまたはmainブランチへのPR作成時（Draft含む）
    - mainブランチへの直接Pushはブランチ保護ルールで防止するのをおすすめ
- `pipenv`による環境構築
- `LocalStack`をDocker composeで起動
    - AWS S3のローカル環境を再現
- `PyTest`の実行
- テスト結果をレポートとして表示