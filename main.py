# %% importları yapalım
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
# %%
df = pd.read_csv("train.csv") #Veri Yükleme
df_copy = df.copy() #verinin kopyasını alıyoruz.

# %%
df_copy.head()
df_copy.shape  #Verinin boyutu
df_copy.columns  #Kolonlar
df_copy.info() #genel bakış. Veri tipleri.
df_copy.describe() #sayısal özellikler için özet
df_copy.isnull().sum().sort_values(ascending=False) #boş değer kontrolü.

# %% Target dağılımı
sns.histplot(df_copy["SalePrice"], kde=True)
plt.show()

# %% hangi mahallede evlerin daha pahalı
df.groupby("Neighborhood")["SalePrice"].mean().sort_values().plot(kind="barh", figsize=(8,6))
plt.title("Neighborhood Ortalama Ev Fiyatları")
plt.show()

# %% log dönüşümü yapıyoruz ki dağılım grafiği sıkıştırılsın. Outlier değerleri azaltmak için.
df_copy["SalePrice"] = np.log1p(df_copy["SalePrice"])

# %% Korelasyon -- sayısal değerlerin birbirlerini nasıl etkilediğini analiz ediyoruz.
corr = df_copy.corr(numeric_only=True)  
corr["SalePrice"].sort_values(ascending=False).head(10)

# %% heatmap bu tür verisetlerinde okunurluğu düşürdüğü için tercih edilmeyebilir.
plt.figure(figsize=(10,8))
sns.heatmap(corr, cmap="coolwarm") #veriyi harita üzerinde gözlimliyoruz.
plt.show()

# Gereksiz kolon silme-- id kolonunu siliyoruz.
df_copy.drop("Id", axis=1, inplace=True)

# %% outlier temizliği.
df_copy=df_copy[df_copy["GrLivArea"] < 4000] 

# %% Fazla eksik değere sahip kolonları siliyoruz.
df_copy.drop(["PoolQC", "MiscFeature", "Alley", "Fence"], axis=1, inplace=True)

# %% eksik verileri doldurma.
df_copy["MasVnrType"] = df_copy["MasVnrType"].fillna("None")
df_copy["MasVnrArea"] = df_copy["MasVnrArea"].fillna(0)

garage_cols = ["GarageFinish", "GarageType", "GarageQual", "GarageCond"]
for col in garage_cols:
    df_copy[col] = df_copy[col].fillna("None")

bsmt_cols = ["BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinType2"]
for col in bsmt_cols:
    df_copy[col] = df_copy[col].fillna("None")

# %% eksik değerleri doldurmak- sayısal değerler
df_copy["GarageYrBlt"] = df_copy["GarageYrBlt"].fillna(0)
df_copy["LotFrontage"] = df_copy["LotFrontage"].fillna(df_copy["LotFrontage"].median())
df_copy["Electrical"] = df_copy["Electrical"].fillna(df_copy["Electrical"].mode()[0])
df_copy["FireplaceQu"] = df_copy["FireplaceQu"].fillna("None")

# %% Yeni feature yaratmak
df_copy["TotalSF"] = df_copy["TotalBsmtSF"] + df_copy["1stFlrSF"] + df_copy["2ndFlrSF"]
# %% evdeki toplam banyoyu tek bir sayıya dönüştüren yeni bir feature
df_copy["TotalBathrooms"] = (df_copy["FullBath"] + 0.5 * df_copy["HalfBath"] + df_copy["BsmtFullBath"] + 0.5 * df_copy["BsmtHalfBath"])

# %% eksik veri kontrolü.
df_copy.isnull().sum().sum()

# %% encoding yapmak.
df_copy= pd.get_dummies(df_copy, drop_first=True)

# %% Feature – Target ayırma
X = df_copy.drop("SalePrice", axis=1) #satış kolunu  düşürdük sadece özellikler kaldı.
y = df_copy["SalePrice"] #target

# %%  Train-test split ayırma
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# %% model eğitmek.
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test) #Tahmin

# %% Model değerlendirme
mse =mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("RMSE: ",rmse)
# %% Model gerçekten iyi mi görmek için 
r2 = r2_score(y_test, y_pred)
print("R2:",r2)

# %%
print(y_test.min(), y_test.max())

# %% Grafik.
plt.scatter(y_test, y_pred)
plt.xlabel("Gerçek değer")
plt.ylabel("Tahmin")
plt.title("Gerçek ve Tahmin")
plt.show()

# %% Model karşılaştırması- random_state Sonuçların her çalıştırmada değişmesini engeller.
models = {
    "Linear": LinearRegression(),
    "Tree": DecisionTreeRegressor(random_state=42),
    "Forest": RandomForestRegressor(random_state=42)
}

sonuclar = {}

for name, model in models.items():
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test,y_pred))

    sonuclar[name] = {"R2": r2, "RMSE": rmse}

sonuclar_df = pd.DataFrame(sonuclar).T
print(sonuclar_df)

# %% cross validation (veri setlerini değiştirmek--veri setlerini farklı katmanlara bölerek modelin genellenebilirliğini ölçer)
sonuclar = {}

for name, model in models.items(): # her model için for içinde cross val yaptırmak.

    scores = cross_val_score(model, X, y, cv=5, scoring="r2")

    sonuclar[name] = scores.mean()

sonuclar_df = pd.DataFrame.from_dict(sonuclar, orient="index", columns=["CV_R2"])

# en iyi modeli en üstte göstermek için sıralama
sonuclar_df = sonuclar_df.sort_values("CV_R2", ascending=False)

print(sonuclar_df)
