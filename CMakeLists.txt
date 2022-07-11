cmake_minimum_required(VERSION 3.13.4)

project(SmartTemplateCryo)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ProstateCryo")
set(EXTENSION_CATEGORY "IGT")
set(EXTENSION_CONTRIBUTORS "Pedro Moreira (BWH)")
set(EXTENSION_DESCRIPTION "3D Slicer module for the Smart Template")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/ProstateCryo.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/ProstateCryo/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(CryoControl)
add_subdirectory(ManualPlanning)
add_subdirectory(ManualPlanning)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
