{
    "targets": [
        {
            "target_name": "cryptonote",
            "sources": [
                "src/main.cc",
                "src/cryptonote_core/cryptonote_format_utils.cpp",
                "src/crypto/tree-hash.c",
                "src/crypto/crypto.cpp",
                "src/crypto/crypto-ops.c",
                "src/crypto/crypto-ops-data.c",
                "src/crypto/hash.c",
                "src/crypto/keccak.c",
                "src/common/base58.cpp",
            ],
            "include_dirs": [
                "src",
                "src/contrib/epee/include",
                "<!(node -e \"require('nan')\")",
            ],
            "link_settings": {
                "libraries": [
                    "-lboost_system",
                    "-lboost_date_time",
                ]
            },
            "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ],
            "cflags_cc": [
                  "-std=c++0x",
                  "-fexceptions",
                  "-frtti",
            ],
            "xcode_settings": {
              "OTHER_CFLAGS": ["-fexceptions", "-frtti"]
            },
            "conditions": [
                ['OS=="openbsd" or OS=="freebsd"', {
                    "cflags": [
                        "-Wunused-function",
                        "-Wunused-variable",
                        "-Wmissing-braces",
                    ],
                    'include_dirs': [
                        '/usr/local/include'],
                    'libraries': [
                        '-L/usr/local/lib']
                }],
            ]
        }
    ]
}
