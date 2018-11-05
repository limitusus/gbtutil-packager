gbtutil-packager
================

## Usage

Download GbtUtility command line utility from [GIGABYTE Support](https://www.gigabyte.com/Support/Utility?kw=GBT&p=1) named `GbtUtility command line utility`.


```console
docker build .
docker run -it $(docker images -q | head -1)
```

Voila!

```console
docker cp $(docker ps -aq | head -1):/rpmbuild/SRPMS/GbtUtility-2.0.12-0.el7.src.rpm /tmp/rpm/
docker cp $(docker ps -aq | head -1):/rpmbuild/RPMS/x86_64/GbtUtility-2.0.12-0.el7.x86_64.rpm /tmp/rpm/
```
