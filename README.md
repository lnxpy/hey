## Hey! - Your AI-powered Pair Programming Friend ![download badge](.pypi_chart/badge.svg)

<a href="https://www.producthunt.com/posts/hey-7fed5187-9b92-4ee8-9ce5-e08d5bc63d15?embed=true&utm_source=badge-featured&utm_medium=badge&utm_souce=badge-hey&#0045;7fed5187&#0045;9b92&#0045;4ee8&#0045;9ce5&#0045;e08d5bc63d15" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=483008&theme=light" alt="Hey&#0033; - AI&#0045;Powered&#0032;Pair&#0032;Programming&#0032;Friend&#0033;&#0032;✨ | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a> <a href="https://www.producthunt.com/posts/hey-7fed5187-9b92-4ee8-9ce5-e08d5bc63d15?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_souce=badge-hey&#0045;7fed5187&#0045;9b92&#0045;4ee8&#0045;9ce5&#0045;e08d5bc63d15" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=483008&theme=light&period=daily" alt="Hey&#0033; - AI&#0045;powered&#0032;pair&#0032;programming&#0032;friend | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

> :basecamp: - Watch this YouTube <a href="https://www.youtube.com/watch?v=fhO34PVa-38&list=LL&index=9">introduction video</a> about Hey!

> :writing_hand: - Read the <a href="https://blog.imsadra.me/introducing-hey-your-ai-powered-pair-programming-friend">"Introducing Hey! - Your AI-powered Pair Programming Friend"</a> article about the creation process, development phases, and a detailed overview of Hey.

Hey is a free CLI-based AI assistant that is powered by the LLMs. You can set which LLM service you want to connect Hey to.

> [!TIP]
> We recommend using the free tokens provided by MindsDB. You can generate one for your personal uses for free on [mdb.ai](https://mdb.ai). You can set Hey to interact with any other LLM service though. You're not limited to mdb.ai. It's a recommendation.

### Installation
Make sure you have `pip` and `python>=3.8` installed on your machine and follow the steps.

#### 1. Setup the package

###### Option A - Download from PyPI
```sh
pip install -U hey-mindsdb
```

###### Option B - Download from the repository
```sh
pip install git+http://github.com/lnxpy/hey.git
```

#### 2. Set the token
Once you got the package installed on your system, it's time to set the token into hey. Run the following command to set the token.

```sh
hey auth
```
</details>

### Usage
There are different commands and sub-commands implemented once you install `hey`. Check them out via the `--help` flag.

```sh
hey --help
```

#### TLDR;

- If you want to use `Hey` in a fast and quick way, use the `ask` command.

  ```sh
  hey ask "explain the duality term in quantum physics."
  ```

- If your question needs more explanations with code snippets maybe, then just `hey`.

  ```sh
  hey
  <OPENS EDITOR>
  ```

  > Keep in mind that when you run `hey` with no sub-commands, the default `$EDITOR` will be used. If this environment variable is not set, then `vim` on Unix-like systems and `notepad` on Windows machines will be used by default.

### Configuration
There is a command dedicated for more customizability. Check the following bullet-points.

- Create a base configuration file.

  ```sh
  hey config create
  ```

- View and edit the configuration file.

  ```sh
  hey config edit
  ```

Here is more information about each configuration parameter.

```json
{
    // llm service URL
    "service": "https://llm.mdb.ai",

    // model version
    "model": "gpt-3.5-turbo",

    // prompt
    "prompt": "Answer in a helpful way.",

    // themes used for the codeblocks
    "code_block_theme": "github-light",

    // how would you like `hey` to think?
    "loading_text": "Thinking..",

    // check out full list: python -m rich.spinner
    "loading_spinner": "dots",

    // never style the output (in case you need to copy the result)
    "never_style": false
}
```

### License
Hey is being licensed under the [MIT License](https://github.com/lnxpy/hey/blob/main/LICENSE).

### Shout-out to
Hey! was created for a hackathon partnering [MindsDB](https://mindsdb.com) X [Hashnode](https://hashnode.com).

<img src="media/badge-dark.svg#gh-dark-mode-only" width=350 height=90>
<img src="media/badge-light.svg#gh-light-mode-only" width=350 height=90>
