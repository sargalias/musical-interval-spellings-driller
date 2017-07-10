# Musical interval spellings trainer
A script that drills you on musical interval spellings. Using this program, you can learn interval spellings extremely quickly as you can do hundreds of repetitions in just a couple of minutes. I created this to use personally, without having plans to publish it online, and it was exactly what I needed.

Note that it doesn't cover any music theory, if you are not sure why some of the answers are the way they are please consult some music theory resources. One thing necessary to understand is about "enharmonics" (notes that have different names but sound the same". Loosely speaking, in music theory, a C# isn't the same as a Db. For example, a minor third above a B is D-flat. It is never C-sharp, even though it sounds the same and is at the same place on an instrument.

### To run:
Run the file **quickMusicSpeller.py** with python.

### Usage:
Type down one interval you want to be drilled on.  
This is case sensitive.  
Lowercase **m** stands for **minor**, uppercase **M** stands for **major**.  
Options are:
- **P1** - Unison  
- **m2** - Minor second  
- **M2** - Major second  
- **m3** - Minor third  
- **M3** - Major third  
- **P4** - Perfect fourth  
- **A4** - Augmented fourth  
- **D5** - Diminished fifth  
- **P5** - Perfect fifth  
- **m6** - Minor sixth  
- **M6** - Major sixth  
- **m7** - Minor seventh  
- **M7** - Major seventh  
- **P8** - Perfect octave  

### Answer formats:  
Not case-sensitive.  
The format is {letter}, followed by "#" or "b" for sharps and flats respectively.  
Two sharps "##" or flats "bb" can be used to denote double sharps and double flats.  
Examples:
- Question: P5 above D  
  Answer: **A**
- Question: P5 below Bb  
  Answer: **Eb**
- Question: M3 above B#  
  Answer: **D##**

### To quit:  
Type **quit**

### Notes:  
Currently the program can only test you on one interval at a time.