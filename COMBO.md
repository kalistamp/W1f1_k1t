## Clean up combos in Kali :

**Show number of lines in a txt file or combo list you are working with :**

``` wc -l example.txt ```

**Unzip a file in terminal :**

``` tar xvzf ‘filename you are unzipping’ ```

**Remove Lines Containing a Specific String:**

```sed -e '/.fr/d' -e '/.uk/d' -e '/.ru/d' -e '/.FR/d' -e '/.UK/d' -e '/.RU/d' /home/kali/Documents/dirty_combo.txt > clean_combo.txt```

Additions:

```-e '/.ne/d' -e '/.jp/d' -e '/.ocn/d' -e '/.ne/d' -e '/.ac/d' -e '/@alice/d' -e '/.it/d' -e '/.br/d'```

***

**Join multiple “combo .txt” files into one big one too work with :**


(After you ‘cd’ over the the folder(or directory) that all the .txt combos are in, you enter the following command)

``` cat *.txt > new.txt ```  (The ‘*’ is joining all .txt files ; and the ‘> new.txt’ is naming this new file you are creating)

**Remove the seperators in the combo list to have them all match… (Ex. of separators… “: or ;”)** 

``` sed ‘s/;/:/g’ example.txt > new_example.txt ``` (We are looking for ” ; ” in the list and changing them all to match ” : ” …. ” > ” saves to the name you choose for this new .txt file)

**Remove the extra spaces between lines in a text file:**

```tr -s '\n' < input.txt > output.txt```

**Sort combo list to easily see duplicates :**

``` cat example.txt | sort > new_example.txt ```

**Remove duplicates from a combo list :**

( command used, sorts list and removes duplicates at the same time… )

``` cat example.txt | sort | uniq > new_example.txt ```

**Mix combo list and save in a new file:**

```shuf combo_list.txt > mixed_combo_list.txt```

**Keep just the password or email and remove the other from list :**

``` cat example.txt | cut -d’ : ‘ -f2 > new_example.txt ``` ( after ” -d’ : ‘ “you must decide to delete before or after the semicolon …… ” -f2 ” deletes just the email leaving you with a list of passwords) – (” -f1 ” deletes all the passwords leaving you with emails)

**Search for specific email in a folder of txt combos using “zipgrep” :**

(After you ‘cd’ over the the folder(or directory) that all the .txt combos are in, you enter the following command)

``` zgrep -a “example @ mail.com\`” *.txt` ``` (Terminal will display which file the email is saved in)

**How to search for multiple emails at the same time :**

``` zgrep -e “example @ mail.com” -e “example2 @ mail.com” -e “example3 @ mail.com” *.txt ```

{ You can also split one giant combo list into multiple smaller txt files, choosing however many lines per split you want }


***

## Clean up Combos with Sublime:

Press F5 or click Edit -> Sort Lines

Click Edit -> Permute Lines -> Unique.

In my experience, CSV/JSON data file has duplicates very often (especially leaked files). And it’s worth remembering to run this function before working with any table.
