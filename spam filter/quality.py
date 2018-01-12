from collections import namedtuple
from utils import *

def compute_confusion_matrix(truth_dict, pred_dict, pos_tag = True, neg_tag = False):
    ConfMat = namedtuple ('ConfMat', 'tp tn fp fn')
    tp, tn, fp, fn = 0,0,0,0
    for email in pred_dict:
        if email not in truth_dict:
            continue
        if (pred_dict[email] == pos_tag):
            if (truth_dict[email] == pos_tag):
                tp += 1
                continue
            if (truth_dict[email] == neg_tag):
                fp += 1
                continue
        if (pred_dict[email] == neg_tag):
            if (truth_dict[email] == neg_tag):
                tn += 1
                continue
            if (truth_dict[email] == pos_tag):
                fn += 1
                continue
    mat = ConfMat (tp,tn,fp,fn)
    return mat


def quality_score (tp,tn,fp,fn):
    if tp + tn + fp + fn == 0:
        return -1
    return (tp+tn)/(tp+tn+10*fp+fn)


def compute_quality_for_corpus(corpus_dir):
    truth = read_classification_from_file(corpus_dir + '/!truth.txt')
    prediction = read_classification_from_file(corpus_dir + '/!prediction.txt')
    conf_mat = compute_confusion_matrix(truth, prediction, "SPAM", 'OK')
    score = quality_score (conf_mat.tp, conf_mat.tn, conf_mat.fp, conf_mat.fn)
    return score
    
    



    