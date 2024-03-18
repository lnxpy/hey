## Hey! - Your AI-powered Pair Programming Friend (EvaDB Release)

> :warning: - You need OpenAI auth token to use Hey.

> :basecamp: - Watch this YouTube <a href="https://www.youtube.com/watch?v=fhO34PVa-38&list=LL&index=9">introduction video</a> about Hey!

Hey is a CLI-based AI assistant tool that is powered by OpenAI's ChatGPT LLM.

### Installation
Declare your OpenAI API token as an environment variable.

```sh
echo "export OPENAI_KEY=<token>" >> ~/.bashrc
```

If you use ZSH, run the following command instead.

```sh
echo "export OPENAI_KEY=<token>" >> ~/.zshrc
```

Make sure you have `pip`, `git`, and `python>=3.6` installed on your machine and run the following command.

```sh
$ pip install git+https://github.com/lnxpy/hey@evadb
```

### Usage
If it's your first time using `hey`, make sure to run the following command and initiating the GPT model for the further usages.

```sh
$ hey --init
```

Use `hey` followed by your question and it'll process the phrase and responses back the content in rich format.

```
$ hey tell me a programming joke
Why do programmers always mix up Christmas and Halloween?

Because Oct 31 == Dec 25!
```

### Requirements
- [EvaDB](https://evadb.readthedocs.io/en/stable/index.html)
- `rich`

### License
Hey is being licensed under the [MIT License](https://github.com/lnxpy/hey/blob/main/LICENSE).
