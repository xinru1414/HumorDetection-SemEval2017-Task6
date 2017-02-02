# echo 'Make sure to install kenlm for example: pip install https://github.com/kpu/kenlm/archive/master.zip'
pip install https://github.com/kpu/kenlm/archive/master.zip
python avocado.py lm_train_dir/lm_train_data plain.txt
kenlm-master/build/bin/lmplz -o 3 -S 70% < plain.txt > text.arpa
python beets.py evaluation_dir/evaluation_data/ lm_train_result/lm_score/
python cilantro_b.py lm_train_result/lm_score/

# echo 'Now please nevigate to your kenlm dirctory and run following commands to complie and train the languge model'
# echo 'Compling commands: '
# echo 'mkdir -p build'
# echo 'cd build'
# echo 'cmake ..'
# echo 'make -j 4'
# echo 'Training language model command example: '
# echo '/kenlm/build/bin/lmplz -o 3 -S 70% </path/to/the/plain/text/file/plain.txt > text.arpa'

