# Kopiernudel
Simple tool to regularly check a file or directory for changes and make a backup with appended timestamp if any changes were detected.
## Dependencies
- pyYaml
## Usage
The program requires a `config.yml` file located in its working directory. This file has to contain these parameters:

| Parameter | Explanation                                                     |
|-----------|-----------------------------------------------------------------|
| src       | Source directory or file to monitor                             |
| dst       | Destination directory for backups                               |
| interval  | The interval in seconds in which the src is checked for changes |

After creating this file you can simply run the program using
> python main.py