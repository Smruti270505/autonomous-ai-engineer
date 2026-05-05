export default function FileExplorer() {
  return (
    <div className="w-64 h-screen bg-zinc-950 border-r border-zinc-800 p-4 text-white">
      <h2 className="font-bold mb-4">Explorer</h2>

      <div className="space-y-2 text-sm">
        <p>📁 frontend</p>
        <p>📁 backend</p>
        <p>📄 main.py</p>
        <p>📄 page.tsx</p>
      </div>
    </div>
  );
}