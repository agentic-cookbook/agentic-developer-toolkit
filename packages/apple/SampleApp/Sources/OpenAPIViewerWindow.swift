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
                <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3.52.5/swagger-ui.css"
                      integrity="sha384-r/Hd/7wTjY0ZrJfOI3W4v2r5xpYVNqiM7H/+IvfmGgHh7v2zTPqEy6gKl0KGqNAm"
                      crossorigin="anonymous">
                <style>
                    html { box-sizing: border-box; overflow: -moz-scrollbars-vertical; overflow-y: scroll; }
                    *, *:before, *:after { box-sizing: inherit; }
                    body { margin: 0; padding: 0; }
                </style>
            </head>
            <body>
                <div id="swagger-ui"></div>
                <script src="https://unpkg.com/swagger-ui-dist@3.52.5/swagger-ui.bundle.js"
                        integrity="sha384-NhqqjHXSIV5nPzIqHI0ygUeF3v5IoXZ/UkycdrysKAuPAZcKUP3tFtzpih0bUfYP"
                        crossorigin="anonymous"></script>
                <script src="https://unpkg.com/swagger-ui-dist@3.52.5/swagger-ui-standalone-preset.js"
                        integrity="sha384-LyT8YCv/L3Eg9Kxgf7EVzQKKO4BhZaWtC7NKnYPpTqX8JZJS/4zMrBn5mWBw5Yo/"
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
        WebViewRepresentable(htmlString: swaggerUIHTML)
            .frame(minWidth: 800, minHeight: 600)
    }
}

#Preview {
    OpenAPIViewerWindow()
}
