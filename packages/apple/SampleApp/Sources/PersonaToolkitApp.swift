import SwiftUI

@main
struct PersonaToolkitApp: App {
    @Environment(\.openWindow) var openWindow

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

        WindowGroup(id: "api-viewer") {
            OpenAPIViewerWindow()
        }
    }
}
