import watch

try:
    watch.main()
except:
    import traceback
    import requests

    webhook_url = "https://discord.com/api/webhooks/....."
    content = {
        "username": "エラー報告",
        "content": traceback.format_exc()[:2000]
    }
    # Discord に配信
    requests.post(webhook_url, content)
