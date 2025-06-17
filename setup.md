---
title: Setup
---

# Run exercises on CERN LXPLUS or CERN SWAN

In order to obtain EOS space for the exercises, open the
[CERNBox website](https://cernbox.cern.ch/) and log in with your CERN credentials.
This will provide you with 1 TB of space in
`/eos/user/<USERNAME INITIAL>/<YOUR USERNAME>`, e.g. `/eos/user/c/clange`.

You can either use LXPLUS or SWAN to run the exercises.
You can switch between the two by following the instructions below.

## Using lxplus.cern.ch

Open a terminal/console, connect to `lxplus.cern.ch` and prepare your working area:

~~~
ssh -L localhost:8888:localhost:8888 <YOUR USERNAME>@lxplus.cern.ch
cd /eos/user/${USER:0:1}/${USER}
~~~
{: .language-bash}

Continue with [Cloning the repository](#cloning-the-repository).

## Using SWAN

In your browser, open the [SWAN website](https://swan.cern.ch/) and
log in with your CERN credentials.

When presented with the "Configure Environment" page, keep everything
unchanged, i.e. the
"Software stack" as _107_ (default in June 2025),
"Platform" _AlmaLinux 9 (gcc13)_
and click "Start my session".

Click on the "Open a terminal" button in the top right corner.

In order to be able to have access to your VOMS proxy, you will
have to log on to `lxplus.cern.ch` and run the following command:

~~~
cp -r ~/.globus /eos/user/${USER:0:1}/${USER}
~~~
{: .language-bash}

## Cloning the repository

~~~
git clone git@github.com:cms-jet/JMEDAS.git -b DASJune2025 --single-branch --depth=1
cd JMEDAS/notebooks/DAS/
~~~
{: .language-bash}

> ## Remember
> Once you clone the repository, using the `DASJune2025` branch, the exercise notebooks are located
> in `JMEDAS/notebooks/DAS/`
{: .callout}

Activate your grid certificate:

~~~
voms-proxy-init -voms cms -valid 192:00
~~~
{: .language-bash}

## Every-time setup for LXPLUS

When using LXPLUS, the following commands have to be executed
*everytime you log in into a new session*.
They load the environment and the packages needed for the exercises
and open a jupyter notebook:

~~~
source /cvmfs/sft.cern.ch/lcg/views/LCG_107/x86_64-el9-gcc13-opt/setup.sh
jupyter notebook --no-browser --port=8888 --ip 127.0.0.1
~~~
{: .language-bash}

If these two lines are running sucessfully, you should see something like this:

~~~
[I 22:17:24.498 NotebookApp] Writing notebook server cookie secret to /afs/cern.ch/user/c/clange/.local/share/jupyter/runtime/notebook_cookie_secret
[I 22:17:26.375 NotebookApp] Serving notebooks from local directory: /eos/home-c/clange/JMEDAS/notebooks/DAS
[I 22:17:26.376 NotebookApp] Jupyter Notebook 6.4.0 is running at:
[I 22:17:26.376 NotebookApp] http://127.0.0.1:8888/?token=b7de34fb074433b51831bdef0f0818f13279824ab33502cd
[I 22:17:26.376 NotebookApp]  or http://127.0.0.1:8888/?token=b7de34fb074433b51831bdef0f0818f13279824ab33502cd
[I 22:17:26.376 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 22:17:26.384 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///afs/cern.ch/user/c/clange/.local/share/jupyter/runtime/nbserver-521240-open.html
    Or copy and paste one of these URLs:
        http://127.0.0.1:8888/?token=b7de34fb074433b51831bdef0f0818f13279824ab33502cd
     or http://127.0.0.1:8888/?token=b7de34fb074433b51831bdef0f0818f13279824ab33502cd

~~~
{: .output}

Copy and paste one of the last two urls in your favorite browser and now you can continue with the lesson 1 (Episode 1).

> ## If you are using PUTTY
> Go to ssh tab on the left then type in source port (ex. 8888) with destination (ex. localhost:8888) and then hit "add" to add this to the list of ports
> If 8888 is occupied, use another port (ex. anything above 8000) instead
{: .callout}

## Every-time setup for SWAN

Open the SWAN projects page in the browser and click on
"CERNBox", then navigate to
`JMEDAS` --> `notebooks` --> `DAS`.

## Useful settings

If you like seeing your working directory in the command line,
you can do also this by adding a line to ~/.bashrc and activating
it with the 'source' command:

~~~
echo "PS1='\W\$ '" >> ~/.bashrc
source ~/.bashrc
~~~
{: .language-bash}

{% include links.md %}
