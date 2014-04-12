// -*- C++ -*-
//
// Package:    RPCPointProducer
// Class:      RPCPointProducer
// 
/**\class RPCPointProducer RPCPointProducer.cc Analysis/RPCPointProducer/src/RPCPointProducer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Camilo Andres Carrillo Montoya
//         Created:  Wed Sep 16 14:56:18 CEST 2009
// $Id: RPCPointProducer.cc,v 1.11 2012/03/29 12:57:05 carrillo Exp $
//
//

#include "RecoLocalMuon/RPCRecHit/interface/RPCPointProducer.h"

// system include files

#include <memory>
#include <ctime>

// user include files

RPCPointProducer::RPCPointProducer(const edm::ParameterSet& iConfig)
{
  cscSegments=iConfig.getParameter<edm::InputTag>("cscSegments");
  dt4DSegments=iConfig.getParameter<edm::InputTag>("dt4DSegments");
//  debug=iConfig.getUntrackedParameter<bool>("debug",false);
//  incldt=iConfig.getUntrackedParameter<bool>("incldt",true);
//  inclcsc=iConfig.getUntrackedParameter<bool>("inclcsc",true);
//  MinCosAng=iConfig.getUntrackedParameter<double>("MinCosAng",0.95);
//  MaxD=iConfig.getUntrackedParameter<double>("MaxD",80.);
//  MaxDrb4=iConfig.getUntrackedParameter<double>("MaxDrb4",150.);
//  ExtrapolatedRegion=iConfig.getUntrackedParameter<double>("ExtrapolatedRegion",0.5);

  debug=iConfig.getUntrackedParameter<bool>("debug");
  incldt=iConfig.getUntrackedParameter<bool>("incldt");
  inclcsc=iConfig.getUntrackedParameter<bool>("inclcsc");
  MinCosAng=iConfig.getUntrackedParameter<double>("MinCosAng");
  MaxD=iConfig.getUntrackedParameter<double>("MaxD");
  MaxDrb4=iConfig.getUntrackedParameter<double>("MaxDrb4");
  ExtrapolatedRegion=iConfig.getUntrackedParameter<double>("ExtrapolatedRegion");

  produces<RPCRecHitCollection>("RPCDTExtrapolatedPoints");
  produces<RPCRecHitCollection>("RPCCSCExtrapolatedPoints");

}


RPCPointProducer::~RPCPointProducer(){

}

void RPCPointProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup){
  /*
  struct timespec start_time, stop_time;
  time_t fs;
  time_t fn;
  time_t ls;
  time_t ln;
  clock_gettime(CLOCK_REALTIME, &start_time);  
  */

  if(incldt){
    edm::Handle<DTRecSegment4DCollection> all4DSegments;
    iEvent.getByLabel(dt4DSegments, all4DSegments);
    if(all4DSegments.isValid()){
      DTSegtoRPC DTClass(all4DSegments,iSetup,iEvent,debug,ExtrapolatedRegion);
      std::auto_ptr<RPCRecHitCollection> TheDTPoints(DTClass.thePoints());     
      iEvent.put(TheDTPoints,"RPCDTExtrapolatedPoints"); 
    }else{
      if(debug) std::cout<<"RPCHLT Invalid DTSegments collection"<<std::endl;
    }
  }

  if(inclcsc){
    edm::Handle<CSCSegmentCollection> allCSCSegments;
    iEvent.getByLabel(cscSegments, allCSCSegments);
    if(allCSCSegments.isValid()){
      CSCSegtoRPC CSCClass(allCSCSegments,iSetup,iEvent,debug,ExtrapolatedRegion);
      std::auto_ptr<RPCRecHitCollection> TheCSCPoints(CSCClass.thePoints());  
//rumi
//    RPCRecHitCollection::const_iterator myrpcPoint;
//  
//    for(myrpcPoint = (CSCClass.thePoints())->begin(); myrpcPoint != (CSCClass.thePoints())->end(); myrpcPoint++){
//      RPCDetId  rpcId = myrpcPoint->rpcId();
//std::cout << "echo from producer:\t" << rpcId << std::endl;
//rumi
}



      iEvent.put(TheCSCPoints,"RPCCSCExtrapolatedPoints"); 
    }
    else{
      if(debug) std::cout<<"RPCHLT Invalid CSCSegments collection"<<std::endl;
    }
  }
}

// ------------ method called once each job just before starting event loop  ------------
void 
RPCPointProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RPCPointProducer::endJob() {
}


