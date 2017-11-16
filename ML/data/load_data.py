from sklearn import model_selection,datasets
import matplotlib.pyplot as plt

def show_digits():
	digits = datasets.load_digits()
	fig = plt.figure()
	print("vector from image 0:",digits.data[0])
	for i in range(25):
		ax = fig.add_subplot(5,5,i+1)
		ax.imshow(digits.images[i],cmap=plt.cm.gray_r,interpolation='nearest')
	plt.show()

def load_data_digits():
	digits = datasets.load_digits()
	return model_selection.train_test_split(digits.data,digits.target,test_size = 0.25,random_state = 0)

def load_data_diabetes():
	diabetes = datasets.load_diabetes()
	return model_selection.train_test_split(diabetes.data,diabetes.target,test_size = 0.25,random_state = 0)

def load_data_iris():
	iris=datasets.load_iris()
	X_train = iris.data
	y_train = iris.target
	return model_selection.train_test_split(X_train,y_train,test_size = 0.25,
	                                         random_state = 0,stratify = y_train)