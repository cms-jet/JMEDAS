#!/bin/bash

CMSSW_VER="CMSSW_10_6_6"
KERNEL_NAME="hats-jec"

set -e
# Get the CMSSW libraries (specifically ROOT)
SCRAM_ARCH=$(ls -d /cvmfs/cms.cern.ch/$(/cvmfs/cms.cern.ch/common/cmsos)*/cms/cmssw/${CMSSW_VER} | tail -n 1 | awk -F / '{ print $4 }')
export SCRAM_ARCH
source /cvmfs/cms.cern.ch/cmsset_default.sh
#if [ -d $CMSSW_VER ]; then
#    rm -rf $CMSSW_VER
#fi
##cd $HOME
#scramv1 project CMSSW $CMSSW_VER
#
#cd $CMSSW_VER/src
#eval `scramv1 runtime -sh`
#scram b

export LD_LIBRARY_PATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/biglib/slc7_amd64_gcc820:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/lib/slc7_amd64_gcc820:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/external/slc7_amd64_gcc820/lib:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0-nmpfii/lib64:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/lib64:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/lib:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cuda/10.1.105-pafccj2/drivers:\
/usr/lib64/root:$LD_LIBRARY_PATH;
export PATH=/cvmfs/cms.cern.ch/share/overrides/bin:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/bin/slc7_amd64_gcc820:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/external/slc7_amd64_gcc820/bin:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0-nmpfii/bin:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin:\
/afs/cern.ch/cms/caf/scripts:\
/cvmfs/cms.cern.ch/common:\
/cvmfs/cms.cern.ch/bin:\
/usr/sue/bin:\
/usr/lib64/qt-3.3/bin:\
/usr/condabin:\
/usr/local/bin:\
/usr/bin:\
/usr/local/sbin:\
/usr/sbin:\
/opt/puppetlabs/bin:\
$PATH;
export PYTHON27PATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/python:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/lib/slc7_amd64_gcc820:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/coral/CORAL_2_3_21-nmpfii4/slc7_amd64_gcc820/python:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/coral/CORAL_2_3_21-nmpfii4/slc7_amd64_gcc820/lib:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xrootd/4.9.1-nmpfii/lib/python2.7/site-packages:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fastjet/3.3.0-pafccj/lib/python2.7/site-packages:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw-tool-conf/45.0-nmpfii6/lib/python2.7/site-packages:\
$PYTHON27PATH;
export PYTHON3PATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/python:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/lib/slc7_amd64_gcc820:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw-tool-conf/45.0-nmpfii6/lib/python3.6/site-packages\
$PYTHON3PATH;
export ROOT_INCLUDE_PATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_6/src:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/coral/CORAL_2_3_21-nmpfii4/include/LCG:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mctester/1.25.0a-nmpfii5/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09-nmpfii5/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dd4hep/v01-10x-nmpfii5/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-nmpfii/include/QtDesigner:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/herwigpp/7.1.4-nmpfii6/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tauolapp/1.1.5-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/charybdis/1.003-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-nmpfii/include/QtOpenGL:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-nmpfii/include/QtGui:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/thepeg/2.1.4-nmpfii6/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pythia8/240-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/herwig/6.521-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/rivet/2.7.2-nmpfii5/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-nmpfii/include/Qt3Support:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lwtnn/2.9/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/classlib/3.1.3-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lhapdf/6.2.1-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cgal/4.2-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tkonlinesw/4.2.0-1_gcc7-nmpfii5/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/starlight/r193-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-nmpfii/include/Qt:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-nmpfii/include/QtCore:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-nmpfii/include/QtXml:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mcdb/1.0.3-pafccj/interface:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libungif/4.1.4-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libtiff/4.0.10-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libpng/1.6.35/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/frontier_client/2.8.20-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pcre/8.37-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/boost/1.67.0-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/zstd/1.4.0-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xrootd/4.9.1-nmpfii/include/xrootd/private:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/vdt/0.4.0-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/valgrind/3.13.0-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/utm/utm_0.7.1-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/toprex/4.23-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tbb/2019_U8/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tauola/27.121.5-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sigcpp/2.6.2-pafccj/include/sigc++-2.0:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sqlite/3.22.0-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/protobuf/3.5.2-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pacparser/1.3.5-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/oracle/12.1.0.2.0-pafccj2/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-numpy/1.16.2-nmpfii2/c-api/core/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/meschach/1.2.pCMS1-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libuuid/2.34/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libunwind/1.3.1/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libhepml/0.2.1-pafccj/interface:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/ktjet/1.06-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/jimmy/4.2-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/jemalloc/5.2.0/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/madgraph5amcatnlo/2.6.0-nmpfii6:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/heppdt/3.03.00-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hector/1.3.4_patch1-nmpfii5/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libjpeg-turbo/2.0.2/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/giflib/5.2.0/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gsl/2.2.1-nmpfii2/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gdbm/1.10-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/freetype/2.10.0/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fftw3/3.3.8/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fftjet/1.5.0-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fastjet/3.3.0-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/expat/2.1.0-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dpm/1.8.0.1-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hepmc/2.06.07-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/vecgeom/v00.05.00-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xerces-c/3.1.3-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xz/5.2.4/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dcap/2.47.12/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libxml2/2.9.9/include/libxml2:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/curl/7.59.0-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cppunit/1.40.1-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/clhep/2.4.0.0-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/openssl/1.0.2d-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pythia6/426-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/photos/215.5-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/zlib-x86_64/1.2.11-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cascade/2.2.04-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/bz2lib/1.0.6-pafccj/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/python/2.7.15-pafccj/include/python2.7:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tinyxml2/6.2.0-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/ittnotify/16.06.18-nmpfii/include:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gosamcontrib/2.0-20150803-pafccj/include:\
/usr/local/include:\
/usr/include;
export ROOT_PATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/madgraph5amcatnlo/2.6.0-nmpfii6:\
/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gosamcontrib/2.0-20150803-pafccj;
export PYTHONHOME=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/python/2.7.15-pafccj/
export PYTHONPATH=$PYTHON27PATH
export EOS_MGM_URL=root://eostotem.cern.ch

#git clone https://github.com/cms-jet/JMEDAS.git Analysis/JMEDAS -b DASSep2020
#git clone https://github.com/cms-jet/JetToolbox Analysis/JetToolbox -b jetToolbox_102X_v3
scramv1 b -j 2
cd ..

# Make a wrapper script to load CMSSW python
cat << 'EOF' > bin/python_wrapper.sh
#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd $DIR
eval `scramv1 runtime -sh`
cd -
exec python "$@"
EOF
chmod +x bin/python_wrapper.sh

# Create the kernel
mkdir -p "$HOME/.local/share/jupyter/kernels/$KERNEL_NAME"
cat << EOF > "$HOME/.local/share/jupyter/kernels/$KERNEL_NAME/kernel.json"
{
 "display_name": "$KERNEL_NAME",
 "language": "python",
 "argv": [
  "$PWD/bin/python_wrapper.sh",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ]
}
EOF


# Report OK
echo "Loaded $CMSSW_VERSION into $KERNEL_NAME!"
