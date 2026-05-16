export type AttachmentSource =
  | { readonly kind: 'remote'; readonly url: URL }
  | { readonly kind: 'inline'; readonly data: Uint8Array }
