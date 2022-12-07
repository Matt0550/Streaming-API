# Streaming-API

APIs that allow you to receive the updated URL of the most popular streaming sites. (example. euroStreaming)

## API Reference

#### Get url from streaming website
API URL: Maintance
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
https://host/eurostreaming
```
You will now be automatically redirected to the website

## Legacy version
A old version of the API is available at the following address: https://github.com/Matt0550/streaming-api-legacy
The old version is no longer maintained and no longer works.
