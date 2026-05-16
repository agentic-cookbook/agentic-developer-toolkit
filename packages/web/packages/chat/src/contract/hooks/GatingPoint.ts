export type GatingPoint =
  | 'willSubmitMessage'
  | 'willExecuteCommand'
  | 'willEmitUpdate'
  | 'willRequestPermission'
  | 'willAcceptInboundMessage'
