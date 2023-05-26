# LambdaからSendgrid経由でメール送信

## 前提条件

自分のSendgridアカウントでAPIキーを発行していること

## メールの送信方法

1. ローカル上で作業

- のコマンドプロンプトで実行

```bash
cd my_test_sendgrid
cd sendgrid_lamda
touch build.sh
chmod 755 build.sh
```
2. AWS Console上での作業

- Lambda関数を作成

- ローカル上で作成された　sendgrid_lambda/dist/lambda.zipをアップロード

- SENDGRID_API_KEYの環境変数にSendgridのアカウントで発行したAPIキーを入れる

- `from_email`,`to_emails`,`subject`,`html_content`の値を変更（to_emailsはメールを送りたいメールアドレスに設定）

- 関数を実行

# my_test_sendgrid
