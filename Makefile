run:
	python main.py

wsl-cleanup:
	rm -rf /mnt/f/Users/derek/Downloads/downloaded
	rm -rf ./top10postsdaily.mp4

windows-cleanup:
	Remove-Item D:\Downloads/downloaded
	Remove-Item ./top10postsdaily.mp4

mac-cleanup:
	rm -rf ~/Downloads/downloaded
	rm -rf ./top10postsdaily.mp4

encrypt-config:
	gpg --batch --output config.py.gpg --passphrase $(pass) --symmetric config.py

decrypt-config:
	gpg --batch --output config.py --decrypt config.py.gpg

