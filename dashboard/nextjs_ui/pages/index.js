import React, { useState, useEffect } from 'react';
import Head from 'next/head';

const API_BASE = "http://localhost:8000";
const DEV_TOKEN = "DEV_TOKEN";

const StatCard = ({ label, value, unit, glow }) => (
  <div className="bg-[#0f1930] p-6 rounded-2xl border border-[#40485d]/10 relative overflow-hidden group hover:border-[#86fea7]/30 transition-all">
    {glow && <div className="absolute -top-12 -right-12 w-24 h-24 bg-[#86fea7]/5 rounded-full blur-2xl group-hover:bg-[#86fea7]/10 transition-all"></div>}
    <h3 className="text-xs uppercase tracking-tighter opacity-50 mb-1">{label}</h3>
    <div className="text-3xl font-mono text-[#dee5ff]">
      {value}<span className="text-sm ml-1 opacity-40">{unit}</span>
    </div>
  </div>
);

const DeviceItem = ({ name, ip, status, onAction }) => (
  <div className="flex items-center justify-between p-4 bg-[#141f38] rounded-xl mb-3 border border-transparent hover:border-[#86fea7]/20 transition-all">
    <div className="flex items-center space-x-4">
      <div className={`w-2 h-2 rounded-full ${status === 'up' ? 'bg-[#86fea7] animate-pulse' : 'bg-red-500'}`}></div>
      <div>
        <div className="text-sm font-medium">{name}</div>
        <div className="text-xs opacity-40 font-mono">{ip}</div>
      </div>
    </div>
    <div className="flex space-x-2">
       <button onClick={() => onAction('scan', ip)} className="text-[10px] bg-white/5 px-2 py-1 rounded hover:bg-[#86fea7]/20 transition-all">RE-SCAN</button>
       <button onClick={() => onAction('ssh', ip)} className="text-[10px] bg-white/5 px-2 py-1 rounded hover:bg-[#86fea7]/20 transition-all">AGENT_LINK</button>
    </div>
  </div>
);

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('overview');
  const [stats, setStats] = useState({ cpu: 0, mem: 0, net: 'LINKING...' });
  const [devices, setDevices] = useState([]);
  const [logs, setLogs] = useState([
    'ONAIO Kernel v4.0 Initialized',
    'Aegis Security Layer: ACTIVE',
    'Waiting for neural link...'
  ]);
  const [command, setCommand] = useState('');
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const fetchStatus = async () => {
    try {
      const res = await fetch(`${API_BASE}/status`, {
        headers: { "Authorization": `Bearer ${DEV_TOKEN}` }
      });
      const data = await res.json();
      setStats({
        cpu: data.pc_stats?.cpu || 0,
        mem: data.pc_stats?.memory || 0,
        net: data.network_status || 'STABLE'
      });
    } catch (e) { console.error("Status fail"); }
  };

  const fetchDevices = async () => {
    try {
      const res = await fetch(`${API_BASE}/devices`, {
        headers: { "Authorization": `Bearer ${DEV_TOKEN}` }
      });
      const data = await res.json();
      const devList = Object.entries(data.devices || {}).map(([ip, info]) => ({
        name: info.vendor || "Unknown Node",
        ip: ip,
        status: info.status || 'down'
      }));
      setDevices(devList);
    } catch (e) { console.error("Device fail"); }
  };

  useEffect(() => {
    fetchStatus();
    fetchDevices();
    const interval = setInterval(fetchStatus, 5000);
    return () => clearInterval(interval);
  }, []);

  const handleCommand = async (e) => {
    e.preventDefault();
    if (!command) return;
    setLogs(prev => [`> ${command}`, ...prev]);
    try {
      const res = await fetch(`${API_BASE}/execute`, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Authorization": `Bearer ${DEV_TOKEN}` },
        body: JSON.stringify({ command })
      });
      const data = await res.json();
      setLogs(prev => [`✅ [${data.intent}] Result: ${data.result}`, ...prev]);
      if (command.toLowerCase().includes('scan')) fetchDevices();
    } catch (e) {
      setLogs(prev => [`❌ KERNEL_COMM_FAILURE`, ...prev]);
    }
    setCommand('');
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`${API_BASE}/memory/search?query=${searchQuery}`, {
        headers: { "Authorization": `Bearer ${DEV_TOKEN}` }
      });
      const data = await res.json();
      setSearchResults(data.results);
    } catch (e) { console.error("Search fail"); }
  };

  return (
    <div className="bg-[#060e20] min-h-screen text-[#dee5ff] font-sans selection:bg-[#86fea7]/30">
      <Head><title>OmniOperator AI | Command Deck</title></Head>

      {/* Futuristic Nav */}
      <aside className="fixed left-0 top-0 h-screen w-20 bg-[#091328] border-r border-[#40485d]/10 flex flex-col items-center py-8 space-y-10 z-50">
        <div className="w-12 h-12 bg-gradient-to-tr from-[#86fea7] to-[#3bb668] rounded-2xl flex items-center justify-center text-[#060e20] font-black text-xl shadow-[0_0_15px_rgba(134,254,167,0.3)]">Ω</div>
        <nav className="flex flex-col space-y-8">
           {['overview', 'devices', 'network', 'cctv', 'memory', 'settings'].map(tab => (
             <button
               key={tab}
               onClick={() => setActiveTab(tab)}
               className={`w-10 h-10 rounded-xl flex items-center justify-center transition-all ${activeTab === tab ? 'text-[#86fea7] bg-[#86fea7]/10' : 'opacity-20 hover:opacity-100'}`}
             >
                <div className="w-5 h-5 border-2 border-current rounded-md"></div>
             </button>
           ))}
        </nav>
      </aside>

      <main className="pl-28 pr-8 py-10 max-w-7xl mx-auto">
        {/* Header Section */}
        <div className="flex justify-between items-center mb-16">
           <div>
              <h1 className="text-5xl font-black tracking-tighter text-white mb-2 italic">OMNI_OPERATOR</h1>
              <div className="flex items-center space-x-3 text-[10px] tracking-[0.3em] opacity-40">
                 <span className="text-[#86fea7]">AEGIS_PROTOCOL_V4</span>
                 <span className="w-1 h-1 bg-white/20 rounded-full"></span>
                 <span>SEC_LEVEL_OMEGA</span>
              </div>
           </div>
           <div className="flex items-center space-x-8">
              <div className="text-right">
                 <div className="text-[#86fea7] font-mono text-lg font-bold">{stats.net}</div>
                 <div className="text-[10px] opacity-20 uppercase">Network Synapse</div>
              </div>
              <div className="w-14 h-14 rounded-full bg-[#141f38] border-2 border-[#86fea7]/30 flex items-center justify-center relative">
                 <div className="absolute inset-0 rounded-full border-2 border-white/5 animate-ping"></div>
                 <div className="w-8 h-8 rounded-full bg-[#86fea7]/10 flex items-center justify-center">
                    <div className="w-2 h-2 bg-[#86fea7] rounded-full shadow-[0_0_10px_#86fea7]"></div>
                 </div>
              </div>
           </div>
        </div>

        <div className="grid grid-cols-12 gap-10">
          <div className="col-span-12 lg:col-span-8 space-y-10">
            <div className="grid grid-cols-3 gap-6">
              <StatCard label="NEURAL_LOAD" value={stats.cpu} unit="%" glow />
              <StatCard label="SYNAPSE_BUF" value={stats.mem} unit="%" />
              <StatCard label="NODE_COUNT" value={devices.length} unit="U" />
            </div>

            <div className="bg-[#0f1930] rounded-[2.5rem] p-10 border border-[#40485d]/10 min-h-[500px] shadow-2xl relative overflow-hidden">
              <div className="flex justify-between items-center mb-10">
                <h2 className="text-2xl font-bold tracking-tight italic opacity-90">{activeTab.toUpperCase()}_INTERFACE</h2>
                <div className="flex space-x-4">
                   <button onClick={fetchDevices} className="text-[10px] border border-white/10 px-4 py-2 rounded-full hover:bg-white/5 transition-all uppercase tracking-widest font-bold">RE-INDEX</button>
                </div>
              </div>

              {activeTab === 'overview' && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                   <div className="p-8 bg-[#141f38] rounded-3xl border border-white/5">
                      <div className="text-[#86fea7] text-[10px] font-bold mb-6 uppercase tracking-[0.2em]">Live Agents</div>
                      {['PC_KERNEL', 'MOBILE_ADB_01', 'SWITCH_SNMP_7', 'CCTV_ONVIF'].map(a => (
                        <div key={a} className="flex justify-between items-center mb-4 last:mb-0">
                           <span className="text-xs opacity-40 font-mono italic">{a}</span>
                           <span className="text-[8px] bg-[#86fea7]/20 text-[#86fea7] px-2 py-1 rounded-md font-bold">STABLE</span>
                        </div>
                      ))}
                   </div>
                   <div className="flex flex-col justify-center items-center text-center opacity-10">
                      <div className="text-9xl font-black tracking-tighter">O</div>
                      <div className="text-xs tracking-[1em] mt-[-20px]">MASTER_CORE</div>
                   </div>
                </div>
              )}

              {activeTab === 'devices' && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {devices.map((d, i) => <DeviceItem key={i} {...d} onAction={(t, i) => setCommand(`${t} ${i}`)} />)}
                </div>
              )}

              {activeTab === 'memory' && (
                <div className="space-y-6">
                   <form onSubmit={handleSearch} className="relative">
                      <input
                        type="text"
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                        placeholder="Search Vector Memory..."
                        className="w-full bg-[#141f38] border border-white/10 rounded-2xl py-4 px-6 outline-none focus:border-[#86fea7]/40 transition-all text-sm"
                      />
                   </form>
                   <div className="space-y-4">
                      {searchResults.map((r, i) => (
                        <div key={i} className="p-4 bg-[#141f38] rounded-xl border-l-4 border-[#86fea7]">
                           <p className="text-sm opacity-80 mb-2">{r.text}</p>
                           <div className="text-[10px] opacity-30 font-mono">{JSON.stringify(r.metadata)}</div>
                        </div>
                      ))}
                   </div>
                </div>
              )}

              {activeTab === 'settings' && (
                <div className="grid grid-cols-2 gap-6">
                   {['AUTO_RESTART_ROUTER', 'ALLOW_REMOTE_SHUTDOWN', 'CLOUD_FALLBACK', 'VERBOSE_LOGS'].map(s => (
                     <div key={s} className="p-6 bg-[#141f38] rounded-2xl flex justify-between items-center border border-white/5 hover:border-[#86fea7]/20 transition-all cursor-pointer">
                        <span className="text-xs font-bold opacity-60 tracking-wider">{s}</span>
                        <div className="w-10 h-5 bg-[#86fea7]/10 rounded-full relative">
                           <div className="absolute right-1 top-1 w-3 h-3 bg-[#86fea7] rounded-full shadow-[0_0_8px_#86fea7]"></div>
                        </div>
                     </div>
                   ))}
                </div>
              )}
            </div>
          </div>

          <div className="col-span-12 lg:col-span-4 space-y-10">
            {/* Console */}
            <div className="bg-[#000000]/60 rounded-[2rem] p-8 border border-[#40485d]/20 h-[600px] flex flex-col font-mono text-[11px] backdrop-blur-3xl shadow-2xl relative group">
               <div className="absolute -inset-1 bg-gradient-to-tr from-[#86fea7]/10 to-transparent rounded-[2.1rem] -z-10 group-hover:from-[#86fea7]/20 transition-all"></div>
               <div className="flex items-center justify-between mb-6 border-b border-white/5 pb-4">
                  <span className="text-[10px] font-bold text-[#86fea7] tracking-widest opacity-80 uppercase">Root_Aegis_Shell</span>
                  <div className="flex space-x-1.5">
                    <div className="w-2.5 h-2.5 bg-red-500/30 rounded-full"></div>
                    <div className="w-2.5 h-2.5 bg-green-500/30 rounded-full animate-pulse"></div>
                  </div>
               </div>
               <div className="flex-1 overflow-y-auto space-y-3 pr-4 flex flex-col-reverse scrollbar-hide">
                  {logs.map((log, i) => (
                    <div key={i} className={`opacity-90 leading-relaxed border-l-2 pl-3 ${log.startsWith('>') ? 'text-[#86fea7] border-[#86fea7]/40' : log.startsWith('✅') ? 'text-cyan-400 border-cyan-400/40' : 'text-white/60 border-white/5'}`}>
                      <span className="opacity-20 text-[9px] mr-2 italic">{new Date().toLocaleTimeString()}</span>
                      {log}
                    </div>
                  ))}
               </div>
               <form onSubmit={handleCommand} className="mt-8 relative">
                  <input
                    type="text"
                    placeholder="Enter Command Hash..."
                    value={command}
                    onChange={(e) => setCommand(e.target.value)}
                    className="w-full bg-[#141f38] border border-white/10 rounded-2xl py-5 px-6 outline-none focus:border-[#86fea7]/50 transition-all text-[#86fea7] placeholder:opacity-20"
                  />
                  <div className="absolute right-6 top-1/2 -translate-y-1/2 text-[#86fea7] opacity-40 font-black text-xl animate-pulse">_</div>
               </form>
            </div>

            {/* Quick Tactical Overrides */}
            <div className="bg-[#0f1930] p-8 rounded-[2rem] border border-[#40485d]/10">
               <h3 className="text-xs font-black mb-6 opacity-30 uppercase tracking-[0.4em]">Tactical_Actions</h3>
               <div className="grid grid-cols-2 gap-4">
                  <button onClick={() => setCommand('scan network')} className="bg-white/5 hover:bg-[#86fea7]/20 p-4 rounded-2xl text-[10px] font-black transition-all border border-white/5 uppercase tracking-widest">Map_Net</button>
                  <button onClick={() => setCommand('restart router')} className="bg-white/5 hover:bg-[#86fea7]/20 p-4 rounded-2xl text-[10px] font-black transition-all border border-white/5 uppercase tracking-widest">Reset_Gate</button>
                  <button className="bg-red-500/5 hover:bg-red-500/20 text-red-500/60 p-4 rounded-2xl text-[10px] font-black transition-all border border-red-500/10 uppercase tracking-widest">Purge_Sys</button>
               </div>
            </div>
          </div>
        </div>
      </main>

      <footer className="fixed bottom-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-[#86fea7]/10 to-transparent"></footer>
    </div>
  );
}
