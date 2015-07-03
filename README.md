# ERE_RE
=======

Tools for relation extraction with FCM.

These tools are used in the following paper:

Mo Yu, Matthew R. Gormley, Mark Dredze. Combining Word Embeddings and Feature Embeddings for Fine-grained Relation Extraction. NAACL 2015.

###################
#CODE DESCRIPTION:#
###################

We provide two tools in this package:

#######################################
#Feature-Rich Compositional Model(FCM)#
#######################################
code/fcm:

We build the tools for ACE and ERE relation extraction on top of the FCM code from https://github.com/Gorov/FCM_nips_workshop.

#######
#LRFCM#
#######
code/lrfcm:

The code for low-rank FCM proposed in our paper.

###################
#DATA DESCRIPTION:#
###################
data_split/{ace|ere}/:

Our data split for ACE 2005 and ERE.

emb/:

The word embeddings used in our paper (filtered based on the ACE and ERE vocabulary).

References
=======
If you want to cite this tool, please using the following bibtext:

@InProceedings{yu-gormley-dredze:2015:NAACL-HLT,

  author    = {Yu, Mo  and  Gormley, Matthew R.  and  Dredze, Mark},
  
  title     = {Combining Word Embeddings and Feature Embeddings for Fine-grained Relation Extraction},
  
  booktitle = {Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  
  month     = {May--June},
  
  year      = {2015},
  
  address   = {Denver, Colorado},
  
  publisher = {Association for Computational Linguistics},
  
  pages     = {1374--1379},
  
  url       = {http://www.aclweb.org/anthology/N15-1155}
}

For questions, comments or to report bugs, please contact gflfof@gmail.com
