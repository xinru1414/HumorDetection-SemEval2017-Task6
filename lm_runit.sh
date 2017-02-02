# echo 'Make sure to install kenlm for example: pip install https://github.com/kpu/kenlm/archive/master.zip'
#echo 'Installing kenlm'
#pip install https://github.com/kpu/kenlm/archive/master.zip
echo 'Getting training data ready'
python src/avocado.py mydata/lm_train_dir/lm_train_data mydata/plain.txt
echo 'Training languge model'
code/kenlm-master/build/bin/lmplz -o 3 -S 70% < mydata/plain.txt > mydata/text.arpa
echo 'Getting language model scores'
python src/beets.py data/evaluation_dir/evaluation_data/ mydata/lm_train_result/lm_score/
echo 'Getting result for task a'
python src/cilantro_a.py mydata/lm_train_result/lm_score/
echo 'Getting result for task b'
python src/cilantro_b.py mydata/lm_train_result/lm_score/

# echo 'Now please nevigate to your kenlm dirctory and run following commands to complie and train the languge model'
# echo 'Compling commands: '
# echo 'mkdir -p build'
# echo 'cd build'
# echo 'cmake ..'
# echo 'make -j 4'
# echo 'Training language model command example: '
# echo '/kenlm/build/bin/lmplz -o 3 -S 70% </path/to/the/plain/text/file/plain.txt > text.arpa'

