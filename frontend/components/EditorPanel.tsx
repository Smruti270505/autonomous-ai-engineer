"use client";

import Editor from "@monaco-editor/react";

export default function EditorPanel() {
  return (
    <div className="flex-1">
      <Editor
        height="100vh"
        defaultLanguage="python"
        defaultValue="# Start coding..."
        theme="vs-dark"
      />
    </div>
  );
}