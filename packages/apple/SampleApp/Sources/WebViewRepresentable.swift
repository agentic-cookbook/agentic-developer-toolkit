#if os(macOS)
import SwiftUI
import WebKit

struct WebViewRepresentable: NSViewRepresentable {
    let htmlString: String
    let baseURL: URL?

    init(htmlString: String, baseURL: URL? = nil) {
        self.htmlString = htmlString
        self.baseURL = baseURL
    }

    func makeNSView(context: Context) -> WKWebView {
        let webView = WKWebView()
        webView.loadHTMLString(htmlString, baseURL: baseURL)
        return webView
    }

    func updateNSView(_ nsView: WKWebView, context: Context) {}
}
#endif
