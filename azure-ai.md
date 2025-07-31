### Azure code auth approaches
```
Recommended: DefaultAzureCredential from Azure Identity client libraries.
  Azure CLI: Authenticates using the account logged in via az login.
  Azure Developer CLI: Authenticates using the account logged in via azd auth login.
  Visual Studio/VS Code: Authenticates using credentials from the IDE.
Old way: key authentication. Store Azure authentication key in .env file
```
