## Hey! - Your AI-powered Pair Programming Friend

<a href="https://www.producthunt.com/posts/hey-7fed5187-9b92-4ee8-9ce5-e08d5bc63d15?embed=true&utm_source=badge-featured&utm_medium=badge&utm_souce=badge-hey&#0045;7fed5187&#0045;9b92&#0045;4ee8&#0045;9ce5&#0045;e08d5bc63d15" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=483008&theme=light" alt="Hey&#0033; - AI&#0045;Powered&#0032;Pair&#0032;Programming&#0032;Friend&#0033;&#0032;✨ | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a> <a href="https://www.producthunt.com/posts/hey-7fed5187-9b92-4ee8-9ce5-e08d5bc63d15?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_souce=badge-hey&#0045;7fed5187&#0045;9b92&#0045;4ee8&#0045;9ce5&#0045;e08d5bc63d15" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=483008&theme=light&period=daily" alt="Hey&#0033; - AI&#0045;powered&#0032;pair&#0032;programming&#0032;friend | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

> :basecamp: - Watch this YouTube <a href="https://www.youtube.com/watch?v=fhO34PVa-38&list=LL&index=9">introduction video</a> about Hey!

> :writing_hand: - Read the <a href="https://blog.imsadra.me/introducing-hey-your-ai-powered-pair-programming-friend">"Introducing Hey! - Your AI-powered Pair Programming Friend"</a> article about the creation process, development phases, and a detailed overview of Hey.

Hey is a CLI-based AI assistant that is powered by the ChatGPT AI model versions supported by [MindsDB](https://mindsdb.com/). This project is designed for [Hashnode X MindsDB](https://hashnode.com/hackathons/mindsdb?source=hncounter-feed) hackathon.

You may need a MindsDB token to use Hey. You can generate one for your personal uses for free from [here](https://mdb.ai). You can set Hey to interact with any other LLM service URL though. You're not limited to mdb.ai.

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

> :warning:: Hey is POSIX-friendly. It might not work properly on Windows machines at the moment.

</details>

<details>
  <summary><h4>2. Set the <code>HEY_TOKEN</code></h4></summary>

Once you got the package installed on your system, it's time to add the token that you just copied from [mdb.ai](https://mdb.ai) into hey, use `hey token [HEY_TOKEN]` to add your token.

</details>

### Usage
There are different commands and sub-commands implemented once you install `hey`. Check them out via the `--help` flag.

```sh
hey --help
```

```
                                                                                                 
 Usage: hey [OPTIONS] COMMAND [ARGS]...                                                          
                                                                                                 
 Hey is a pair-programming friend that interacts with ChatGPT and responds back in a pretty      
 style. ✨                                                                                       
                                                                                                 
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────╮
│ --no-style,--ns                 Don't style the output.                                       │
│ --version             -V        Show the current version of Hey.                              │
│ --install-completion            Install completion for the current shell.                     │
│ --show-completion               Show completion for the current shell, to copy it or          │
│                                 customize the installation.                                   │
│ --help                          Show this message and exit.                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────╮
│ ask      Ask Hey directly in-command.                                                         │
│ config   Configuration management.                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────╯
```

- If you want to use `Hey` in a fast and quick way, use the `ask` command.

  ```sh
  hey ask "explain the duality term in quantum physics."
  ```

- If your question needs more explanations with code snippets, then just `hey`.

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

    // thinking animation symbol
    // check out full list: python -m rich.spinner
    "loading_spinner": "dots",

    // never style the output (in case you need to copy the result)
    "never_style": false
}
```

### Tech Stack
- Infrastructures & Hosting
    - [MindsDB](https://mdb.ai)

### License
Hey is being licensed under the [MIT License](https://github.com/lnxpy/hey/blob/main/LICENSE).

### Special Thanks to
[MindsDB](https://mindsdb.com) X [Hashnode](https://hashnode.com) for hosting this great hackathon.

<img src="media/badge-dark.svg#gh-dark-mode-only" width=350 height=90>
<img src="media/badge-light.svg#gh-light-mode-only" width=350 height=90>
