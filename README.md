# dllproxygen

Parses a dll, extracts the exoports and generates a vs2019 project
containing a proxied dll. 

```
main.py --functions examplefunction1,examplefunction2 --proxytarget originaldll target.dll dest_projectfolder 
```

will generate a visual studio 2019 project in dest_projectfolder
with a dll that proxies all exported functions to originaldll.dll while
intercepting the functions examplefunction1 and examplefunction2

## Notes

You need to have premake5.exe in your PATH

The script does not know about return types or arguments of functions. 
You have to adjust this yourself in the generated ```proxy.cpp```.
The default function decleration template is ```int examplefunctions(){return 0;}```
