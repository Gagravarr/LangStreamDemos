# Setting up Mini-LangStream (LangStream + MiniKube) on Azure

To help you follow https://docs.langstream.ai/installation/get-started-minikube
on a fresh Azure VM, running Ubuntu 22.04 LTS.

Setup Azure VM with loads of memory (ideally at least 32gb)

```
apt-get install curl
apt-get install apt-transport-https
apt-get install docker.io
apt-get install build-essential
apt-get install jq zip unzip
apt-get install openjdk-17-jdk openjdk-17-jre
apt-get install python3-dev python3-numpy python3-pandas
```

Download binaries from their sites, place on `$PATH`:
 * minikube
 * kubectl
 * helm

```
minikube config set driver docker
minikube config set memory 24576
minikube config set cpus 6

helm repo add langstream https://langstream.ai/charts
```

Run the LangStream CLI installer
 * `curl -Ls "https://raw.githubusercontent.com/LangStream/langstream/main/bin/get-cli.sh" | bash`
 * Test with `langstream -h`

Run the Mini-LangStream installer
 * `curl -Ls "https://raw.githubusercontent.com/LangStream/langstream/main/mini-langstream/get-mini-langstream.sh" | bash`
 * Test with `mini-langstream -h`

Start Mini-LangStream
 * `mini-langstream start`
