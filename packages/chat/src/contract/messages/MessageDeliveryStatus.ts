export type MessageDeliveryStatus =
  | { readonly kind: 'composing' }
  | { readonly kind: 'sending' }
  | { readonly kind: 'sent' }
  | { readonly kind: 'delivered' }
  | { readonly kind: 'failed'; readonly reason: string }
  | { readonly kind: 'received' }
