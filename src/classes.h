#include <string>
#include <vector>
#include <utility>
#include "DataFormats/Common/interface/Wrapper.h"

namespace {
  struct dictionary {
  	//std::pair<std::string,float> psf;
	//std::vector<std::pair<std::string,float> > vpsf;
	std::vector<std::vector<std::pair<std::string,float> > > vvpsf;
	//edm::Wrapper<std::vector<std::pair<std::string,float> > > wvpsf;
	edm::Wrapper<std::vector<std::vector<std::pair<std::string,float> > > > wvvpsf;
  };
}