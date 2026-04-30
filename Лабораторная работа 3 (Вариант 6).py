# ЕМЕЛЬЯНЕНКО АНАСТАСИЯ
# ЛАБОРАТОРНАЯ РАБОТА 3
# ВАРИАНТ 6


from statsmodels.datasets import longley
import matplotlib.pyplot as plt # библиотека для графиков


data = longley.load_pandas().data #таблица с численными данными
print(data.head())
years = [1951, 1952, 1953, 1954, 1955]

gnpdefl = [data["GNPDEFL"][4], data["GNPDEFL"][5], data["GNPDEFL"][6], data["GNPDEFL"][7], data["GNPDEFL"][8]] #инфляция
unemp = [data["UNEMP"][4], data["UNEMP"][5], data["UNEMP"][6], data["UNEMP"][7], data["UNEMP"][8]] #безработица
armed = [data["ARMED"][4], data["ARMED"][5], data["ARMED"][6], data["ARMED"][7], data["ARMED"][8]] #армия

plt.figure(figsize=(15, 8))
plt.plot(years, gnpdefl, linewidth=2)
plt.plot(years, unemp, linewidth=2)
plt.plot(years, armed, linewidth=2)

plt.legend(["GNPDEFL", "UNEMP", "ARMED"])
plt.title("Данные за 1951-1955")
plt.grid(True)
plt.show()

