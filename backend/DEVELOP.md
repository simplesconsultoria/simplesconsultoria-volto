# Using the development buildout

Create a virtualenv in the package:

```shell
python3 -m 
```

Install requirements with pip:

```shell
pip install -r requirements.txt
```

Run buildout:

```shell
buildout
```

Start Plone in foreground:

```shell
./bin/instance fg
```


## Running tests

```shell
make test_all
```
