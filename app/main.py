from __future__ import annotations
import subprocess
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.scatter_parser import parse_scatter, firmware_path

# SP Flash Tool yang diletakkan di dalam repository.
BUNDLED_SPFT = ROOT / "SP_Flash_Tool_v5"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AJI MULTITOOL SERVIS")
        self.geometry("1050x650")
        self.minsize(900, 560)
        self.scatter = tk.StringVar()
        self.spft = tk.StringVar(value=str(BUNDLED_SPFT) if BUNDLED_SPFT.is_dir() else "")
        self.status = tk.StringVar(value="Siap. Mode aman: belum ada operasi write ke perangkat.")
        self._build()
        self._check_spft()

    def _build(self):
        top = ttk.Frame(self, padding=12); top.pack(fill="x")
        ttk.Label(top, text="AJI MULTITOOL SERVIS", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(top, text="MediaTek service frontend • Scatter / SP Flash Tool v5 bridge").pack(anchor="w")

        f = ttk.LabelFrame(self, text="Firmware", padding=10); f.pack(fill="x", padx=12, pady=8)
        ttk.Label(f, text="Scatter:").grid(row=0,column=0,sticky="w")
        ttk.Entry(f, textvariable=self.scatter).grid(row=0,column=1,sticky="ew",padx=8)
        ttk.Button(f,text="Pilih…",command=self.choose_scatter).grid(row=0,column=2)
        ttk.Label(f, text="SP Flash Tool v5:").grid(row=1,column=0,sticky="w",pady=(8,0))
        ttk.Entry(f, textvariable=self.spft).grid(row=1,column=1,sticky="ew",padx=8,pady=(8,0))
        ttk.Button(f,text="Pilih folder…",command=self.choose_spft).grid(row=1,column=2,pady=(8,0))
        f.columnconfigure(1,weight=1)

        b = ttk.Frame(self,padding=(12,4)); b.pack(fill="x")
        ttk.Button(b,text="Baca Scatter",command=self.load_scatter).pack(side="left",padx=(0,6))
        ttk.Button(b,text="Dry-Run Flash Plan",command=self.dry_run).pack(side="left",padx=6)
        ttk.Button(b,text="Jalankan SP Flash Tool",command=self.launch_spft).pack(side="left",padx=6)

        self.tree=ttk.Treeview(self,columns=("file","start","size","region","op"),show="headings")
        for col,title,w in [("file","File",260),("start","Linear Start",130),("size","Size",130),("region","Region",120),("op","Operation",120)]:
            self.tree.heading(col,text=title); self.tree.column(col,width=w)
        self.tree.pack(fill="both",expand=True,padx=12,pady=8)
        ttk.Label(self,textvariable=self.status,relief="sunken",anchor="w").pack(fill="x",side="bottom")

    def _check_spft(self):
        exe = Path(self.spft.get()) / "flash_tool.exe" if self.spft.get() else None
        if exe and exe.exists():
            self.status.set("SP Flash Tool v5 ditemukan di dalam repository.")
        else:
            self.status.set("SP Flash Tool v5 belum ditemukan di repository. Pilih folder secara manual.")

    def choose_scatter(self):
        p=filedialog.askopenfilename(title="Pilih scatter",filetypes=[("Scatter","*.txt"),("Semua","*.*")])
        if p: self.scatter.set(p); self.load_scatter()

    def choose_spft(self):
        p=filedialog.askdirectory(title="Folder SP Flash Tool v5")
        if p: self.spft.set(p); self._check_spft()

    def load_scatter(self):
        if not self.scatter.get(): return
        try:
            parts=parse_scatter(self.scatter.get())
            for x in self.tree.get_children(): self.tree.delete(x)
            for p in parts:
                self.tree.insert("","end",values=(p.file_name,hex(p.linear_start) if p.linear_start is not None else "",hex(p.size) if p.size is not None else "",p.region,p.operation))
            self.status.set(f"Scatter terbaca: {len(parts)} partisi.")
        except Exception as e:
            messagebox.showerror("Scatter error",str(e))

    def dry_run(self):
        if not self.scatter.get(): return messagebox.showwarning("Scatter","Pilih scatter terlebih dahulu.")
        parts=parse_scatter(self.scatter.get()); missing=[]
        for p in parts:
            if p.file_name and p.file_name != "NONE":
                fp=firmware_path(self.scatter.get(),p.file_name)
                if not fp.exists(): missing.append(p.file_name)
        msg=f"Partisi: {len(parts)}\nFile firmware hilang: {len(missing)}"
        if missing: msg += "\n\n" + "\n".join(missing[:15])
        messagebox.showinfo("Dry-Run",msg); self.status.set("Dry-run selesai; tidak ada write ke perangkat.")

    def launch_spft(self):
        folder=Path(self.spft.get())
        exe=folder/"flash_tool.exe"
        if not exe.exists():
            return messagebox.showerror("SP Flash Tool","flash_tool.exe tidak ditemukan.\n\nLokasi yang dicari:\n" + str(exe))
        try:
            subprocess.Popen([str(exe)],cwd=str(folder))
            self.status.set("SP Flash Tool v5 dijalankan dari repository.")
        except Exception as e:
            messagebox.showerror("SP Flash Tool",f"Gagal menjalankan SP Flash Tool:\n{e}")

if __name__ == "__main__":
    App().mainloop()
