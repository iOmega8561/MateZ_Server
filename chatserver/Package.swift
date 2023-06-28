// swift-tools-version: 5.8
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "chatserver",
    products: [
        .executable(name: "chatserver", targets: ["chatserver"])
    ],
    dependencies: [
        .package(url: "https://github.com/vapor/vapor.git", from: "4.0.0")
    ],
    targets: [
        .executableTarget(
            name: "chatserver",
            dependencies: [
                .product(name: "Vapor", package: "vapor")
            ]),
    ]
)
