import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: [
    "@agentic-developer-toolkit/chat",
    "@agentic-developer-toolkit/themes",
  ],
};

export default nextConfig;
