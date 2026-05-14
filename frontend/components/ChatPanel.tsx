"use client";

import { useState } from "react";
import axios from "axios";

interface Message {
  role: string;
  content: string;
}

export default function ChatPanel() {

  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState<Message[]>([]);

  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {

    if (!message.trim()) return;

    const userMessage = {
      role: "user",
      content: message
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {

      const res = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          messages: [...messages, userMessage]
        }
      );

      const aiMessage = {
        role: "assistant",
        content: res.data.response
      };

      setMessages((prev) => [...prev, aiMessage]);

    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }

    setMessage("");
  };

  return (
    <div className="w-96 h-screen bg-zinc-950 border-l border-zinc-800 text-white flex flex-col">

      <div className="p-4 border-b border-zinc-800 font-bold">
        AI Assistant
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">

        {messages.map((msg, index) => (

          <div
            key={index}
            className={`p-3 rounded-lg max-w-[90%]
              ${msg.role === "user"
                ? "bg-blue-600 ml-auto"
                : "bg-zinc-800"
              }`}
          >
            {msg.content}
          </div>

        ))}

        {loading && (
          <div className="bg-zinc-800 p-3 rounded-lg w-fit">
            Thinking...
          </div>
        )}

      </div>

      <div className="p-4 border-t border-zinc-800">

        <input
          type="text"
          placeholder="Ask AI anything..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          className="w-full bg-zinc-900 p-3 rounded outline-none mb-3"
        />

        <button
          onClick={sendMessage}
          className="w-full bg-blue-600 hover:bg-blue-700 p-3 rounded"
        >
          Send
        </button>

      </div>

    </div>
  );
}