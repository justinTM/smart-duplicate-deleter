# smart-duplicate-deleter

Compares local duplicate music tracks to a set of rules and automatically deletes the "undesired" track.

## Code workflow
1. Gather list of music files from a local root path  
  a. Use <filename>.endswith(<extension>) to find .mp3, .aac, .m4a, .m4p, and .wav files.
2. Get file metadata for each file (ie. title, bpm, etc.)  
  a. Use [Mutagen](https://mutagen.readthedocs.io) package to get tags like title, bpm, and date.  
3. Find duplicate files based on metadata string matching confidence interval  
  a. Compare the string titles of two files, and determine (with a confidence rating) if they are duplicates
4. Apply metadata rules to determine which file(s) to delete  
  a. Prefer higher bitrate over lower bitrate  
  b. Prefer existing Traktor analysis over no Traktor analysis  
  c. Prefer newer over older  
5. Delete files
