import SwiftUI

@main
struct PersonaToolkitApp: App {
    #if os(macOS)
    @Environment(\.openWindow) var openWindow
    #endif

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        #if os(macOS)
        .windowResizability(.contentSize)
        .commands {
            CommandMenu("View") {
                Button("Open API Documentation") {
                    openWindow(id: "api-viewer")
                }
                .keyboardShortcut("d", modifiers: [.command, .option])
            }
        }
        #endif

        #if os(macOS)
        WindowGroup(id: "api-viewer") {
            OpenAPIViewerWindow()
        }
        #endif
    }
}
