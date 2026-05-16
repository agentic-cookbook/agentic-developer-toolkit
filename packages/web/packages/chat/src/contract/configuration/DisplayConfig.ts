export interface DisplayConfig {
  readonly showAvatars: boolean
  readonly showReadReceipts: boolean
  readonly showTypingIndicators: boolean
  readonly maxParticipants?: number
  readonly allowJoining: boolean
  readonly allowDeparting: boolean
  readonly themeIdentifier?: string
  readonly reducedMotion: boolean
}
