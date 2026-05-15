import Foundation

/// A media-type identifier. Concrete values can be MIME ("text/markdown"),
/// UTType strings on Apple ("public.image"), or app-namespaced
/// ("application/vnd.apt.question+json"). Interpretation is up to the
/// renderer; the contract just carries the identifier string.
public protocol MediaType: Sendable {
    var identifier: String { get }
}

public enum AttachmentSource: Sendable {
    case remote(URL)
    case inline(Data)
}

public enum AttachmentPresentation: Sendable, Hashable {
    case inline      // rendered in the transcript at message position
    case attached    // separate affordance (preview, download, …)
}
