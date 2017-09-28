# Syncer 

## phillyai의 게임파일 동기화를 위해 만든 Repository 

백그라운드에서 돌아가면서 file의 해쉬값을 가져와서 변경됐는지를 체크한다. 

- 백그라운드에서 돌아간다.
- file의 hash를 비교한다. 
- hash가 같으나 name이 다르면 동기화 시킨다. 
- hash값이 다르면 동기화 시킨다.