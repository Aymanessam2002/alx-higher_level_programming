# Alx School - 0x0B-python-input_output

Reading and writing to files. Reading and writing JSON objects, hacking virtual memory

## New commands / functions used:

- `import json`
- `with open(<filename>, 'w' or 'a' or 'r' or 'b', encoding="utf-8") as file:` -- 'w' for write, 'a' for append, 'r' for read, and 'b' for bytemode. It is good practice to use with open(): because it will be properly closed after reading, even if will raises an exception.
- `file.read(size)` -- Reads the whole file if <size> is ommitted. Otherwise reads <size> bytes from the file.
- `file.readline()` -- Reads a single line up to the new line
- `file.readlines()` -- Read all the lines including newline characters
- `file.seek(offset, from_what)` -- changes the position of the object
- `file.tell()` -- Returns an integer witht he offset
- `file.close()` -- closes a file descriptor
- `json.dump()` -- Puts a python object into a json structure.
- `json.dumps()` -- Serializes the object into a text file.
- `json.load(file_descriptor)` -- loads a json object if file_descriptor has been opened for reading.

## Helpful Links

- [PyDocs: Reading and Writing Files](https://docs.python.org/3.4/tutorial/inputoutput.html#reading-and-writing-files)
- [PyDocs: Predefined Cleanup Actions](https://docs.python.org/3.4/tutorial/errors.html#predefined-clean-up-actions)
- [Files in python](http://www.diveintopython3.net/files.html)
- [json encoder and decoder](https://docs.python.org/3.4/library/json.html)
- [Learn To Program: Youtube](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring stuff with Python](https://automatetheboringstuff.com/)
- [The Proc Filesystem](https://www.kernel.org/doc/Documentation/filesystems/proc.txt)
