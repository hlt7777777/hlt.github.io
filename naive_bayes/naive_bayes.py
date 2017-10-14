from load_data import load_data_digits,show_digits
from naive_bayes_alg import test_GaussianNB,test_MultinomialNB,test_MultinomialNB_alpha,test_BernoulliNB,test_BernoulliNB_alpha,test_BernoulliNB_binarize

show_digits()

if __name__ == '__main__':
	X_train, X_test, y_train, y_test = load_data_digits()
	test_GaussianNB(X_train,X_test,y_train,y_test)
	test_MultinomialNB(X_train,X_test,y_train,y_test)
	test_MultinomialNB_alpha(X_train,X_test,y_train,y_test)
	test_BernoulliNB(X_train, X_test, y_train, y_test)
	test_BernoulliNB_alpha(X_train, X_test, y_train, y_test)
	test_BernoulliNB_binarize(X_train, X_test, y_train, y_test)
