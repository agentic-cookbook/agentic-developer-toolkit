import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: [
    "@agentic-persona-toolkit/chat",
    "@agentic-persona-toolkit/themes",
  ],
};

export default nextConfig;
