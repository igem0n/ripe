cmake_minimum_required(VERSION 3.30)

project(Ripe)

option(BUILD_EXCUTABLE "Build ripe executable" ON)

set (RIPE_VERSION "4.2.2")
set (RIPE_SOVERSION "4.2.2")

find_package(ZLIB REQUIRED)
find_package(cryptopp REQUIRED)
find_package(cryptopp-pem REQUIRED)

################################################ RIPE LIB #####################################

add_library(ripe lib/Ripe.cc)

target_sources(ripe PUBLIC FILE_SET HEADERS BASE_DIRS include FILES include/Ripe.h)

target_link_libraries(ripe
    cryptopp::cryptopp
    cryptopp-pem::cryptopp-pem
    ZLIB::ZLIB
)

install (TARGETS ripe FILE_SET HEADERS)

target_compile_definitions(ripe PUBLIC RIPE_VERSION="${RIPE_VERSION}")

if(BUILD_SHARED_LIBS)
    set_target_properties(ripe PROPERTIES
        VERSION ${RIPE_VERSION}
        SOVERSION ${RIPE_SOVERSION}
    )
endif()

if(WIN32 AND BUILD_SHARED_LIBS)
    target_compile_definitions(ripe PUBLIC RIPE_DLL)
    target_compile_definitions(ripe PRIVATE RIPE_EXPORTS)
endif()

################################################ RIPE ##############################################

if(BUILD_EXCUTABLE)
    add_executable (ripe-bin src/ripe.cc)
    target_link_libraries (ripe-bin PRIVATE ripe)

    set_target_properties (ripe-bin PROPERTIES
        OUTPUT_NAME "ripe"
        VERSION ${RIPE_VERSION}
        SOVERSION ${RIPE_SOVERSION}
    )

    install (TARGETS ripe-bin DESTINATION bin)
endif()

########################################## Unit Testing ###################################

include(CTest)
if (BUILD_TESTING)
    add_subdirectory(test)
endif()
