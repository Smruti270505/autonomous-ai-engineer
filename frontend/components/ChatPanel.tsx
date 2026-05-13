"use client";

import { useState } from "react";
import axios from "axios";

export default function ChatPanel() {

  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {

    if (!message) return;

    setLoading(true);

    try {

      const res = await axios.post(
        "http://localhost:8000/chat",
        {
          message: message
        }
      );

      setResponse(res.data.response);

    } catch (error) {
      console.log(error);
    }

    setLoading(false);
  };

  return (
    <div className="w-80 h-screen bg-zinc-950 border-l border-zinc-800 text-white flex flex-col">

      <div className="p-4 border-b border-zinc-800 font-bold">
        AI Assistant
      </div>

      <div className="flex-1 p-4 overflow-y-auto">
        <p className="text-sm whitespace-pre-wrap">
          {response}
        </p>
      </div>

      <div className="p-4 border-t border-zinc-800">

        <input
          type="text"
          placeholder="Ask AI anything..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          className="w-full bg-zinc-900 p-2 rounded outline-none mb-2"
        />

        <button
          onClick={sendMessage}
          className="w-full bg-blue-600 p-2 rounded"
        >
          {loading ? "Thinking..." : "Send"}
        </button>

      </div>

    </div>
  );
}