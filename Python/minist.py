from sklearn.datasets import fetch_openml

minist = fetch_openml('minist_784', as_frame=False)
x,y = minist.data, minist.target
print(x)
