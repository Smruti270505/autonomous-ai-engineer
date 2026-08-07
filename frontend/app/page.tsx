"use client";

import { useState, useEffect } from "react";

import FileExplorer from "../components/FileExplorer";
import CodeEditor from "../components/CodeEditor";
import ChatPanel from "../components/ChatPanel";

export default function Home() {

  const [selectedFile, setSelectedFile] = useState("");

  const [code, setCode] = useState("");

  useEffect(() => {

    if (!selectedFile) return;

    fetch(
      `http://127.0.0.1:8000/file?path=${selectedFile}`
    )
      .then((res) => res.json())
      .then((data) => setCode(data.content));

  }, [selectedFile]);

  return (

    <div className="flex">

      <FileExplorer onSelect={setSelectedFile} />

      <CodeEditor code={code} />

      <ChatPanel />

    </div>

  );
}