find_package(easyloggingpp REQUIRED)
find_package(GTest REQUIRED)

include(GoogleTest)

add_executable(ripe-unit-tests main.cc)

target_compile_definitions(ripe-unit-tests PUBLIC
    ELPP_FEATURE_ALL
    ELPP_DEFAULT_LOG_FILE="logs/ripe-unit-test.log"
    ELPP_DEFAULT_LOGGING_FLAGS=4096
)

target_link_libraries(ripe-unit-tests PRIVATE ripe gtest::gtest easyloggingpp::easyloggingpp)

gtest_discover_tests(ripe-unit-tests)