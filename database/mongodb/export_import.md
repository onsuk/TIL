# mongoexport, mongoimport

MongoDB를 EC2에서 LightSail로 옮기면서 `mongoexport`와 `mongoimport` 명령어를 간략하게 써봤다.

이에 대한 간략한 정리.

- **mongoexport**
```bash
$ mongoexport -h <hostname> --port <port> -u <user> -p <password> -d <database> -c <collection> -o <filename.json>
```

- **mongoimport**
```bash
$ mongoimport -h <hostname> --port <port> -u <user> -p <password> -d <database> --file <filename.json>
```

`mongoimport`의 경우는 위와 같이 따로 collection을 지정해주지 않으면 `collection` 이름에 대해 자동으로 `filename`을 쓴다. (`-c` 옵션을 이용해 `collection`을 지정할 수도 있음.)