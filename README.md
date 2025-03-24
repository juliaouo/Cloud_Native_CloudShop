# Cloud_Native_CloudShop

## Environment
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
sh run.sh
```
or non-interactive mode
```
sh run.sh < input.txt
```

you can modify `config/database.py`
```
db_type: RepositoryType = RepositoryType.FILE
```
to 
```
db_type: RepositoryType = RepositoryType.MEMORY
```
to change repository mode (type MEMORY dose not save/load any file)