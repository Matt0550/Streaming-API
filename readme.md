# Streaming-API

APIs that allow you to receive the updated URL of the most popular streaming sites. (example. euroStreaming)

## API Reference

#### Get url from streaming website
API URL: https://streaming.api.matt05.it
```http
GET /v1/${website}
```

| Parameter | Description   | Available sites                  |
| :-------- | :------------ | :------------------------------- |
| `website` | **Required**. | `View the list below `          |

#### Available sites
- `eurostreaming`
- `altadefinizione`
- `cb01`

#### Response
```json
{"message":"https://eurostreaming.town","status":"success"}
```
### Automatic redirect

```
https://streaming.api.matt05.it/eurostreaming
```
You will now be automatically redirected to the website

## Help or feedback
You can contact me on:

Discord: https://discord.gg/5WrVyQKWAr

Telegram: https://t.me/Non_Sono_matteo

Mail: mail@matt05.it

## Legacy version
A old version of the API is available at the following address: https://github.com/Matt0550/streaming-api-legacy

The old version is no longer maintained and no longer works.

## Support me

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/matt05)

[![buy-me-a-coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/Matt0550)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/sillittimatteo)