# artemis2hashcat

## Description
Python3 implementation for converting Artemis PBKDF2WithHmacSHA1 hashes to hashcat format

## Usage
The default configuration for Apache Artemis is to use the [DefaultSensitiveStringCodec](https://github.com/apache/activemq-artemis/blob/main/artemis-commons/src/main/java/org/apache/activemq/artemis/utils/DefaultSensitiveStringCodec.java#L235) in order to store user passwords as PBKDF2WithHmacSHA1 hashes in the "artemis-users.properties" file.

The hashes stored in "artemis-users.properties" usually have the following form:
```
username = ENC(ITERATIONS:SALT:HASH)
```

[This python3 code](https://github.com/mbadanoiu/artemis2hashcat/blob/main/artemis2hashcat.py) converts the Artemis hash into a hashcat compatible format using one of the following commands:
- With "ENC(...)":
```
python3 artemis2hashcat.py 'ENC(1024:8D873D1EDFB8ABACBC1A8229AC6A691B2856427B385167AC5DA636A8B0D0CF7C:50DE2FF97B69C8B8D127356F8F1090730F8F805DAA288E804E199788394EF0C9363671038857CB7F83ACE9022ACE2119792B9FCFB72CA68D026A5458B2D4C7CF)'
```
OR
- Content without "ENC(...)":
```
python3 artemis2hashcat.py '1024:8D873D1EDFB8ABACBC1A8229AC6A691B2856427B385167AC5DA636A8B0D0CF7C:50DE2FF97B69C8B8D127356F8F1090730F8F805DAA288E804E199788394EF0C9363671038857CB7F83ACE9022ACE2119792B9FCFB72CA68D026A5458B2D4C7CF'
```
**Note:** The above hash corresponds to the plaintext password "7KBeh41j".

The result of the above commands should have the following form:
```
sha1:1024:jYc9Ht+4q6y8GoIprGppGyhWQns4UWesXaY2qLDQz3w=:UN4v+XtpyLjRJzVvjxCQcw+PgF2qKI6AThmXiDlO8Mk2NnEDiFfLf4Os6QIqziEZeSufz7cspo0CalRYstTHzw==
```

By writing the output to a file (e.g. test.hashcat) we can use the following hashcat command, with hash-mode [12000](https://hashcat.net/wiki/doku.php?id=example_hashes), in order to attempt to crack the hash:
```
hashcat -m 12000 -a 0 test.hashcat test.lst
```
