# 基于 tkinter、sympy、numpy、matplotlib 实现的泰勒展开计算器，并绘制展开后的函数图像
# 写法示例：(1+x)^-1，ln(1+x)，exp(x)，sin(x)
import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 让 matplotlib 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


# ============ 核心计算函数 ============
def parse_expr(expr_str):
    """把用户输入的字符串转成 sympy 表达式"""
    x = sp.Symbol('x')
    expr_str = expr_str.strip()
    # 支持常见写法替换
    expr_str = expr_str.replace('ln(', 'log(')     # ln -> log
    expr_str = expr_str.replace('^', '**')          # ^ -> **
    return sp.sympify(expr_str)


def maclaurin(expr, n_terms):
    """麦克劳林展开，返回保留 n_terms 项的表达式"""
    x = sp.Symbol('x')
    result = sp.Integer(0)
    for i in range(n_terms):
        deriv = sp.diff(expr, x, i).subs(x, 0)#在0处展开，若要修改，修改0为其他数值即可
        result += deriv * x**i / sp.factorial(i)
    return sp.expand(result)


# ============ GUI 程序 ============
class TaylorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("泰勒展开计算器")
        self.root.geometry("700x600")
        
        # ---- 输入区 ----
        frame_input = ttk.LabelFrame(root, text="输入", padding=10)
        frame_input.pack(fill='x', padx=10, pady=8)
        
        # 表达式
        ttk.Label(frame_input, text="表达式 f(x):").grid(row=0, column=0, sticky='w', pady=4)
        self.entry_expr = ttk.Entry(frame_input, width=40)
        self.entry_expr.grid(row=0, column=1, padx=6, pady=4)
        self.entry_expr.insert(0, "sin(x)")
        ttk.Label(frame_input, text="例: sin(x), exp(x), 1/(1+x), ln(1+x)").grid(
            row=0, column=2, sticky='w', padx=6)
        
        # 展开项数
        ttk.Label(frame_input, text="展开项数:").grid(row=1, column=0, sticky='w', pady=4)
        self.spin_terms = ttk.Spinbox(frame_input, from_=1, to=20, width=8)
        self.spin_terms.set(5)
        self.spin_terms.grid(row=1, column=1, sticky='w', padx=6, pady=4)
        
        # 返回类型
        ttk.Label(frame_input, text="返回类型:").grid(row=2, column=0, sticky='w', pady=4)
        self.var_style = tk.StringVar(value='expr')
        frame_style = ttk.Frame(frame_input)
        frame_style.grid(row=2, column=1, sticky='w', padx=6, pady=4)
        ttk.Radiobutton(frame_style, text="表达式", variable=self.var_style,
                        value='expr', command=self.on_style_change).pack(side='left')
        ttk.Radiobutton(frame_style, text="数值", variable=self.var_style,
                        value='num', command=self.on_style_change).pack(side='left', padx=12)
        
        # 数值 x
        ttk.Label(frame_input, text="x 的值:").grid(row=3, column=0, sticky='w', pady=4)
        self.entry_xval = ttk.Entry(frame_input, width=15)
        self.entry_xval.grid(row=3, column=1, sticky='w', padx=6, pady=4)
        self.entry_xval.insert(0, "0.5")
        self.entry_xval.config(state='disabled')  # 默认禁用
        
        # ---- 按钮区 ----
        frame_btn = ttk.Frame(root, padding=5)
        frame_btn.pack(fill='x', padx=10)
        ttk.Button(frame_btn, text="计算", command=self.calculate).pack(side='left', padx=4)
        ttk.Button(frame_btn, text="绘图对比", command=self.plot).pack(side='left', padx=4)
        ttk.Button(frame_btn, text="清空输出", command=self.clear_output).pack(side='left', padx=4)
        
        # ---- 输出区 ----
        frame_out = ttk.LabelFrame(root, text="结果", padding=10)
        frame_out.pack(fill='both', expand=True, padx=10, pady=8)
        
        self.text_out = tk.Text(frame_out, height=18, wrap='word')
        self.text_out.pack(fill='both', expand=True, side='left')
        scrollbar = ttk.Scrollbar(frame_out, orient='vertical', command=self.text_out.yview)
        scrollbar.pack(side='right', fill='y')
        self.text_out.config(yscrollcommand=scrollbar.set)
    
    # ---- 事件：返回类型切换 ----
    def on_style_change(self):
        if self.var_style.get() == 'num':
            self.entry_xval.config(state='normal')
        else:
            self.entry_xval.config(state='disabled')
    
    # ---- 事件：计算 ----
    def calculate(self):
        try:
            expr = parse_expr(self.entry_expr.get())
            n_terms = int(self.spin_terms.get())
            if n_terms < 1:
                raise ValueError("项数至少为 1")
            
            poly = maclaurin(expr, n_terms)
            
            self.text_out.insert('end', f"原函数: f(x) = {expr}\n")
            self.text_out.insert('end', f"麦克劳林展开（{n_terms} 项）:\n")
            self.text_out.insert('end', f"  {poly}\n")
            
            if self.var_style.get() == 'num':
                xval_str = self.entry_xval.get().strip()
                xval = sp.sympify(xval_str)
                approx = poly.subs(sp.Symbol('x'), xval)
                true_val = expr.subs(sp.Symbol('x'), xval)
                self.text_out.insert('end', f"\n数值结果 (x = {xval}):\n")
                self.text_out.insert('end', f"  近似值: {sp.N(approx, 10)}\n")
                self.text_out.insert('end', f"  真实值: {sp.N(true_val, 10)}\n")
                try:
                    err = abs(float(approx) - float(true_val))
                    self.text_out.insert('end', f"  误差:   {err:.3e}\n")
                except Exception:
                    pass
            
            self.text_out.insert('end', "\n" + "-" * 50 + "\n")
            self.text_out.see('end')
        
        except Exception as e:
            messagebox.showerror("计算错误", f"出错: {e}")
    
    # ---- 事件：绘图 ----
    def plot(self):
        try:
            expr = parse_expr(self.entry_expr.get())
            x = sp.Symbol('x')
            
            # 只绘制 2、4、6、8 项
            term_list = [2, 4, 6, 8]
            polys = {}
            for n in term_list:
                polys[n] = maclaurin(expr, n)
            
            # 生成数值函数
            f_true = sp.lambdify(x, expr, 'numpy')
            f_polys = {n: sp.lambdify(x, polys[n], 'numpy') for n in polys}
            
            # 采样范围：以 0 为中心
            xs = np.linspace(-3, 3, 800)
            try:
                ys_true = f_true(xs)
                ys_true = np.asarray(ys_true, dtype=float)
            except Exception:
                ys_true = np.full_like(xs, np.nan)
            
            # 绘图
            fig, ax = plt.subplots(figsize=(9, 6), dpi=90)
            
            # 真实曲线：淡一点、粗一点、放底层（zorder 低）
            ax.plot(xs, ys_true, '-', color='black', linewidth=5,
                    alpha=0.3, label='真实值 f(x)', zorder=1)
            
            # 各阶展开曲线，用鲜明的颜色，放上层
            colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']  # 蓝、绿、橙、红
            line_styles = ['-', '--', '-.', ':']
            for idx, n in enumerate(term_list):
                try:
                    ys = f_polys[n](xs)
                    ys = np.asarray(ys, dtype=float)
                    # 把极端值截断，避免 y 轴被拉爆
                    ys[np.abs(ys) > 1e3] = np.nan
                    ax.plot(xs, ys,
                            linestyle=line_styles[idx],
                            color=colors[idx],
                            linewidth=2.0,
                            alpha=0.9,
                            label=f'{n} 项展开',
                            zorder=3 + idx)  # 逐层往上叠
                except Exception:
                    pass
            
            ax.axhline(0, color='gray', linewidth=0.5, zorder=0)
            ax.axvline(0, color='gray', linewidth=0.5, zorder=0)
            ax.set_ylim(-5, 5)   # 限制 y 轴范围，避免高阶爆炸把图压扁
            ax.set_xlim(-3, 3)
            ax.set_title(f'泰勒展开对比:  {sp.sstr(expr)}', fontsize=13)
            ax.set_xlabel('x', fontsize=11)
            ax.set_ylabel('y', fontsize=11)
            ax.grid(True, alpha=0.3)
            ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
            
            plt.tight_layout()
            plt.show()
        
        except Exception as e:
            messagebox.showerror("绘图错误", f"出错: {e}")
    
    # ---- 事件：清空 ----
    def clear_output(self):
        self.text_out.delete('1.0', 'end')


# ============ 入口 ============
if __name__ == '__main__':
    root = tk.Tk()
    app = TaylorApp(root)
    root.mainloop()