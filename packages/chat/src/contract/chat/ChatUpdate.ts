export type ChatUpdate =
  | { readonly kind: 'messagesChanged' }
  | { readonly kind: 'participantsChanged' }
  | { readonly kind: 'typingChanged' }
  | { readonly kind: 'pendingPermissionsChanged' }
  | { readonly kind: 'pendingWidgetsChanged' }
  | { readonly kind: 'displayConfigChanged' }
  | { readonly kind: 'error'; readonly message: string }
