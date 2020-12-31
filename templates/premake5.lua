workspace "%PROJ_NAME%"
    configurations { "Debug", "Release" }


project "%PROJ_NAME%"
    kind "SharedLib"
    language "c++"
    targetdir "bin/%{cfg.buildcfg}"

files {"proxy.cpp","proxy.h","proj.def"}

filter "files:**"
    flags {"NoPCH"}

staticruntime "off"
