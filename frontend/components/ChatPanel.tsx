export default function ChatPanel() {
  return (
    <div className="w-80 h-screen bg-zinc-950 border-l border-zinc-800 text-white flex flex-col">
      
      <div className="p-4 border-b border-zinc-800 font-bold">
        AI Assistant
      </div>

      <div className="flex-1 p-4 overflow-y-auto">
        <p className="text-sm text-zinc-400">
          Ask the AI anything about your code...
        </p>
      </div>

      <div className="p-4 border-t border-zinc-800">
        <input
          type="text"
          placeholder="Type message..."
          className="w-full bg-zinc-900 p-2 rounded outline-none"
        />
      </div>
    </div>
  );
}