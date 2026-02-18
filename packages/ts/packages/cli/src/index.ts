#!/usr/bin/env node
import { Command } from "commander";

const program = new Command();

program
  .name("doux-ts")
  .description("TypeScript companion CLI for Doux AI")
  .command("doctor")
  .description("Print local setup hint")
  .action(() => {
    console.log("Use `doux doctor` from the Python package for Ollama connectivity checks.");
  });

program.parse();
