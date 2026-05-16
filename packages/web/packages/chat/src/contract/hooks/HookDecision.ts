export type HookDecision =
  | { readonly kind: 'proceed' }
  | { readonly kind: 'block'; readonly reason: string }
