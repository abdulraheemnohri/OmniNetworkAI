import React, { useState, useEffect } from 'react';
import Head from 'next/head';

export default function Dashboard() {
  const [status, setStatus] = useState(null);
  const [command, setCommand] = useState('');
  const [output, setOutput] = useState([]);

  useEffect(() => {
    // In a real app, fetch from ONAIO API
    setStatus({
      protected: true,
      cpu: 12,
      memory: 45,
      devices: 5,
      traffic: [10, 20, 15, 30, 25]
    });
  }, []);

  const handleCommand = async (e) => {
    e.preventDefault();
    setOutput([...output, { type: 'in', text: command }]);
    // Mock API call
    setTimeout(() => {
      setOutput(prev => [...prev, { type: 'out', text: `Executing: ${command}. Result: Success.` }]);
    }, 500);
    setCommand('');
  };

  return (
    <div className="bg-[#060e20] min-h-screen text-[#dee5ff] font-sans">
      <Head>
        <title>OmniOperator AI Dashboard</title>
      </Head>

      <nav className="p-6 flex justify-between items-center border-b border-[#40485d]/20">
        <h1 className="text-2xl font-bold text-[#86fea7]">OmniOperator</h1>
        <div className="flex space-x-4">
          <span className="text-sm opacity-60">System Online</span>
          <div className="w-2 h-2 rounded-full bg-[#86fea7] animate-pulse"></div>
        </div>
      </nav>

      <main className="p-8 grid grid-cols-12 gap-8">
        {/* System Status */}
        <div className="col-span-12 md:col-span-4 bg-[#0f1930] p-8 rounded-3xl border border-[#40485d]/10 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-32 h-32 bg-[#86fea7]/5 rounded-full blur-3xl"></div>
          <h2 className="text-sm uppercase tracking-widest opacity-50 mb-4">Core Status</h2>
          <div className="text-5xl font-bold text-[#86fea7] mb-2">PROTECTED</div>
          <p className="opacity-70">Aegis Layer Active</p>
        </div>

        {/* Stats */}
        <div className="col-span-12 md:col-span-8 grid grid-cols-3 gap-4">
          <div className="bg-[#141f38] p-6 rounded-2xl">
            <h3 className="opacity-50 text-xs uppercase mb-2">CPU LOAD</h3>
            <div className="text-2xl font-mono">{status?.cpu}%</div>
          </div>
          <div className="bg-[#141f38] p-6 rounded-2xl">
            <h3 className="opacity-50 text-xs uppercase mb-2">MEM USAGE</h3>
            <div className="text-2xl font-mono">{status?.memory}%</div>
          </div>
          <div className="bg-[#141f38] p-6 rounded-2xl">
            <h3 className="opacity-50 text-xs uppercase mb-2">DEVICES</h3>
            <div className="text-2xl font-mono">{status?.devices}</div>
          </div>
        </div>

        {/* Console / Output */}
        <div className="col-span-12 bg-[#000000]/30 p-6 rounded-2xl font-mono text-sm h-64 overflow-y-auto border border-[#40485d]/10">
          {output.map((line, i) => (
            <div key={i} className={line.type === 'in' ? 'text-[#86fea7]' : 'text-white/70'}>
              {line.type === 'in' ? '> ' : ''}{line.text}
            </div>
          ))}
        </div>
      </main>

      {/* Command Input */}
      <div className="fixed bottom-8 left-1/2 -translate-x-1/2 w-full max-w-2xl px-4">
        <form onSubmit={handleCommand} className="relative group">
          <input
            type="text"
            value={command}
            onChange={(e) => setCommand(e.target.value)}
            placeholder="Enter operator command..."
            className="w-full bg-[#1f2b49]/80 backdrop-blur-xl border border-[#40485d]/30 rounded-full py-4 px-8 outline-none focus:border-[#86fea7]/50 transition-all text-lg"
          />
          <button type="submit" className="absolute right-4 top-1/2 -translate-y-1/2 p-2 text-[#86fea7]">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" /></svg>
          </button>
        </form>
      </div>
    </div>
  );
}
