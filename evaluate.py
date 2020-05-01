from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,precision_score,recall_score,f1_score
import itertools
import matplotlib.pyplot as plt
import numpy as np

def plot_confusion_matrix(cm, classes):
    plt.imshow(cm, cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=30)
    plt.yticks(tick_marks, classes)

    threshold = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, round(cm[i, j],2),
                 horizontalalignment="center", 
                 color="white" if cm[i, j] > threshold else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    
def calculate_performance_metrics(y,y_pred,p_average="weighted",r_average="weighted",f1_average="weighted",normalize_cm="true",figsize=(8,8),n_prec=2):
    classes = list(set(y))
    print(f'Acurracy Score : {round(accuracy_score(y, y_pred),n_prec)}')
    print(f'Precision Score : {round(precision_score(y, y_pred,average="weighted"),n_prec)}')
    print(f'Recall Score : {round(recall_score(y, y_pred,average="weighted"),n_prec)}')
    print(f'F1 Score : {round(f1_score(y, y_pred,average="weighted"),n_prec)}')
    cnf_matrix = confusion_matrix(y, y_pred, labels=classes,normalize=normalize_cm)
    plt.figure(figsize=figsize)
    plot_confusion_matrix(cnf_matrix, classes)
