Pastebin Scanner

This tool can be used to scrape new pastes to pastebin.
This tool does not require access to the pastebin API.
By default this tool scans every fifty seconds and check
each keyword in keywords.txt against new pastes. If a match
is found, the raw paste data is saved to the directory the
program is stored in for manual review. 

This tool is my second real project and will be polished 
in the future. Future plans include automated proxy to avoid
temporary IP bans. This is currently an issue with the program.
Furture update will also include an email feature to send
alerts when specific keywords are matched. 

Keywords can be in the form of regular expression. By default,
keywords.txt contains three regex patterns. As one who is interested 
in security, these regex look for common identity and email 
identifiers. Use responsibly.

Don't be evil.
Use for good.