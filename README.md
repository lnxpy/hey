## Hey! - Your AI-powered Pair Programming Friend

> :warning: - You need OpenAI auth token to make Hey work.

> :basecamp: - Watch this YouTube <a href="https://www.youtube.com/watch?v=fhO34PVa-38&list=LL&index=9">introduction video</a> about Hey!

> :writing_hand: - Read the <a href="https://imsadra.me/introducing-hey-your-ai-powered-pair-programming-friend">"Introducing Hey! - Your AI-powered Pair Programming Friend"</a> article about the creation process, development phases, and a detailed overview of Hey.

> :package: - Check out <a href="https://pypi.org/project/hey-mindsdb/">Hey on PyPI</a>.

Hey is a CLI-based AI assistant that is powered by the ChatGPT AI model versions supported by [MindsDB](https://mindsdb.com/). This project is designed for [Hashnode X MindsDB](https://hashnode.com/hackathons/mindsdb?source=hncounter-feed) hackathon.

### Installation
Make sure you have `pip` and `python>=3.6` installed on your machine and follow the steps.

<details>
  <summary><h4>1. Setup the package</h4></summary>

##### Option A - Download from PyPI archive
```sh
pip install -U hey-mindsdb
```

##### Option B - Download from GitHub archive
```sh
pip install git+http://github.com/lnxpy/hey.git
```

> :warning:: Hey is POSIX-friendly. It might not work properly on the Windows machines at the moment.

</details>

<details>
  <summary><h4>2. Set the <code>MINDSDB_EMAIL_ADDRESS</code> environment variable</h4></summary>

Once you got the package installed on your system, it's time to add the `MINDSDB_EMAIL_ADDRESS` environment variable. Create an account on [mindsdb.com](https://mindsdb.com/), train your GPT model and replace your email with `<EMAIL>` in the following options.

##### > If you use the default bash shell
```sh
echo "export MINDSDB_EMAIL_ADDRESS=<EMAIL>" >> ~/.bashrc
```
##### > If you use ZSH
```sh
echo "export MINDSDB_EMAIL_ADDRESS=<EMAIL>" >> ~/.zshrc
```

> :bulb:: Read the article for more information about training your MindsDB model.

</details>

<details>
  <summary><h4>3. Set your MindsDB account password</h4></summary>

Now, it's time to set your account's password. Simply run `hey` with the `--auth` option and enter your MindsDB account password.

```sh
hey --auth
```

You're all set to go. :)

</details>

### Usage
Use `hey` followed by your question and it'll process the phrase and responses back the content in Markdown.

```
$ hey generate a power function in javascript
To generate a power function in JavaScript, you can use the built-in Math.pow()
method. Here's an example of how to create a power function using JavaScript:


 function powerFunction(base, exponent) {
   return Math.pow(base, exponent);
 }

 // Example usage:
 console.log(powerFunction(2, 3)); // Output: 8
 console.log(powerFunction(5, 2)); // Output: 25
```

```
$ hey tell me a programming joke
Why do programmers always mix up Christmas and Halloween?

Because Oct 31 == Dec 25!
```

```
$ hey add annotations to this function: $(cat file.py)
To add annotations to the given Python function, you can include comments and
docstrings to provide more information about the function's purpose and usage.
Here's an example:


 # Importing the required module from setuptools package
 from setuptools import setup

 # Function to setup MindsDB package
 def mindsdb_setup():
     """
     This function sets up the MindsDB package using the setup() function from
 setuptools.
     """
     # Calling the setup() function to configure the package
     setup()
```

### Tech Stack
- Tools
    - [Python](https://python.org)
- Infrastructures & Hosting
    - [MindsDB](https://mindsdb.com)
    - [PyPI](https://pypi.org)

### Package Stats
![stats](media/stats.svg)

### License
Hey is being licensed under the [MIT License](https://github.com/lnxpy/hey/blob/main/LICENSE).

### Special Thanks to
[MindsDB](https://mindsdb.com) X [Hashnode](https://hashnode.com) for hosting this great hackathon.

<img src="media/badge-dark.svg#gh-dark-mode-only" width=350 height=90>
<img src="media/badge-light.svg#gh-light-mode-only" width=350 height=90>
