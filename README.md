# backup-direct-messages
An easy way to backup all of your Instagram direct messages in an Instagram direct thread.
This is partly the work of https://github.com/ahmdrz. 
I've cloned his repo, modified it to fullfill my needs and then committed to my github. 
Please check-out the original repo: https://github.com/instautils/backup-direct-messages

### Backup everything in DM and generate clean CSV files with username, full name and proper date time.

This program will save all of your messages in `output/thread_name/results.csv` directory and download all of thread media in `output`.

```bash
  python automator.py -u <username> -p <password>
```

results.csv headers are :

1. UserID
2. Username
3. Full Name
4. Message
5. Date Time

