#pragma once

%FWD_EXPORTS%

#define WIN32_LEAN_AND_MEAN
#include <windows.h>


#ifdef %PROJ_NAME%_EXPORTS
#define %PROJ_NAME%_API __declspec(dllexport)
#else
#define %PROJ_NAME%_API __declspec(dllimport)
#endif

extern "C" {
	%FUNCTIONS_HEADER%
}