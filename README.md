# dllproxygen

Parses a dll, extracts the exoports and generates a vs2019 project
containing a proxied dll. 

```
main.py --functions examplefunction target.dll dest_projectfolder
```

will generate a visual studio 2019 project in dest_projectfolder
with a dll that proxies all exported functions to target.dll while
intercepting the function examplefunction.

## Notes

The script does not know about return types or arguments functions. 
You have to adjust this in ```proxy.cpp```. The default function
decleration template is ```int examplefunctions(){return 0;}```
