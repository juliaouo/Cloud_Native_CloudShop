# Cloud_Native_CloudShop

## Environment
* OS=Ubuntu 22.04
* python=3.8 or higher

## Installation
```bash
git clone https://github.com/juliaouo/Cloud_Native_CloudShop.git
```

## Usage
```
cd Cloud_Native_CloudShop
```
interactive mode
```
bash run.sh
```
or non-interactive mode
```
bash run.sh < input.txt
```

you can modify `config/database.py`
```
db_type: RepositoryType = RepositoryType.FILE
```
to 
```
db_type: RepositoryType = RepositoryType.MEMORY
```
to change repository mode (type MEMORY does not save/load any file)
