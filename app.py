"""GUI-приложение калькулятора дохода по вкладу (Tkinter)."""
import tkinter as tk
from tkinter import messagebox

from calculator import calculate_income, parse_positive_number


class CalculatorApp:
    """Окно калькулятора: только представление, расчёт делегирует calculator.py."""

    def __init__(self, root):
        self.root = root
        root.title("Калькулятор дохода по вкладу")
        root.geometry("450x350")
        root.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        tk.Label(self.root, text="Расчёт дохода по банковскому вкладу",
                 font=("Arial", 14, "bold")).pack(pady=15)

        frame_inputs = tk.Frame(self.root)
        frame_inputs.pack(pady=10)
        self.entry_sum = self._input_row(frame_inputs, 0, "Сумма вклада (руб.):")
        self.entry_rate = self._input_row(frame_inputs, 1, "Годовая ставка (%):")
        self.entry_days = self._input_row(frame_inputs, 2, "Срок размещения (дней):")

        frame_result = tk.Frame(self.root)
        frame_result.pack(pady=15)
        tk.Label(frame_result, text="Доход (руб.):",
                 font=("Arial", 11, "bold")).grid(row=0, column=0, padx=5)
        self.result_var = tk.StringVar()
        tk.Label(frame_result, textvariable=self.result_var,
                 font=("Arial", 11, "bold"), fg="blue").grid(row=0, column=1, padx=5)

        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=15)
        tk.Button(frame_buttons, text="Рассчитать", command=self.on_calculate,
                  width=12, bg="#4CAF50", fg="white",
                  font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5)
        tk.Button(frame_buttons, text="Очистить", command=self.on_clear,
                  width=12, bg="#2196F3", fg="white",
                  font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5)
        tk.Button(frame_buttons, text="Выход", command=self.on_exit,
                  width=12, bg="#f44336", fg="white",
                 font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5)

    def _input_row(self, parent, row, label_text):
        tk.Label(parent, text=label_text, width=25, anchor="w").grid(
            row=row, column=0, padx=5, pady=5)
        entry = tk.Entry(parent, width=20)
        entry.grid(row=row, column=1, padx=5, pady=5)
        return entry

    def on_calculate(self):
        try:
            s = parse_positive_number(self.entry_sum.get())
            p = parse_positive_number(self.entry_rate.get())
            d = parse_positive_number(self.entry_days.get())
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
            return
        self.result_var.set(f"{calculate_income(s, p, d):.2f}")

    def on_clear(self):
        for entry in (self.entry_sum, self.entry_rate, self.entry_days):
            entry.delete(0, tk.END)
        self.result_var.set("")

    def on_exit(self):
        if messagebox.askyesno("Выход", "Вы действительно хотите выйти?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()