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
                    window.onload = function() {
                        const ui = SwaggerUIBundle({
                            url: "https://api.agenticdeveloperhub.com/openapi.json",
                            dom_id: '#swagger-ui',
                            presets: [
                                SwaggerUIBundle.presets.apis,
                                SwaggerUIStandalonePreset
                            ],
                            layout: "StandaloneLayout"
                        })
                        window.ui = ui
                    }
                </script>
            </body>
            </html>
            """
    }

    var body: some View {
        WebViewRepresentable(
            htmlString: swaggerUIHTML,
            baseURL: URL(string: "https://api.agenticdeveloperhub.com/")
        )
        .frame(minWidth: 800, minHeight: 600)
    }
}

#Preview {
    OpenAPIViewerWindow()
}
