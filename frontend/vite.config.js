import { defineConfig } from "vite";

// use esbuild's automatic JSX runtime so component files don't need "import React" in scope
export default defineConfig({
  esbuild: { jsx: "automatic" },
});
