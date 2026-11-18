# Garden App

HyperionDev Git Workflows practical. Simple gardening tips using the supplied advice.

## Run (Python 3)

```powershell
git clone https://github.com/Khethelo01/garden-app.git
cd garden-app
python garden_advice.py
```

No third-party dependencies are needed.

## Verify

```powershell
python -m unittest -v
```

## Design

get_advice() combines two dictionary lookups. Unknown choices receive the original
fallback messages. Importing the module does not start the command-line program.

## Workflow

The supplied starter is preserved in the initial commit. Each improvement has its
own issue, local branch and merged pull request. This is individual coursework;
no independent reviewer approval is claimed.
