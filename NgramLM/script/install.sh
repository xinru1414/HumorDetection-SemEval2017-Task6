echo 'Installing kenlm'
pip install https://github.com/kpu/kenlm/archive/master.zip

cd ../KenLM/kenlm-master
mkdir -p build
cd build
cmake ..
make -j 4
cd ../../..
