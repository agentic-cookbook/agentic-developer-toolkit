#if os(macOS)
import SwiftUI

struct OpenAPIViewerWindow: View {
    private let swaggerUIHTML: String

    init() {
        self.swaggerUIHTML = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>OpenAPI Viewer</title>
                <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5.32.6/swagger-ui.css"
                      integrity="sha384-9Q2fpS+xeS4ffJy6CagnwoUl+4ldAYhOs9pgZuEKxypVModhmZFzeMlvVsAjf7uT"
                      crossorigin="anonymous">
                <style>
                    html { box-sizing: border-box; overflow: -moz-scrollbars-vertical; overflow-y: scroll; }
                    *, *:before, *:after { box-sizing: inherit; }
                    body { margin: 0; padding: 0; }
                </style>
            </head>
            <body>
                <div id="swagger-ui"></div>
                <script src="https://unpkg.com/swagger-ui-dist@5.32.6/swagger-ui-bundle.js"
                        integrity="sha384-EYdOaiRwn44zNjrw+Tfs06qYz9BGQVo2f4/pLY5i7VorbjnZNhdplAbTBk8FXHUJ"
                        crossorigin="anonymous"></script>
                <script src="https://unpkg.com/swagger-ui-dist@5.32.6/swagger-ui-standalone-preset.js"
                        integrity="sha384-49fpFaVrAWI/qdgl9Vv5E/4NXxRUiJX5vGuLws1NUpTWGtEqzWEx8gHTw2UTehFK"
                        crossorigin="anonymous"></script>
                <script>
                    const HTTP_METHODS = ['get','post','put','patch','delete','head','options','trace']

                    function tagForPath(path) {
                        const segments = path.split('/').filter(s => s.length > 0)
                        if (segments.length === 0) return 'default'
                        if (segments[0] === 'api' && segments.length > 1) return segments[1]
                        return segments[0]
                    }

                    function regroupByPath(spec) {
                        const tagSet = new Set()
                        for (const [path, item] of Object.entries(spec.paths || {})) {
                            const tag = tagForPath(path)
                            tagSet.add(tag)
                            for (const method of HTTP_METHODS) {
                                if (item[method]) item[method].tags = [tag]
                            }
                        }
                        spec.tags = [...tagSet].sort().map(name => ({ name }))
                        return spec
                    }

                    function showError(message) {
                        const el = document.getElementById('swagger-ui')
                        el.replaceChildren()
                        const wrap = document.createElement('div')
                        wrap.style.cssText = 'padding:24px;font-family:-apple-system,sans-serif;color:#c00'
                        const h = document.createElement('h2')
                        h.textContent = 'Could not load OpenAPI spec'
                        const p = document.createElement('p')
                        p.textContent = message
                        wrap.appendChild(h)
                        wrap.appendChild(p)
                        el.appendChild(wrap)
                    }

                    window.onload = function() {
                        fetch("https://apidocs.agenticdeveloperstorage.com/openapi.json", {
                            signal: AbortSignal.timeout(10000)
                        })
                            .then(r => {
                                if (!r.ok) throw new Error("HTTP " + r.status + " " + r.statusText)
                                return r.json()
                            })
                            .then(spec => {
                                window.ui = SwaggerUIBundle({
                                    spec: regroupByPath(spec),
                                    dom_id: '#swagger-ui',
                                    presets: [
                                        SwaggerUIBundle.presets.apis,
                                        SwaggerUIStandalonePreset
                                    ],
                                    layout: "StandaloneLayout",
                                    tagsSorter: "alpha",
                                    operationsSorter: "alpha",
                                    docExpansion: "none"
                                })
                            })
                            .catch(err => showError(String(err)))
                    }
                </script>
            </body>
            </html>
            """
    }

    var body: some View {
        WebViewRepresentable(
            htmlString: swaggerUIHTML,
            baseURL: URL(string: "https://apidocs.agenticdeveloperstorage.com/")
        )
        .frame(minWidth: 800, minHeight: 600)
    }
}

#Preview {
    OpenAPIViewerWindow()
}
#endif
