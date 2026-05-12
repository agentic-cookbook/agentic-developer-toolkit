import { notFound } from 'next/navigation'
import { examples } from '../manifest'

export function generateStaticParams() {
  return examples.map((e) => ({ exampleId: e.id }))
}

export const dynamicParams = false

export default async function ExamplePage({
  params,
}: {
  params: Promise<{ exampleId: string }>
}) {
  const { exampleId } = await params
  const entry = examples.find((e) => e.id === exampleId)
  if (!entry) {
    notFound()
  }
  const Component = entry.Component
  return <Component />
}
