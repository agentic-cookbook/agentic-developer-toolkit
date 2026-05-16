export interface CommandResult {
  readonly invocationID: string
  readonly ok: boolean
  readonly resultJSON?: string
  readonly errorMessage?: string
  readonly completedAt: Date
}
