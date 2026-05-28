#if os(macOS)
import AppKit
import SwiftUI
import WebKit

struct WebViewRepresentable: NSViewRepresentable {
    let htmlString: String
    let baseURL: URL?

    init(htmlString: String, baseURL: URL? = nil) {
        self.htmlString = htmlString
        self.baseURL = baseURL
    }

    func makeCoordinator() -> Coordinator {
        Coordinator()
    }

    func makeNSView(context: Context) -> WKWebView {
        let webView = WKWebView()
        webView.navigationDelegate = context.coordinator
        webView.loadHTMLString(htmlString, baseURL: baseURL)
        context.coordinator.lastHTML = htmlString
        context.coordinator.lastBaseURL = baseURL
        return webView
    }

    func updateNSView(_ nsView: WKWebView, context: Context) {
        guard context.coordinator.lastHTML != htmlString
              || context.coordinator.lastBaseURL != baseURL else { return }
        nsView.loadHTMLString(htmlString, baseURL: baseURL)
        context.coordinator.lastHTML = htmlString
        context.coordinator.lastBaseURL = baseURL
    }
}

extension WebViewRepresentable {
    final class Coordinator: NSObject, WKNavigationDelegate {
        var lastHTML: String?
        var lastBaseURL: URL?

        // Route user-clicked external links to the default browser; let the
        // embedded page handle same-origin anchors (Swagger UI uses them to
        // jump between operations).
        func webView(
            _ webView: WKWebView,
            decidePolicyFor navigationAction: WKNavigationAction,
            decisionHandler: @escaping (WKNavigationActionPolicy) -> Void
        ) {
            if navigationAction.navigationType == .linkActivated,
               let url = navigationAction.request.url,
               url.host != webView.url?.host {
                NSWorkspace.shared.open(url)
                decisionHandler(.cancel)
                return
            }
            decisionHandler(.allow)
        }
    }
}
#endif
