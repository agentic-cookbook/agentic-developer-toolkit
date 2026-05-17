import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: [
    "@agentic-persona-toolkit/chat",
    "@agentic-persona-toolkit/themes",
    "@agentic-persona-toolkit/viewport",
  ],
};

export default nextConfig;
