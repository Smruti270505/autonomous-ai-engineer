"use client";

import { useEffect, useState } from "react";

export default function FileExplorer() {

  const [files, setFiles] = useState<string[]>([]);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/files")
      .then((res) => res.json())
      .then((data) => setFiles(data));

  }, []);

  function handleClick(file: string) {
    console.log(file);
  }

  return (

    <div className="w-64 h-screen bg-zinc-950 border-r border-zinc-800 p-4 text-white">

      <h2 className="font-bold mb-4">Explorer</h2>

      <div className="space-y-2 text-sm">

        {files.map((file, index) => (

          <p
            key={index}
            onClick={() => handleClick(file)}
            className="cursor-pointer hover:text-blue-400"
          >
            📄 {file}
          </p>

        ))}

      </div>

    </div>

  );
}